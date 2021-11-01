# SONG PLAY ANALYSIS WAREHOUSE

## Propose of the project
This project has been developed to warehouse the song listening behavior of the user of music streaming application for analytics purpose.

## About datasets
The songs data & log data are in JSON format that are stored in Amazon S3

## Tech stack
- Python
- Postgres
- AWS redshift
- Notion for project management
- Github for Version control


## Usage manual
- Create dwh.cfg file to store information regarding aws
- Execute `main.py` to perform following actions in sequence
  - Drop tables if exists
  - Create tables
  - Loads data from S3 to staging tables
  - Loads data from staging tables to facts and dimension tables

## Files description
The project consists of five major files

### `constants.py`
This file consists of all constants of aws configuration

### sql_queries.py
This file consists of all sql queries

### create_tables.py
It performs operation using sql_queries
- Establish connection with database
- Drops table 
- Creates table

### etl&#46;py
This program consists of two methods for  
- Loading data from S3 to staging tables
- Inserting data to the facts and dimensional table from staging tables

### `main.py`
This program is a complete pipeline to 
- Drop the existing tables
- Create the new tables
- Load the data to staging tables
- Insert the data to facts and dimension tables
