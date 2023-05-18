USE ROLE ACCOUNTADMIN;

CREATE OR REPLACE WAREHOUSE MOVIE_L;
CREATE OR REPLACE DATABASE MOVIE_DB;
CREATE OR REPLACE SCHEMA MOVIE_SCHEMA;

-- create file format
CREATE or REPLACE file format csvformat
  skip_header = 0
  type = 'CSV';

  -- create stage
-- CREATE or REPLACE stage ratings_data_stage
--   file_format = csvformat
--   url = '/Users/nadina/Documents/ml-100k/ratings.csv';


-- create a table where we upload data
CREATE or REPLACE TABLE MOVIE_DB.MOVIE_SCHEMA.ratings (
-- user id | item id | rating | timestamp
    user_id NUMBER(38,0),
    item_id NUMBER(38,0),
    rating FLOAT,
    timestamp DATE
);
STAGE_FILE_FORMAT = ( TYPE = 'csv' FIELD_DELIMITER= '\t' );

put file://'/Users/nadina/Documents/ml-100k/ratings.csv' ratings

-- copy from file into the table
COPY into ratings
  from @ratings_data_stage;

