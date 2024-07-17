-- main_0_1.sql
SOURCE setup_mysql_dev.sql;

-- Insert some initial data for testing
USE hbnb_dev_db;
INSERT INTO users (email, password, first_name, last_name) VALUES
('test1@example.com', 'password1', 'Test', 'One'),
('test2@example.com', 'password2', 'Test', 'Two');

USE hbnb_test_db;
INSERT INTO users (email, password, first_name, last_name) VALUES
('test1@example.com', 'password1', 'Test', 'One'),
('test2@example.com', 'password2', 'Test', 'Two');
