import sqlite3

db_connection = sqlite3.connect("superstore.db")
cursor = db_connection.cursor()

delete_query = "DELETE FROM Orders WHERE Sales < 50"
cursor.execute(delete_query)
print(f"Pedidos com vendas menores que R$ 50,00 foram excluidos.")

update_query = "UPDATE Orders SET `Ship Mode` = 'Pedido em Revisão' WHERE Quantity > 10"
cursor.execute(update_query)
print(f"Pedidos com quantidade maior que 10 foram atualizados para 'Pedido em Revisao'.")

db_connection.commit()
db_connection.close()
