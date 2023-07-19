-- Script: Create unique_id Table
-- Description: This script creates the unique_id table with the specified columns.

-- Create the table unique_id if it doesn't exist
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1 UNIQUE,
  name VARCHAR(256)
);
