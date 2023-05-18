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

CREATE IF NOT EXISTS file format csvpipe
  skip_header = 0
  type = 'CSV'
  FIELD_DELIMITER = '|';

CREATE OR REPLACE stage items_data_stage
    file_format = csvpipe;

CREATE OR REPLACE table MOVIE_DB.MOVIE_SCHEMA.items
-- movie id | movie title | release date | video release date |
-- IMDb URL | unknown | Action | Adventure | Animation |
-- Children's | Comedy | Crime | Documentary | Drama | Fantasy |
-- Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
-- Thriller | War | Western |
item_id NUMBER(38, 0),
title 
