-- Script: Create id_not_null Table
-- Description: This script creates the id_not_null table with the specified columns.

-- Create the table id_not_null if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT DEFAULT 1,
  name VARCHAR(256)
);
