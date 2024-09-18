import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Tr3@$ury',
    database = 'musicdb'
)

cursor = db.cursor()

query = 'INSERT INTO songs(artist, mood, title) values(%s, %s, %s)'
values = [
    ('Xasthur', 'depressed', 'Telepathic with the Deceased'),
    ('Xasthur', 'depressed', 'Screaming at Forgotten Tears'),
]

cursor.executemany(query, values)
db.commit()
cursor.close()
db.close()