-- db-init_db.sql

CREATE DATABASE IF NOT EXISTS my_database;

USE my_database;

CREATE TABLE IF NOT EXISTS my_movies (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Autor VARCHAR(100),
    Descripcion TEXT,
    Fecha_de_Estreno DATE
);
