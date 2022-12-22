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

