-- Script: Create force_name Table
-- Description: This script creates the force_name table with the specified columns.

-- Create the table force_name if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
  id INT,
  name VARCHAR(256) NOT NULL
);
