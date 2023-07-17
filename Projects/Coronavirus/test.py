import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Exemplo de DataFrame com as colunas "ano" e "vendas"
data = {
    'ano': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    'vendas': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
}

df = pd.DataFrame(data)

# Separar os dados em variáveis de entrada (X) e saída (y)
X = df['ano'].values.reshape(-1, 1)  # Precisamos de uma matriz 2D para a regressão linear
y = df['vendas'].values

print(X)

# Criar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X, y)

# Fazer previsões para os próximos anos (2020, 2021, 2022, etc.)
anos_futuros = np.arange(2020, 2030).reshape(-1, 1)  # Novamente, precisamos de uma matriz 2D
vendas_previstas = modelo.predict(anos_futuros)

# Imprimir as previsões
for ano, venda in zip(anos_futuros.ravel(), vendas_previstas):
    print(f"Ano: {ano}, Vendas previstas: {venda:.2f}")
