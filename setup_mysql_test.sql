-- This script prepares a MySQL server for the project testing environment.
-- It creates a project testing database named: hbnb_test_db if it doesn't already exist.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- It creates a new user named: hbnb_test with all privileges on the database hbnb_test_db.
-- The password 'hbnb_test_pwd' is set if the user doesn't already exist.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- It grants the SELECT privilege for the user hbnb_test on the performance_schema database.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

-- It grants all privileges to the new user on the hbnb_test_db.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
