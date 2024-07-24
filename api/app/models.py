from flask_mysqldb import MySQL

def get_all_movies(mysql: MySQL):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM my_movies")
    movies = cursor.fetchall()
    cursor.close()
    return movies

def get_movie_by_id(mysql: MySQL, movie_id: int):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM my_movies WHERE ID = %s", (movie_id,))
    movie = cursor.fetchone()
    cursor.close()
    return movie

def add_movie(mysql: MySQL, director: str, descripcion: str, fecha_de_estreno: str):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO my_movies (director, Descripcion, Fechaestreno) VALUES (%s, %s, %s)", (director, descripcion, fecha_de_estreno))
    mysql.connection.commit()
    cursor.close()

def update_movie(mysql: MySQL, movie_id: int, director: str, descripcion: str, fecha_de_estreno: str):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE my_movies SET director = %s, Descripcion = %s, Fecha_de_Estreno = %s WHERE ID = %s", (director, descripcion, fecha_de_estreno, movie_id))
    mysql.connection.commit()
    cursor.close()

def delete_movie(mysql: MySQL, movie_id: int):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM my_movies WHERE ID = %s", (movie_id,))
    mysql.connection.commit()
    cursor.close()
