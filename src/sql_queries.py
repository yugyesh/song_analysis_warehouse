# region drop table queries
drop_songplay = "DROP TABLE IF EXISTS songplays"
drop_songs = "DROP TABLE IF EXISTS songs"
drop_artists = "DROP TABLE IF EXISTS artists"
drop_users = "DROP TABLE IF EXISTS users"
drop_time = "DROP TABLE IF EXISTS time"

drop_table_queries = [drop_songplay, drop_songs, drop_artists, drop_users, drop_time]

# region create table queries
create_songplay = """
CREATE TABLE IF NOT EXISTS songplays(
    songplay_id SERIAL PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    user_id INT NOT NULL,
    song_id VARCHAR(25) NOT NULL,
    artist_id VARCHAR(25) NOT NULL,
    level VARCHAR(5) NOT NULL,
    session_id INT NOT NULL,
    location VARCHAR(100) NOT NULL,
    user_agent VARCHAR(100) NOT NULL
)
"""

create_song = """
CREATE TABLE IF NOT EXISTS songs(
    song_id VARCHAR(25) PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    artist_id VARCHAR(25) NOT NULL,
    year INT NOT NULL,
    duration FLOAT NOT NULL
)
"""

create_artist = """
CREATE TABLE IF NOT EXISTS artists(
    artist_id VARCHAR(25) PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    location VARCHAR(100) NOT NULL,
    latitude FLOAT,
    longitude FLOAT
)
"""

create_user = """
CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
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
    weekday VARCHAR(10) NOT NULL
)
"""

create_table_queries = [
    create_songplay,
    create_song,
    create_artist,
    create_user,
    create_time,
]
# endregion
