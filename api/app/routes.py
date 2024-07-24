from flask import Flask, request, jsonify
from app import app, mysql
from controllers.movies_controller import get_movies, get_movie, create_movie, update_movie_info, delete_movie_info


@app.route('/')
def index():
    return "Welcome to the Flask API!"

@app.route('/movies', methods=['GET'])
def get_all_movies():
    movies = get_movies(mysql)
    return jsonify(movies)

@app.route('/movies/<int:id>', methods=['GET'])
def get_single_movie(id):
    movie = get_movie(mysql, id)
    return jsonify(movie)

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.json
    create_movie(mysql, data['pelicula'], data['director'], data['descripcion'], data['Fechaestreno'])
    return jsonify({'message': 'Movie added successfully'}), 201

@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    data = request.json
    update_movie_info(mysql, id, data['pelicula'], data['director'], data['descripcion'], data['Fechaestreno'])
    return jsonify({'message': 'Movie updated successfully'})

@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    delete_movie_info(mysql, id)
    return jsonify({'message': 'Movie deleted successfully'})
