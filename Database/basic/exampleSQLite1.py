import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur  = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks ')
cur.execute('CREATE TABLE Tracks (Title TEXT, plays INTEGER)')

conn.close()

