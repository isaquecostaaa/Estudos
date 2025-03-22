import pandas as pd 

try:
    df = pd.read_csv('dados_inexistentes.csv')
except FileNotFoundError:
    print("O arquivo não foi encontrado. Verifique o nome e tente novamente!")