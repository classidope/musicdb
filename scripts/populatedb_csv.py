import csv
import mysql.connector
from mysql.connector import Error

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Tr3@$ury',
    database='musicdb'
)

cursor = db.cursor()

with open(r"C:\Users\class1d\Documents\dev\moodBasedMusic\scripts\songList.csv") as f:
    reader = csv.reader(f)

    for i in reader:
        artist = i[0].strip()
        mood = i[2].strip()
        title = i[1].strip()
        
        try:
            cursor.execute('INSERT INTO songs(artist, mood, title) VALUES (%s, %s, %s)', (artist, mood, title))
            #cursor.execute('INSERT INTO songs(artist, mood, title) VALUES (%s, %s, %s)', (i[0], i[1], i[2]))
        except Error as e:
            if e.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
                print(f'Skipping duplicate entry: {artist}, {title}, {mood}')
            else:
                print(f'Error: {e}')
                raise

db.commit()
cursor.close()
db.close()
