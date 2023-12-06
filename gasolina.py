
# Importando bibliotecas 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados do CSV
gas_df = pd.read_csv('/content/gasoline-ebac/gasolina.csv')

# Criando o gráfico
plt.figure(figsize=(12, 6))
sns.lineplot(x='dia', y='venda', data=gas_df)
plt.title('Preço da Gasolina ao longo do Tempo')
plt.xlabel('Dia')
plt.ylabel('Preço')

# Salvando o gráfico em .png
plt.savefig('gasolina.png')
