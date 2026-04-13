import pandas as pd
import matplotlib.pyplot as plt

#==============================
#Leitura dos dados
#==============================
dados=pd.read_csv("dados/dados.csv")

#==============================
#Visualização inicial
#==============================
print(dados.head(10))

#==============================
#Histograma
#==============================
dados['nota'].hist(bins=5)
plt.title('Distribuição das Notas')
plt.xlabel('Notas')
plt.ylabel('Quantidade')
plt.savefig('histo.png')
plt.clf() #limpa o gráfico antes do próximo

#==============================
#Boxplot
#==============================
dados.boxplot(column=['nota'])
plt.title('Boxplot das Notas')
plt.savefig('boxplot.png')
plt.clf()

#==============================
#Estatísticas
#==============================
print("Média idade:", dados['idade'].mean())
print("Mediana:", dados['nota'].median())
print("Desvio padrão:", dados['nota'].std())