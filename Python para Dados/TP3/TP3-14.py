import pandas as pd

df = pd.read_csv("Superstore.csv", encoding='latin1')

pedidos_lucrativos = df[df["Profit"] > 0]

pedidos_lucrativos.to_csv("pedidos_lucrativos.csv", index=False)

print("Arquivo 'pedidos_lucrativos.csv' foi criado com sucesso!")
