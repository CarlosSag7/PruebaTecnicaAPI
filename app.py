from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

books = [
    {"id":1 , "title" : "Libro de la selva", "author": "Ricardo"},
    {"id":2 , "title" : "Libro de la costa", "author": "Juan"},
    {"id":3 , "title" : "Libro de la sierra", "author": "Rodrigo"}
]


@app.route('/saludo',methods=['GET'])
def hello_world():
    return "Hola a todos"

@app.route('/despedida',methods=['GET'])
def adios():
    return "Adios a todos"

@app.route('/pokemon/<id>', methods=['GET'])
def sacar_pokemon(id):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")

    if response.status_code == 200:
        pokemon_data = response.json()
        print(type(pokemon_data))
        return jsonify(pokemon_data)
    else:
        return jsonify({'Error':'Pokemon no encontrado'})
    
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books',methods=['POST'])
def post_books():
    response = request.get_json()

    new_book = {
        "id": len(books)+1,
        "title": response.get('title'),
        "author": response.get("author")
    }

    books.append(new_book)

    return "Generado correctamente"