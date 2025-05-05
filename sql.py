import sqlite3

connection = sqlite3.connect('students.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INT(2),
    name VARCHAR(10),
    surname VARCHAR(10),
    sex VARCHAR (1),
    age INT,
    mail VARCHAR(30),
    grade INT,
    phone_number VARCHAR(10)

)
""")
connection.commit()
connection.close()

connection = sqlite3.connect('students.db')
cursor = connection.cursor()

cursor.execute("""INSERT INTO students (id, name, surname, sex, age, mail, grade, phone_number   )
VALUES
    (1, "John", "Smith", "M", 19, "john@mail.com", 2, "+79854562535" ),
    (2, "Emily", "Johnson", "F", 20, "emily@mail.com", 3, "+79123456789"),
    (3, "Michael", "Williams", "M", 21, "michael@mail.com", 1, "+79098765432"),
    (4, "Sophia", "Brown", "F", 18, "sophia@mail.com", 2, "+79234567890"),
    (5, "James", "Davis", "M", 22, "james@mail.com", 4, "+79345678901"),
    (6,"Olivia", "Miller", "F", 19, "olivia@mail.com", 1, "+79456789012"),
    (7,"Robert", "Wilson", "M", 20, "robert@mail.com", 3, "+79567890123"),
    (8,"Ava", "Taylor", "F", 21, "ava@mail.com", 2, "+79678901234")

""")
student = cursor.fetchall()
connection.commit()
connection.close()


def get_students():
    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students')
    student = cursor.fetchall()

    if student:
        return f' {student}'
    else:
        return "no data"

    connection.commit()
    connection.close()


def delete_student_sql(student_id):
    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    connection.commit()
    return True




