-- List all records of the table second_table of the database hbtn_0c_0 in your MySQL server
-- The database name will be passed as an argument to the mysql command
SELECT score, name FROM second_table WHERE name != "" ORDER by score DESC;
