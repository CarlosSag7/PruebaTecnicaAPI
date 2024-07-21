# main.py

from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object('config.Config')

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT 1 ''')
    results = cursor.fetchone()
    return f"Database connection successful: {results}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
