from app.models import get_all_movies, get_movie_by_id, add_movie, update_movie, delete_movie

def get_movies(mysql):
    return get_all_movies(mysql)

def get_movie(mysql, movie_id):
    return get_movie_by_id(mysql, movie_id)

def create_movie(mysql, autor, descripcion, fecha_de_estreno):
    add_movie(mysql, autor, descripcion, fecha_de_estreno)

def update_movie_info(mysql, movie_id, autor, descripcion, fecha_de_estreno):
    update_movie(mysql, movie_id, autor, descripcion, fecha_de_estreno)

def delete_movie_info(mysql, movie_id):
    delete_movie(mysql, movie_id)
