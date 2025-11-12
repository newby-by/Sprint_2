"""The second task.

Create two child classes by the parent class.
"""

class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        return str(self.movies)


class Comedy(Movies):
    def add_movie(self, movie):
        return 'Комедии:' + super().add_movie(movie)


class Drama(Movies):
    def add_movie(self, movie):
        return 'Драмы:' + super().add_movie(movie)


print(Comedy().add_movie('Большой куш'))
print(Drama().add_movie('Оружейный барон'))
