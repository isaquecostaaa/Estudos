
import requests
from bs4 import BeautifulSoup
import re


def limpar_titulo(titulo):
    return re.sub(r"^\d+\.\s*", "", titulo) 

url = "https://www.imdb.com/chart/top/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

ul = soup.select_one("ul.ipc-metadata-list.sc-e22973a9-0.khSCXM")

movies = ul.select("h3.ipc-title__text") if ul else []

if __name__ == '__main__':

    print("Títulos:")
    for movie in movies[:10]:
        title = movie.get_text(strip=True)
        formated_title = limpar_titulo(title)

        print(formated_title)