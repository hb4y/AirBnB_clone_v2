-- Script that prepares a MySQL server for the project:
--   creates the database hbnb_test_db.
--   creates the user hbnb_test.
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
DROP USER IF EXISTS 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant select
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
