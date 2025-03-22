import pandas as pd
import sqlite3

db_connection = sqlite3.connect("superstore.db")

query = "SELECT * FROM Orders WHERE Profit > 100 AND Segment = 'Consumer'"
filtered_df = pd.read_sql(query, db_connection)

db_connection.close()
print(filtered_df)