class TV:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"

class Movies(TV):
    def __init__(self, title, year, rating):
        super().__init__(title, year)
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year}) - Nota: {self.rating}"

class Series(TV):
    def __init__(self, title, year, seasons, episodes, rating):
        super().__init__(title, year)
        self.seasons = seasons
        self.episodes = episodes
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.seasons} temporada(s) |{self.episodes} episódio(s) - Nota: {self.rating}"