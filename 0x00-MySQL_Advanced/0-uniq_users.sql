-- creates users table in database
-- creates database if it does not exist
CREATE DATABASE IF NOT EXISTS holberton;
CREATE TABLE IF NOT EXISTS holberton.users (
	id INT AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255) NOT NULL
);

