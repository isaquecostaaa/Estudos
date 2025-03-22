import pandas as pd

try:
    df = pd.read_csv("arquivo_inexistente.csv")
except FileNotFoundError:
    pass

print("O programa continua executando mesmo sem o arquivo.")
