from app import app, connect_to_db
from flask import render_template, request
from flask import flash, session, redirect, url_for

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

@app.route('/select', methods=['GET'])
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

    print(data)


    return render_template('results.html', Data=data, Mood=mood)

@app.route('/add-song', methods=['GET','POST'])
def add_song():
    if 'username' not in session:
        flash('You need to be logged in to add a song!')
        return redirect(url_for('login'))
    
    if session['username'] != 'admin':
        flash('You need to be admin to add song')
        return redirect(url_for('index'))
    
    if request.method == "POST":
        artist = request.form.get('artist')
        title = request.form.get('title')
        mood = request.form.get('mood')


        conn = connect_to_db()
        cursor = conn.cursor()

        try:
            query = "INSERT INTO songs (artist, title, mood) VALUES (%s, %s, %s)"
            cursor.execute(query, (artist, title, mood))
            conn.commit()
            flash('Your Song has been added successfully!')

            cursor.close()
            conn.close()

        except Exception as e:
            conn.rollback()
            flash('Failed to add song ;) Try again later')

    return render_template('add_song_normal.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = connect_to_db()
        cursor = conn.cursor()
        
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        conn.commit()
        
        flash('Registration successful! Please log in.')
        cursor.close()
        conn.close()
        
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = connect_to_db()
        cursor = conn.cursor()
        
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        
        if user:
            session['username'] = username
            flash('Login successful!')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.')
        
        cursor.close()
        conn.close()
        
    return render_template('login.html')

@app.route('/delete-song/<int:song_id>', methods=['POST'])
def delete_song(song_id):
    if 'username' not in session:
        flash('You need to be logged in!')
        return redirect(url_for('login'))
    
    if session['username'] != 'admin':
        flash('You need to be admin to remove song!')
        return redirect(url_for('index'))
    
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM songs WHERE id = %s", (song_id,))
        conn.commit()
        flash('song has been deleted')
    except:
        conn.rollback()
        flash('failed to delete song')
    
    cursor.close()
    conn.close()

    return redirect('/')

@app.route('/update-song/<int:song_id>', methods=['GET', 'POST'])
def update_song(song_id):
    if 'username' not in session:
        flash('You need to be logged in!')
        return redirect(url_for('login'))

    if session['username'] != 'admin':
        flash('You need to be admin to update songs!')
        #return redirect(url_for('index'))

    conn = connect_to_db()
    cursor = conn.cursor()

    if request.method == "POST":
        new_artist = request.form.get('artist')
        new_title = request.form.get('title')
        new_mood = request.form.get('mood')

        try:
            query = "UPDATE songs SET artist=%s, title=%s, mood=%s WHERE id=%s"
            cursor.execute(query, (new_artist, new_title, new_mood, song_id))

            conn.commit()
            flash('Song has been updated successfully!')
        except:
            conn.rollback() 
            flash('Failed to update the song.')
        
        cursor.close()
        conn.close()

        return redirect('/')

    else:
        query = "SELECT * FROM songs WHERE id = %s"
        cursor.execute(query, (song_id,))
        song = cursor.fetchone()

        cursor.close()
        conn.close()

        if song:
            return render_template('update_song.html', song=song)
        else:
            flash('Song not found!')
            return redirect('/')


@app.route('/search/', methods=['GET'])
def search():
    search_term = request.args.get('search_term', '').lower()
    search_field = request.args.get('search_field', 'mood')

    conn = connect_to_db()
    cursor = conn.cursor()

    # Prepare the query based on the selected field
    query = f"SELECT * FROM songs WHERE LOWER({search_field}) LIKE %s"
    search_pattern = f"%{search_term}%"

    cursor.execute(query, (search_pattern,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('results.html', Data=results, SearchTerm=search_term, SearchField=search_field)
