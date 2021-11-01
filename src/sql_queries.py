from src.constants import DWH_ROLE_ARN

# region drop table queries
drop_staging_songs = "DROP TABLE IF EXISTS staging_songs"
drop_staging_events = "DROP TABLE IF EXISTS staging_events"

drop_songplay = "DROP TABLE IF EXISTS songplays"
drop_songs = "DROP TABLE IF EXISTS songs"
drop_artists = "DROP TABLE IF EXISTS artists"
drop_users = "DROP TABLE IF EXISTS users"
drop_time = "DROP TABLE IF EXISTS time"

drop_table_queries = [
    drop_songplay,
    drop_songs,
    drop_artists,
    drop_users,
    drop_time,
    drop_staging_songs,
    drop_staging_events,
]

# region create table queries
create_staging_songs = """
CREATE TABLE IF NOT EXISTS staging_songs(
    num_songs INT PRIMARY KEY,
    artist_id VARCHAR,
    artist_latitude FLOAT,
    artist_longitude FLOAT,
    artist_location VARCHAR,
    artist_name VARCHAR,
    song_id VARCHAR,
    title VARCHAR,
    duration FLOAT,
    year INT
)
"""
create_staging_events = """
CREATE TABLE IF NOT EXISTS staging_events(
    artist VARCHAR,
    auth VARCHAR,
    first_name VARCHAR,
    gender CHAR(1),
    item_in_session INT,
    last_name VARCHAR,
    length FLOAT,
    level VARCHAR(5),
    location VARCHAR,
    method VARCHAR(5),
    page VARCHAR(20),
    registration varchar(50),
    session_id int,
    song VARCHAR,
    status INT,
    ts BIGINT,
    user_agent VARCHAR,
    user_id INT
)
"""

create_songplay = """
CREATE TABLE IF NOT EXISTS songplays(
    songplay_id INT IDENTITY(0, 1) PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    user_id INT NOT NULL,
    song_id VARCHAR NOT NULL,
    artist_id VARCHAR NOT NULL,
    level VARCHAR(5) NOT NULL,
    session_id INT NOT NULL,
    location VARCHAR NOT NULL,
    user_agent VARCHAR NOT NULL
)
"""

create_song = """
CREATE TABLE IF NOT EXISTS songs(
    song_id VARCHAR(25) PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    artist_id VARCHAR(25) NOT NULL,
    year INT NOT NULL,
    duration FLOAT NOT NULL
)
"""

create_artist = """
CREATE TABLE IF NOT EXISTS artists(
    artist_id VARCHAR(25) PRIMARY KEY,
    name VARCHAR NOT NULL,
    location VARCHAR NOT NULL,
    latitude FLOAT,
    longitude FLOAT
)
"""

create_user = """
CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender CHAR(1) NOT NULL,
    level VARCHAR(5) NOT NULL
)
"""

create_time = """
CREATE TABLE IF NOT EXISTS time(
    start_time TIMESTAMP PRIMARY KEY,
    hour INT NOT NULL,
    day INT NOT NULL,
    week INT NOT NULL,
    month INT NOT NULL,
    year INT NOT NULL,
    weekday INT NOT NULL
)
"""

create_table_queries = [
    create_songplay,
    create_song,
    create_artist,
    create_user,
    create_time,
    create_staging_songs,
    create_staging_events,
]
# endregion

# copy data from s3 to staging area
copy_staging_songs = """
copy staging_songs from 's3://udacity-dend/song_data/A/A'
iam_role '{}'
format as json 'auto'
region 'us-west-2';
""".format(
    DWH_ROLE_ARN
)

copy_staging_events = """
copy staging_events from 's3://udacity-dend/log_data'
iam_role '{}'
format as json 's3://udacity-dend/log_json_path.json'
region 'us-west-2';
""".format(
    DWH_ROLE_ARN
)

copy_queries = [copy_staging_songs, copy_staging_events]

# TODO: Add insert table query for fact and dimension table

# fact table
insert_into_songplay = """
INSERT INTO songplays(
start_time, user_id, song_id, artist_id, level, session_id, location, user_agent
)
SELECT DISTINCT
to_timestamp(se.ts::text, 'YYYYMMDDHH24MISS') as start_time, se.user_id, ss.song_id, ss.artist_id, se.level, se.session_id, se.location, se.user_agent
FROM staging_events se
JOIN staging_songs ss
on
se.song = ss.title
"""

insert_into_song = """
INSERT INTO songs(
song_id, title, artist_id, year, duration
)
SELECT DISTINCT
song_id, title, artist_id, year, duration
FROM staging_songs
WHERE
song_id IS NOT NULL
AND 
song_id NOT IN (SELECT DISTINCT song_id FROM songs)
"""

insert_into_artist = """
INSERT INTO artists(
artist_id, name, location, latitude, longitude
)
SELECT DISTINCT
artist_id, artist_name as name, artist_location, artist_latitude, artist_longitude
FROM staging_songs
WHERE
artist_id IS NOT NULL
AND
artist_id NOT IN (SELECT DISTINCT artist_id FROM artists)
"""

insert_into_user = """
INSERT INTO users (
user_id, first_name, last_name, gender, level
)
SELECT DISTINCT
user_id, first_name, last_name, gender, level
FROM staging_events
WHERE 
user_id IS NOT NULL
AND
user_id NOT IN (SELECT DISTINCT user_id FROM users)
"""
insert_into_time = """
INSERT INTO time(
start_time, hour, day, week, month, year, weekday 
)
SELECT DISTINCT
to_timestamp(ts::text, 'YYYYMMDDHH24MISS') as start_time,
EXTRACT(hour FROM start_time) as hour, 
EXTRACT(day FROM start_time) as day, 
EXTRACT(week FROM start_time) as week, 
EXTRACT(month FROM start_time) as month, 
EXTRACT(year FROM start_time) as year, 
EXTRACT(DOW FROM start_time) as weekday 
FROM staging_events
WHERE start_time IS NOT NULL
"""

insert_queries = [
    insert_into_songplay,
    insert_into_song,
    insert_into_artist,
    insert_into_user,
    insert_into_time,
]
