from app import app, connect_to_db
from flask import render_template, request

def get_default_moods():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT mood FROM songs")
    moods = cursor.fetchall()
    cursor.close()
    conn.close()
    mood_list = []
    for mood in moods:
        mood_list.append(mood[0])
    print(mood_list) 
    return mood_list


@app.route('/')
def index():
    moods = get_default_moods()
    return render_template('index.html', Moods=moods)

@app.route('/search', methods=['GET'])
def get_mood():
    mood = request.args.get('mood')
    
    # print(f"Received mood: {mood}")  # Debugging line

    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM songs WHERE mood = '%s'" % mood

    cursor.execute(query)
    
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    print(data)  # Add this line to debug


    return render_template('results.html', data=data, Mood=mood)

@app.route('/insert', methods=['POST'])