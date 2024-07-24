# config.py

class Config:
    MYSQL_HOST = 'mysql_container'  # O usa el nombre del servicio si usas docker-compose, por ejemplo, 'mysql'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'my-secret-pw'
    MYSQL_DB = 'my_database'
