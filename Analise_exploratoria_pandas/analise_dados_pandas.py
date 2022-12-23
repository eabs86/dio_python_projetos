import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

plt.style.use("seaborn")

df = pd.read_excel("E:/Professional/Documents/dio/python/Projetos/Analise_exploratoria_pandas/AdventureWorks.xlsx")

df.head()   #valor da venda = receita = Quantidade x Preço Unitário

#verificando se há valores faltantes na base de dados:

df.isnull().sum() # não há valores ausentes

# df.shape    #tamanho da base (904,16)
# df.dtypes

receita_total = df['Valor Venda'].sum()

print(receita_total)

#custo total

df['custo'] = df['Custo Unitário'].mul(df['Quantidade'])
custo_total = df['custo'].sum()

#lucro

df['lucro'] = df['Valor Venda'] - df['custo']

lucro_total = df['lucro'].sum()

#tempo de envio

df['tempo envio'] = (df['Data Envio']-df['Data Venda']).dt.days


# média do tempo (em dias) de envio para cada marca

media_tempo_envio = df.groupby('Marca')['tempo envio'].mean()

# Lucro por ano e por marca => primeiro faz o agrupamentpo por ano e por marca, para filtrar depois pelo lucro

pd.options.display.float_format = '{:20,.2f}'.format

ano_marca = df.groupby([df['Data Venda'].dt.year, 'Marca'])['lucro'].sum()

# resetar o indexador

lucro_ano = df.groupby([df['Data Venda'].dt.year, 'Marca'])['lucro'].sum().reset_index()

# Total de produtos vendidos

produtos_vendidos = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)

# Gráfico do Total de Produtos vendidos

produtos_vendidos = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=True).plot.barh(title = 'Total de Produtos Vendidos')
plt.xlabel('Total')
plt.ylabel('Produtos')
plt.show()

# Plotando o Lucro por ano

df.groupby(df['Data Venda'].dt.year)['lucro'].sum().plot.bar(title = 'Lucro x Ano')
plt.xlabel('Ano')
plt.ylabel('Lucro')
plt.show()


# Apenas as vendas do ano de 2009

df_2009 = df[df['Data Venda'].dt.year==2009]

# Lucro por mês
df_2009.groupby(df_2009['Data Venda'].dt.month)['lucro'].sum().plot(title='Lucro x Mês')
plt.xlabel("Mês")
plt.ylabel("Lucro")
plt.show()

# Lucro por marca
df_2009.groupby('Marca')['lucro'].sum().plot.bar(title = 'Lucro x Marca')
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation = 30)
plt.show()

# Lucro por Classe

df_2009.groupby('Classe')['lucro'].sum().plot.bar(title = 'Lucro x Classe')
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation = 'horizontal')
plt.show()

# analise estatísticas 

# análise no tempo de envio (em dias)
df['tempo envio'].describe()

# gráfico de boxplot

plt.boxplot(df['tempo envio'])
plt.show()

#gráfico em histograma

plt.hist(df['tempo envio'])
plt.show()

# filtrando para saber quem tem o tempo de envio = 20 (outlier)

df[df['tempo envio']==20]

