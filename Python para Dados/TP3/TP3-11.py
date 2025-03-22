import pandas as pd

try:
    df = pd.read_csv("exemplo.csv")
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado. Verifique o nome e tente novamente!")
except pd.errors.EmptyDataError:
    print("Erro: O arquivo está vazio.")
except pd.errors.ParserError:
    print("Erro: Problema ao ler o arquivo. Verifique se ele está formatado corretamente.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
else:
    print("Arquivo carregado com sucesso!")