-- Script that prepares a MySQL server for the project:
-- creates the database hbnb_dev_db. Creates the user hbnb_dev.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
