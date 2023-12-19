-- This script prepares a MySQL server for the project development environment.
-- It creates a project development database named: hbnb_dev_db if doesn't already exist.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- It creates a new user named: hbnb_dev with all privileges on the database hbnb_dev_db.
-- The password 'hbnb_dev_pwd' is set if the user doesn't already exist.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- It grants all privileges to the new user on the hbnb_dev_db.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- It grants the SELECT privilege for the user hbnb_dev on the performance_schema database.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
