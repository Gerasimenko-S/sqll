import sqlite3

connection = sqlite3.connect('students.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INT(2),
    name VARCHAR(10),
    surname VARCHAR(15),
    gend VARCHAR (1),
    age INT,
    mail VARCHAR(30),
    grade INT,
    phone_number VARCHAR(10),
    grupa VARCHAR(3),
    form VARCHAR(3)

)
""")
connection.commit()
connection.close()

connection = sqlite3.connect('students.db')
cursor = connection.cursor()

cursor.execute("""INSERT INTO students (id, name, surname, gend, age, mail, grade, phone_number, grupa, form)
VALUES
    (1, "Елена", "Филатова", "Ж", 19, "elena@mail.com", 2, "+79854562535", "A1", "Б"),
    (2, "Иван", "Петров", "М", 20, "ivan@mail.com", 3, "+79123456789", "B2", "ВБ"),
    (3, "Анна", "Смирнова", "Ж", 18, "anna@mail.com", 1, "+79098765432", "A1", "ВБ"),
    (4, "Дмитрий", "Козлов", "М", 21, "dmitry@mail.com", 4, "+79234567890", "C3", "Ц"),
    (5, "Ольга", "Новикова", "Ж", 19, "olga@mail.com", 2, "+79345678901", "A1", "Б"),
    (6, "Алексей", "Морозов", "М", 20, "alex@mail.com", 3, "+79456789012", "B2", "Ц"),
    (7, "Мария", "Волкова", "Ж", 18, "maria@mail.com", 1, "+79567890123", "A1", "Б"),
    (8, "Сергей", "Павлов", "М", 22, "sergey@mail.com", 4, "+79678901234", "C3", "ВБ"),
    (9, "Екатерина", "Семенова", "Ж", 19, "ekaterina@mail.com", 2, "+79789012345", "A1", "Б"),
    (10, "Андрей", "Федоров", "М", 20, "andrey@mail.com", 3, "+79890123456", "B2", "Ц"),
    (11, "Наталья", "Кузнецова", "Ж", 18, "natalya@mail.com", 1, "+79901234567", "A1", "ВБ"),
    (12, "Артем", "Иванов", "М", 21, "artem@mail.com", 4, "+70012345678", "C3", "Б"),
    (13, "Юлия", "Лебедева", "Ж", 19, "yulia@mail.com", 2, "+70123456789", "A1", "Б"),
    (14, "Максим", "Соколов", "М", 20, "maxim@mail.com", 3, "+70234567890", "B2", "Ц"),
    (15, "Анастасия", "Козлова", "Ж", 18, "nastya@mail.com", 1, "+70345678901", "A1", "ВБ"),
    (16, "Павел", "Егоров", "М", 22, "pavel@mail.com", 4, "+70456789012", "C3", "ВБ"),
    (17, "Виктория", "Орлова", "Ж", 19, "vika@mail.com", 2, "+70567890123", "A1", "Б"),
    (18, "Кирилл", "Андреев", "М", 20, "kirill@mail.com", 3, "+70678901234", "B2", "Ц"),
    (19, "Алина", "Макарова", "Ж", 18, "alina@mail.com", 1, "+70789012345", "A1", "Б"),
    (20, "Денис", "Захаров", "М", 21, "denis@mail.com", 4, "+70890123456", "C3", "Б")

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



