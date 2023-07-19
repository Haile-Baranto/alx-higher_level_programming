-- Full Creation of second_table
-- This script creates a table called second_table in the hbtn_0c_0 database and inserts multiple rows.

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS second_table (
  id INT,
  name VARCHAR(256),
  score INT
);

-- Insert the rows
INSERT INTO second_table (id, name, score)
VALUES (1, 'John', 10),
       (2, 'Alex', 3),
       (3, 'Bob', 14),
       (4, 'George', 8);
