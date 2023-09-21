from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this in a real app!

# Database configuration
DATABASE = "assetmanager"
USER = "jussi"
PASSWORD = "tietokantaweb"
HOST = "localhost"

# Create a connection to the database
conn = psycopg2.connect(
    dbname=DATABASE,
    user=USER,
    password=PASSWORD,
    host=HOST
)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        
        if user:
            return redirect(url_for('second_page'))
        else:
            flash('Login failed. Check your username and password.')
    return render_template('login.html')

@app.route('/second_page')
def second_page():
    return "Welcome to the second page!"

if __name__ == "__main__":
    app.run(debug=True)
