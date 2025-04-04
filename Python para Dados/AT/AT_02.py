import requests
from bs4 import BeautifulSoup
from AT_01 import limpar_titulo


url = "https://www.imdb.com/chart/top/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

ul = soup.select_one("ul.ipc-metadata-list.sc-e22973a9-0.khSCXM")

movies = ul.select("h3.ipc-title__text") if ul else []
metadata_divs = ul.select("div.sc-2bbfc9e9-6.cZkKPy.cli-title-metadata") if ul else []
ratings = ul.select(".ipc-rating-star--rating") if ul else []

movie_data = []

for i in range(len(movies)):
    title = movies[i].text.strip()
    formated_title = limpar_titulo(title)
    
    year_span = metadata_divs[i].select("span")[0] if i < len(metadata_divs) else None
    year = int(year_span.text) if year_span and year_span.text.isdigit() else "N/A"

    rating = float(ratings[i].text) if i < len(ratings) and ratings[i].text.replace(".", "").isdigit() else "N/A"

    movie_data.append({"title": formated_title, "year": year, "rating": rating})

for movie in movie_data[:5]:
    print(f"{movie['title']} ({movie["year"]}) - Nota: {movie["rating"]}")