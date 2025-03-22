import pandas as pd

try:
    df = pd.read_csv("superstore.csv", encoding='latin1')
    
    pedidos_lucrativos = df[df["Profit"] > 0]
    
    resumo_vendas = pedidos_lucrativos.groupby("City")["Sales"].sum().reset_index()
    resumo_vendas.to_csv("resumo_vendas.csv", index=False)
    
    print("O arquivo 'resumo_vendas.csv' foi criado com sucesso!")

except FileNotFoundError:
    print("Erro: O arquivo 'superstore.csv' não foi encontrado. Verifique o caminho e tente novamente!")
except pd.errors.EmptyDataError:
    print("Erro: O arquivo está vazio. Verifique o conteúdo do arquivo!")
except pd.errors.ParserError:
    print("Erro: Problema ao ler o arquivo. Verifique se ele está formatado corretamente!")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
