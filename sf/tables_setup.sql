USE ROLE ACCOUNTADMIN;

CREATE OR REPLACE WAREHOUSE MOVIE_L;
CREATE OR REPLACE DATABASE MOVIE_DB;
CREATE OR REPLACE SCHEMA MOVIE_SCHEMA;

-- create file format
CREATE or REPLACE file format csvformat
  skip_header = 0
  type = 'CSV'
  FIELD_DELIMITER = '\t';

  -- create stage
CREATE or REPLACE stage ratings_data_stage
  file_format = csvformat;


-- create a table where we upload data
CREATE or REPLACE TABLE MOVIE_DB.MOVIE_SCHEMA.ratings (
-- user id | item id | rating | timestamp
    user_id NUMBER(38,0),
    item_id NUMBER(38,0),
    rating FLOAT,
    timestamp number(38,0)
);

-- !!!use SNOWSQL in the terminal to upload data!!!
-- put file:///Users/nadina/Documents/ml-100k/ratings.csv @ratings_data_stage;
-- nadina#COMPUTE_WH@MOVIE_DB.MOVIE_SCHEMA>put file:///Users/nadina/Documents/ml-100k/ratings.csv @ratings_data_stage;
-- +-------------+----------------+-------------+-------------+--------------------+--------------------+----------+---------+
-- | source      | target         | source_size | target_size | source_compression | target_compression | status   | message |
-- |-------------+----------------+-------------+-------------+--------------------+--------------------+----------+---------|
-- | ratings.csv | ratings.csv.gz |     1979173 |      828256 | NONE               | GZIP               | UPLOADED |         |
-- +-------------+----------------+-------------+-------------+--------------------+--------------------+----------+---------+

-- copy from the stage into the table
COPY into ratings
  from @ratings_data_stage;

-- Check if it worked
select *
from ratings;
-- success!!!

-- will need later foreign keys (user_id and item_id)


-- CREATE A TABLE items (contains movies info)
-- STEPS:
-- 1. File format
-- 2. Stage
-- 3. Table
-- 4. snowsql put file into the stage
-- 5. COPY from the stage into the table

CREATE OR REPLACE file format   csvpipe -- CREATE file format IF NOT EXISTS  csvpipe 
  skip_header = 0
  type = 'CSV'
  FIELD_DELIMITER = '|';
  -- ENCODING = UTF8
  -- REPLACE_INVALID_CHARACTERS = TRUE;

CREATE OR REPLACE stage items_data_stage
    file_format = csvpipe;

CREATE OR REPLACE table MOVIE_DB.MOVIE_SCHEMA.items (
-- movie id | movie title | release date | video release date |
-- IMDb URL | unknown | Action | Adventure | Animation |
-- Children's | Comedy | Crime | Documentary | Drama | Fantasy |
-- Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
-- Thriller | War | Western |
item_id NUMBER(38, 0),
title VARCHAR(255),
release_date DATE,
video_release_date DATE,
imdb_url VARCHAR,
unknown_genre BOOLEAN,
action BOOLEAN,
adventure BOOLEAN,
animation BOOLEAN,
children BOOLEAN,
comedy BOOLEAN,
crime BOOLEAN,
documentary BOOLEAN,
drama BOOLEAN,
fantasy BOOLEAN,
film_noir BOOLEAN,
horror BOOLEAN,
musical BOOLEAN,
mystery BOOLEAN,
romance BOOLEAN,
sci_fi BOOLEAN,
thriller BOOLEAN,
war BOOLEAN,
western BOOLEAN,
PRIMARY KEY(item_id));

-- put file:///Users/nadina/Documents/ml-100k/items.csv @items_data_stage;

COPY INTO items
FROM @items_data_stage; -- ON_ERROR = CONTINUE;

-- check if correct
select * from items;
-- after 2 hrs of cleaning f..ng broken csv finally it loaded. aaaaaaaa!!!

-- count null values in the column video_release_date

SELECT SUM(CASE WHEN video_release_date is NULL THEN 1 ELSE 0 END) AS null_values, count(*) as all_values
FROM MOVIE_DB.MOVIE_SCHEMA.items;
-- returns 1682 and 1682

-- drop the column video_release_date
ALTER TABLE items
DROP COLUMN video_release_date;

SELECT * FROM items;

-- LOAD USERS, use the csvpipe file format
CREATE OR REPLACE table MOVIE_DB.MOVIE_SCHEMA.users (
-- user id | age | gender | occupation | zip code
user_id NUMBER(38,0),
age NUMBER(3,0),
gender VARCHAR(255),
occupation VARCHAR(255),
zip VARCHAR(255),
PRIMARY KEY (user_id)
);


CREATE OR REPLACE stage users_data_stage
    file_format = csvpipe;

COPY INTO users FROM @users_data_stage;

SELECT * FROM users;

ALTER TABLE ratings
ADD CONSTRAINT user_id FOREIGN KEY(user_id) REFERENCES users(user_id);


ALTER TABLE ratings
ADD CONSTRAINT item_id FOREIGN KEY(item_id) REFERENCES items(item_id);
