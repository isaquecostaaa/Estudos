import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import re
from AT_01 import limpar_titulo


DATABASE_URL = "sqlite:///imdb.db"
Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    rating = Column(Float)

class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    seasons = Column(Integer)
    episodes = Column(Integer)

def create_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

def save_movie(session, title, year, rating):
    try:
        movie = Movie(title=title, year=year, rating=rating)
        session.add(movie)
        session.commit()
    except Exception as e:
        print(f"Erro ao inserir o filme: {e}")
        session.rollback()

def save_series(session, title, year, rating, seasons, episodes):
    try:
        serie = Series(title=title, year=year, rating=rating, seasons=seasons, episodes=episodes, )
        session.add(serie)
        session.commit()
    except Exception as e:
        print(f"Erro ao inserir a série: {e}")
        session.rollback()

def get_movies():
    url = "https://www.imdb.com/chart/top/"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
    except requests.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    
    ul = soup.find("ul", class_="ipc-metadata-list")
    
    movies = ul.select("h3.ipc-title__text") if ul else []
    metadata_divs = ul.select("div.sc-2bbfc9e9-6.cZkKPy.cli-title-metadata") if ul else []
    ratings = ul.select(".ipc-rating-star--rating") if ul else []


    movie_data = []
    for i in range(len(movies)):
        try:
            title = movies[i].text.strip()
            formated_title = limpar_titulo(title)
            
            year_span = metadata_divs[i].select("span")[0] if i < len(metadata_divs) else None
            year = int(year_span.text) if year_span and year_span.text.isdigit() else "N/A"

            rating = float(ratings[i].text) if i < len(ratings) and ratings[i].text.replace(".", "").isdigit() else "N/A"

            movie_data.append({"title": formated_title, "year": year, "rating": rating})
        except (AttributeError, ValueError, IndexError) as e:
            print(f"Erro ao processar filme {movies[i].text if i < len(movies) else 'desconhecido'}: {e}")

    
    return movie_data


def get_series():
    base_url = "https://www.imdb.com"
    list_url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"

    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(list_url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao acessar {list_url}: {e}")
        return []


    soup = BeautifulSoup(response.text, "html.parser")

    series_links = []
    series_data = []

    for item in soup.select("li.ipc-metadata-list-summary-item a.ipc-title-link-wrapper"):
        try:
            series_links.append(base_url + item["href"].split("?")[0]) 
        except (KeyError, IndexError) as e:
            print(f"Erro ao extrair link de série: {e}")

    for link in series_links:
        try:
            series_response = requests.get(link, headers=headers)
            series_soup = BeautifulSoup(series_response.text, "html.parser")

            title = rating = year = seasons = episodes = "Não encontrado"


            title = series_soup.select_one("h1").text.strip()
            episodes = int(series_soup.select_one("h3.ipc-title__text span.ipc-title__subtext").text)
            rating = float(series_soup.select_one("span.sc-d541859f-1.imUuxf").text)

            seasons_element = series_soup.select_one("#browse-episodes-season")
            if seasons_element:
                aria_label = seasons_element.get("aria-label", "")
                match = re.search(r"\d+", aria_label) 
                seasons = int(match.group()) if match else 1
            else:
                seasons = 1


            release_date_li = series_soup.select_one("li[data-testid='title-details-releasedate']")
            if release_date_li:
                release_date_text = release_date_li.select_one("div.ipc-metadata-list-item__content-container a").text 
                match = re.search(r"\b\d{4}\b", release_date_text)
                year = int(match.group()) if match else None
            else:
                year = None

            series_data.append({"title": title, "year": year, "rating": rating,"seasons": seasons,"episodes": episodes})

        except (AttributeError, ValueError, TypeError, requests.RequestException) as e:
            print(f"Erro ao processar série {link}: {e}")

    return series_data

def main():
    create_db()

    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    movies = get_movies()
    series = get_series()

    for movie in movies:
        save_movie(session, movie["title"], movie["year"], movie["rating"])

    for serie in series:
        save_series(session, serie["title"], serie["year"], serie["rating"], serie["seasons"], serie["episodes"])

    session.close()

if __name__ == "__main__":
    main()