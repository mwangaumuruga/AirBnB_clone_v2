-- Creates the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creates the user if it does not exist and sets the password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grants all privileges on the hbnb_dev_db database to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grants SELECT privilege on the performance_schema database to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to ensure that all changes take effect immediately
FLUSH PRIVILEGES;
