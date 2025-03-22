import sqlite3
import pandas as pd

conn = sqlite3.connect("superstore.db")

query = "SELECT `Row ID`, Quantity FROM Orders"
df = pd.read_sql_query(query, conn)

if (df["Quantity"] < 0).any():
    print("Alerta: Foram encontrados valores negativos na coluna 'Quantity'!")

    df.loc[df["Quantity"] < 0, "Quantity"] = 0
    for index, row in df.iterrows():
        conn.execute("UPDATE Orders SET Quantity = ? WHERE [Row ID] = ?", (row["Quantity"], row["Row ID"]))
    
    conn.commit()
    print("Valores negativos corrigidos no banco de dados!")
else:
    print("Não há valores negativos.")
conn.close()
