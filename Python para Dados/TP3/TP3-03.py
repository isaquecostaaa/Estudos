import pandas as pd
import sqlite3

db_connection = sqlite3.connect("superstore.db")

df = pd.read_csv("Superstore.csv", encoding='latin1')

df.to_sql("Orders", db_connection, if_exists="replace", index=False)

loaded_df = pd.read_sql("SELECT * FROM Orders", db_connection)

db_connection.close()
print("Banco de dados criado e dados inseridos com sucesso.")