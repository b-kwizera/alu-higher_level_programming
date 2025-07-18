0-privileges.sql: lists all privileges for user_0d_1 and user_0d_2 on localhost.
1-create_user.sql: creates user_0d_1 with full privileges if not already present.
3-force_name.sql: creates table force_name with NOT NULL name column, if it doesn't already exist.
4-never_empty.sql: creates id_not_null table with default value 1 for id.
5-unique_id.sql: creates unique_id table with id as unique and default value of 1.
6-states.sql: creates database hbtn_0d_usa and states table with auto-increment id and NOT NULL name
7-cities.sql: creates cities table in hbtn_0d_usa with foreign key to states.id
8-cities_of_california_subquery.sql: lists cities of California using a subquery (no JOIN)
9-cities_by_state_join.sql: lists all cities and their state names using JOIN, sorted by city id
10-genre_id_by_show.sql: lists tv shows with at least one genre linked, sorted by title and genre_id
11-genre_id_all_shows.sql: lists all tv shows with genre IDs, including NULL for shows without genres
12-no_genre.sql: lists tv shows without any genre linked, sorted by title
13-count_shows_by_genre.sql: lists genres and number of linked shows, sorted descending
14-my_genres.sql: lists all genres of the show 'Dexter' sorted alphabetically
15-comedy_only.sql: lists all shows with the genre Comedy sorted by title
