import sqlite3

conn = sqlite3.connect('esports_players.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE esports_player
          (id INTEGER PRIMARY KEY ASC, 
           first_name VARCHAR(30) NOT NULL,
           last_name VARCHAR(30) NOT NULL,
           player_name VARCHAR(30) NOT NULL,
           age INTEGER NOT NULL,
           num_towers INTEGER NOT NULL,
           objectives INTEGER NOT NULL,
           denies INTEGER NOT NULL,
           kills INTEGER NOT NULL,
           deaths INTEGER NOT NULL,
           type VARCHAR(20) NOT NULL
           )
          ''')

conn.commit()
conn.close()
