import pandas as pd
import sqlite3

db_connection = sqlite3.connect('superstore.db')

query = "SELECT * FROM Orders"
df = pd.read_sql(query, db_connection)

df['Sales'] = df['Sales'].fillna(0)
df['Discount'] = df['Discount'].fillna(0)
df['Product Name'] = df['Product Name'].fillna("Não Informado")

df['Total com desconto'] = df['Sales'] - (df['Sales'] * df['Discount'])

df = df.sort_values(by='Sales', ascending=False)
df.to_sql('Orders', db_connection, if_exists='replace', index=False)

db_connection.close()
print("Banco de dados atualizado com sucesso!")