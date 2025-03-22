import sqlite3
import pandas as pd

conn = sqlite3.connect("superstore.db")

query = """
SELECT City, AVG(Sales) AS Avg_Sales
FROM Orders
GROUP BY City
ORDER BY Avg_Sales DESC;
"""

df = pd.read_sql_query(query, conn)
conn.close()

print(df)