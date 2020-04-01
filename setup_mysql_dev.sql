-- Script that prepares a MySQL server for the project:
--   creates the database hbnb_dev_db.
--   creates the user hbnb_dev.
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
DROP USER IF EXISTS 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant select
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
