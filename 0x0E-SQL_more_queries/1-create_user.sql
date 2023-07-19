-- Script: Create MySQL Server User
-- Description: This script creates the MySQL server user with all privileges.

-- Create user_0d_1 if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
WITH GRANT OPTION;

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
