0-list_databases.sql: Script that lists all databases of your MySQL server.
1-create_database_if_missing.sql: Creates the database hbtn_0c_0 if it doesn't exist.
2-remove_database.sql: Deletes the database hbtn_0c_0 if it exists.
3-list_tables.sql: Lists all tables of the specified database.
4-first_table.sql: Creates first_table with columns id (INT) and name (VARCHAR(256)) if not exists.
5-full_table.sql: Prints full CREATE TABLE statement of first_table using SHOW CREATE TABLE.
6-list_values.sql: Lists all rows of the first_table from the hbtn_0c_0 database.
7-insert_value.sql: Inserts a new row with id=89 and name='Best School' into first_table.
8-count_89.sql: Counts records with id=89 in first_table.
9-full_creation.sql: creates second_table and inserts multiple rows.
10-top_score.sql: lists all records of second_table ordered by score descending showing score and name.
11-best_score.sql: lists all records of second_table with score >= 10 ordered by score descending showing score and name.
12-no_cheating.sql: updates the score of Bob to 10 in second_table using only the name field.
13-change_class.sql: removes all records with score less than or equal to 5 in second_table.
14-average.sql: computes the average score of all records in second_table.
15-groups.sql: lists count of records grouped by score in second_table sorted by number descending.
16-no_link.sql: lists records in second_table with non-null/non-empty name ordered by descending score.
