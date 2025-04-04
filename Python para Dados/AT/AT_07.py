import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///imdb.db"

def analyze_movies():
    try:
        engine = create_engine(DATABASE_URL)
        
        movies_df = pd.read_sql("SELECT * FROM movies", con=engine)

        movies_sorted = movies_df.sort_values(by="rating", ascending=False)

        top_movies = movies_sorted[movies_sorted["rating"] > 9.0]

        print("filmes com rating acima de 9.0:")
        print(top_movies.head(), "\n")

        print("Filmes mais bem avaliados:")
        print(movies_sorted.head())

    except Exception as e:
        print(f"Erro ao consultar o banco de dados: {e}")

if __name__ == "__main__":
    analyze_movies()
