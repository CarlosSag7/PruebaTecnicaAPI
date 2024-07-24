def get_movies(mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM my_movies")
    results = cursor.fetchall()
    movies = []
    for row in results:
        movie = {
            "ID": row[0],
            "pelicula": row[1],
            "director": row[2],
            "descripcion": row[3],
            "Fechaestreno": row[4]
        }
        movies.append(movie)
    return movies

def get_movie(mysql, id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM my_movies WHERE ID = %s", (id,))
    row = cursor.fetchone()
    if row:
        movie = {
            "ID": row[0],
            "pelicula": row[1],
            "director": row[2],
            "descripcion": row[3],
            "Fechaestreno": row[4]
        }
        return movie
    return None

def create_movie(mysql, pelicula, director, descripcion, fecha_de_estreno):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO my_movies (pelicula, director, descripcion, Fechaestreno) VALUES (%s, %s, %s, %s)", 
                   (pelicula, director, descripcion, fecha_de_estreno))
    mysql.connection.commit()

def update_movie_info(mysql, id, pelicula, director, descripcion, fecha_de_estreno):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE my_movies SET pelicula = %s, director = %s, descripcion = %s, Fechaestreno = %s WHERE ID = %s", 
                   (pelicula, director, descripcion, fecha_de_estreno, id))
    mysql.connection.commit()

def delete_movie_info(mysql, id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM my_movies WHERE ID = %s", (id,))
    mysql.connection.commit()
