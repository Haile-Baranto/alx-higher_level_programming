-- Script: List Cities of California (Without JOIN)
-- Description: This script lists all the cities of California without using the JOIN keyword.

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Get the state_id for California from the states table
SET @state_id := (SELECT id FROM states WHERE name = 'California');

-- List all the cities of California from the cities table
SELECT * FROM cities WHERE state_id = @state_id ORDER BY id ASC;
