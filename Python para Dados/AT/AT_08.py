""" Salve os dados de filmes e séries em arquivos separados (movies.csv e series.csv).
Salve os dados de filmes e séries no formato JSON (movies.json e series.json).
Use try-except para evitar erros de escrita. """

import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///imdb.db"

def export_data():
    try:
        engine = create_engine(DATABASE_URL)

        movies_df = pd.read_sql("SELECT * FROM movies", con=engine)
        series_df = pd.read_sql("SELECT * FROM series", con=engine)

        movies_df.to_csv("movies.csv", index=False)
        series_df.to_csv("series.csv", index=False)

        movies_df.to_json("movies.json", orient="records", indent=4)
        series_df.to_json("series.json", orient="records", indent=4)

        print("Dados exportados com sucesso:")
        print("- Arquivos CSV: movies.csv, series.csv")
        print("- Arquivos JSON: movies.json, series.json")

    except Exception as e:
        print(f"Erro ao exportar os dados: {e}")

if __name__ == "__main__":
    export_data()
