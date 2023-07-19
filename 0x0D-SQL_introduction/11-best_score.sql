-- Description: This script lists all records with a score greater than or equal to
-- 10 from the table second_table in the hbtn_0c_0 database, 
-- ordered by score (top first).

-- List records with score >= 10 ordered by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
