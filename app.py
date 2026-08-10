from flask import Flask, render_template 
import sqlite3 

app = Flask(__name__)

@app.route('/')
def home():
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT title, description FROM projects")
        projects = cursor.fetchall()
        conn.close()

        return render_template('index.html', projects = projects)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 500))
    app.run(host = '0.0.0.0', port = port)
