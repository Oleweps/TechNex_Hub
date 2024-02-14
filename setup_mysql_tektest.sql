-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS tek_test_db;
CREATE USER IF NOT EXISTS 'tek_test'@'localhost' IDENTIFIED BY 'Daniel6179@';
GRANT ALL PRIVILEGES ON `tek_test_db`.* TO 'tek_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'tek_test'@'localhost';
FLUSH PRIVILEGES;
