from flask import Flask, request, jsonify
from app import app, mysql

@app.route('/movies', methods=['GET'])
def get_all_movies():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM my_movies")
    movies = cursor.fetchall()
    cursor.close()
    return jsonify(movies)

@app.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM my_movies WHERE ID = %s", (id,))
    movie = cursor.fetchone()
    cursor.close()
    if movie:
        return jsonify(movie)
    else:
        return jsonify({"error": "Movie not found"}), 404

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    pelicula = data.get("pelicula")
    director = data.get("director")
    descripcion = data.get("descripcion")
    Fechaestreno = data.get("Fechaestreno")
    
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO my_movies (pelicula, director, descripcion, Fechaestreno)
        VALUES (%s, %s, %s, %s)
    """, (pelicula, director, descripcion, Fechaestreno))
    mysql.connection.commit()
    new_id = cursor.lastrowid
    cursor.close()
    
    return jsonify({"id": new_id, "message": "Movie added successfully"}), 201

@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    data = request.get_json()
    pelicula = data.get("pelicula")
    director = data.get("director")
    descripcion = data.get("descripcion")
    Fechaestreno = data.get("Fechaestreno")
    
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE my_movies 
        SET pelicula = %s, director = %s, descripcion = %s, Fechaestreno = %s 
        WHERE ID = %s
    """, (pelicula, director, descripcion, Fechaestreno, id))
    mysql.connection.commit()
    cursor.close()
    
    return jsonify({"message": "Movie updated successfully"})

@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM my_movies WHERE ID = %s", (id,))
    mysql.connection.commit()
    cursor.close()
    
    return jsonify({"message": "Movie deleted successfully"})
