import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///imdb.db"

def load_data():
    try:
        engine = create_engine(DATABASE_URL)
        
        movies_df = pd.read_sql("SELECT * FROM movies", con=engine)
        series_df = pd.read_sql("SELECT * FROM series", con=engine)
        
        print("Filmes:")
        print(movies_df.head(), "\n")

        print("Séries:")
        print(series_df.head(), "\n")

    except Exception as e:
        print(f"Erro ao consultar o banco de dados: {e}")

if __name__ == "__main__":
    load_data()
