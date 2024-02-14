-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS tek_dev_db;
CREATE USER IF NOT EXISTS 'tek_dev'@'localhost' IDENTIFIED BY 'Daniel6179@';
GRANT ALL PRIVILEGES ON `tek_dev_db`.* TO 'tek_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'tek_dev'@'localhost';
FLUSH PRIVILEGES;
