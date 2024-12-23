
# Simple Secure Web Application with Flask
from flask import Flask, request, render_template, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "supersecretkey"

# Database initialization
def init_db():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        content TEXT NOT NULL,
                        user_id INTEGER,
                        FOREIGN KEY (user_id) REFERENCES users (id)
                    )''')
    conn.commit()
    conn.close()

# Secure headers
@app.after_request
def apply_secure_headers(response):
    response.headers["Content-Security-Policy"] = "default-src 'self';"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response

# Routes
@app.route('/')
def index():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT posts.title, posts.content, users.username FROM posts JOIN users ON posts.user_id = users.id")
    posts = cursor.fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            flash('Username already exists!')
            return redirect(url_for('register'))
        conn.close()
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('Login successful!')
            return redirect(url_for('index'))
        flash('Invalid credentials!')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!')
    return redirect(url_for('index'))

@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'user_id' not in session:
        flash('You must be logged in to create a post!')
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)", (title, content, session['user_id']))
        conn.commit()
        conn.close()
        flash('Post created successfully!')
        return redirect(url_for('index'))
    return render_template('create.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
