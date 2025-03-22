import pandas as pd

df = pd.read_csv('Superstore.csv', encoding='latin1')
num_linhas, num_colunas = df.shape

print(f"Primeiras 5 linhas do dataset: \n {df.head()}")

print(f"\nTipos de dados das colunas: \n {df.dtypes}")

print(f"\nO dataset tem {num_linhas} linhas e {num_colunas} colunas.")

if df.isnull().any().any():
    print(f"\nValores nulos por coluna: \n {df.isnull().sum()}")
else:
    print("Não há valores nulos.")