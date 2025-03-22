import pandas as pd
import sqlite3

db_connection = sqlite3.connect("superstore.db")

query_top_products = "SELECT `Product Name`, SUM(Quantity) as TotalQuantity FROM Orders GROUP BY `Product Name` ORDER BY TotalQuantity DESC LIMIT 5"
top_products_df = pd.read_sql(query_top_products, db_connection)

query_top_city = "SELECT City, SUM(Sales) as TotalSales FROM Orders GROUP BY City ORDER BY TotalSales DESC LIMIT 1"
top_city_df = pd.read_sql(query_top_city, db_connection)

db_connection.close()
print(f"5 produtos mais vendidos em quantidade: \n{top_products_df}")
print(f"\nCidade com maior volume de vendas: \n{top_city_df}")