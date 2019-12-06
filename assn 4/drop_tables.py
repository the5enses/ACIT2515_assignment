import sqlite3

conn = sqlite3.connect('esports_players.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE esports_player
          ''')

conn.commit()
conn.close()
