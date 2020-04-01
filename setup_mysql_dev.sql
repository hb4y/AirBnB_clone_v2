-- Script that prepares a MySQL server for the project:
--   creates the database hbnb_dev_db.
--   creates the user hbnb_dev.
-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_dev_db;
-- Create user
CREATE USER IF NOT EXISTS 'user_dev'@'localhost' IDENTIFIED BY 'user_dev_pwd';
-- Grant all
GRANT ALL ON hbnb_dev_db.* TO 'user_dev'@'localhost';
-- Grant select
GRANT SELECT ON performance_schema.* TO 'user_dev'@'localhost';
