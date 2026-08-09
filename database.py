import sqlite3
def get_connection():
    return sqlite3.connect("college.db")
from models import Student
def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        roll INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        department TEXT,
        email TEXT,
        phone TEXT
    )
    """)

    connection.commit()
    connection.close()
def insert_student(roll, name, age, department, email, phone):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO students
            (roll, name, age, department, email, phone)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (roll, name, age, department, email, phone))

        connection.commit()
        return True

    except sqlite3.IntegrityError:
        connection.rollback()
        return False

    finally:
        connection.close()
def get_all_students():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    connection.close()

    students = []

    for row in data:
        student = Student(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5]
        )
        students.append(student)

    return students
    

def search_student_by_roll(roll):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE roll=?",
        (roll,)
    )

    data = cursor.fetchone()

    connection.close()

    if data:
        return Student(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4],
            data[5]
        )

    return None

def update_student_data(roll, field, value):
    allowed_fields = {
        "name",
        "age",
        "department",
        "email",
        "phone"
    }

    if field not in allowed_fields:
        return False

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        f"UPDATE students SET {field}=? WHERE roll=?",
        (value, roll)
    )

    updated = cursor.rowcount

    connection.commit()
    connection.close()

    return updated > 0

def delete_student_by_roll(roll):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM students WHERE roll=?",
        (roll,)
    )
    deleted = cursor.rowcount
    connection.commit()
    connection.close()
    return deleted > 0

