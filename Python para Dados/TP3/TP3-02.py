import pandas as pd

df = pd.read_csv('Superstore.csv', encoding='latin1')
df.to_excel("Superstore.xlsx", index=False)

df = pd.read_excel("Superstore.xlsx")

df[df['Order Date'].str.contains("2015")].to_excel("Orders_2015.xlsx", index=False)
df[df['Order Date'].str.contains("2016")].to_excel("Orders_2016.xlsx", index=False)

orders_2015 = pd.read_excel("Orders_2015.xlsx")
orders_2016 = pd.read_excel("Orders_2016.xlsx")

combined_orders = pd.concat([orders_2015, orders_2016], ignore_index=True)

combined_orders.to_excel("Combined_Orders.xlsx", index=False)

print("Arquivos combinados com sucesso!")