import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do CSV
data = pd.read_csv('imc_dataset.csv')

# Mapear as categorias de rótulo para cores
label_colors = {
    'Underweight': 'red',
    'Normal Weight': 'green',
    'Overweight': 'blue',
    'Obese': 'purple'
}

# Criar a figura e os subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Legenda do gráfico de dispersão
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', label='Underweight', markerfacecolor='red', markersize=8),
    plt.Line2D([0], [0], marker='o', color='w', label='Normal Weight', markerfacecolor='green', markersize=8),
    plt.Line2D([0], [0], marker='o', color='w', label='Overweight', markerfacecolor='blue', markersize=8),
    plt.Line2D([0], [0], marker='o', color='w', label='Obese', markerfacecolor='purple', markersize=8)
]
axes[0].legend(handles=legend_elements, loc='upper right')

# Gráfico de barras - Distribuição de classes de IMC
imc_classes = ['Underweight', 'Normal Weight', 'Overweight', 'Obese']
imc_counts = data['Label'].value_counts()
bar_colors = [label_colors[label] for label in imc_classes]  # Mapear as cores com base nas categorias de rótulo
axes[0].bar(imc_classes, imc_counts, color=bar_colors)
axes[0].set_xlabel('IMC Classes')
axes[0].set_ylabel('Contagem')
axes[0].set_title('Distribuição de classes de IMC')

# Remover os nomes dos rótulos do eixo x
plt.sca(axes[0])
plt.xticks([])

# Ajustar o espaçamento entre os subplots
plt.tight_layout()

# Gráfico de pizza - Distribuição de gênero
gender_counts = data['Gender'].value_counts()
axes[2].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
axes[2].set_title('Distribuição de gênero')

# Gráfico de dispersão - Relação entre altura e peso
heights = data['Height']
weights = data['Weight']
labels = data['Label']
scatter_colors = [label_colors[label] for label in labels]  # Mapear as cores com base nas categorias de rótulo
scatter = axes[1].scatter(heights, weights, c=scatter_colors)
axes[1].set_xlabel('Altura(cm)')
axes[1].set_ylabel('Peso(kg)')
axes[1].set_title('Relação entre altura e peso')

# Ajustar o layout e exibir os gráficos
plt.tight_layout()
plt.show()
