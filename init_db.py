import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create the projects table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL
    )
''')

# Insert your existing projects
projects = [
    ("Student Management System", "A web application for managing student records, attendance, fees, results, and academic information. It simplifies administrative tasks and provides an organized way to store and access student data."),
    ("Class Management System", "A complete management system that helps educational institutes organize students, teachers, subjects, attendance, exams, fee structures, holidays, and departmental information through a single, user-friendly platform."),
    ("Calculator", "A simple calculator application built using Python that performs basic arithmetic operations through a clean and easy-to-use interface.")
]

cursor.executemany("INSERT INTO projects (title, description) VALUES (?, ?)", projects)

conn.commit()
conn.close()

print("Database created and projects added successfully!")