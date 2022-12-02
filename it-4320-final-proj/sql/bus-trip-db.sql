-- MySQL database for user login credentials
CREATE DATABASE `bus-trip-db`;
USE `bus-trip-db`;

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users`
    (
        `username` VARCHAR(25) NOT NULL PRIMARY KEY,
        `password` VARCHAR(100)
    );

-- Insert admin users into database using information in passcodes.txt file
INSERT INTO `users` VALUES ("admin1", sha1("12345"));
INSERT INTO `users` VALUES ("admin2", sha1("24680"));
INSERT INTO `users` VALUES ("admin3", sha1("98765"));