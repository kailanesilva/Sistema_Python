import pandas as pd
from sklearn.linear_model import LinearRegression

# Exemplo de dados de vendas
dados_vendas = {
    'data': ['2023-10-01', '2023-11-01', '2023-12-01', '2024-01-01'],
    'quantidade_vendida': [100, 150, 200, 250]
}

# Função que faz a previsão de demanda
def prever_demanda():
    # Carregar os dados em um DataFrame
    df = pd.DataFrame(dados_vendas)
    df['data'] = pd.to_datetime(df['data'])
    df.set_index('data', inplace=True)

    # Previsão com Regressão Linear
    X = (df.index - df.index.min()).days.values.reshape(-1, 1)
    y = df['quantidade_vendida'].values

    modelo = LinearRegression()
    modelo.fit(X, y)

    # Prever a demanda futura
    dias_futuros = 30  # Prever para os próximos 30 dias
    X_futuro = [[(df.index.max() - df.index.min()).days + dias_futuros]]
    previsao = modelo.predict(X_futuro)

    print(f"Demanda prevista para os próximos {dias_futuros} dias: {previsao[0]}")
