-- this script create a table users.
-- table have (id: int, email: string(255), name: string(255))

CREATE TABLE IF NOT EXISTS `users`(
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `email` VARCHAR(255) UNIQUE NOT NULL,
    `name` VARCHAR(255)
);
