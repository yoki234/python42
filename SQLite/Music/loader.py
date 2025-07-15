import sqlite3 as sql

with sql.connect('SQLite/Music/music.db') as db:
    cursor = db.cursor()
    cursor.execute('''
CREATE TABLE IF NOT EXISTS music_style(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL UNIQUE                 )
                    ''')
    
    cursor.execute('''
CREATE TABLE IF NOT EXISTS artist(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL UNIQUE                 )
                    ''')
    cursor.execute('''
CREATE TABLE IF NOT EXISTS publisher(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL UNIQUE                 )
                    ''')

    cursor.execute('''
CREATE TABLE IF NOT EXISTS album(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL, 
music_style INTEGER,
date TEXT NOT NULL,  
artist INTEGER,
PUBLISHER INTEGER,
FOREIGN KEY(music_style) PEFERENCES music_style(id),
FOREIGN KEY(id_artist) PEFERENCES artist(id),    
FOREIGN KEY(id_publisher) PEFERENCES publisher(id)            )
                    ''')
    
    cursor.execute('''
CREATE TABLE IF NOT EXISTS track(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL, 
artist_style INTEGER,
id_music_album INTEGER,
music_style INTEGER,
length_trac TEXT NOT NULL,  
FOREIGN KEY(music_style) PEFERENCES music_style(id),
FOREIGN KEY(id_artist) PEFERENCES artist(id),    
FOREIGN KEY(id_publisher) PEFERENCES publisher(id)            )
                    ''')