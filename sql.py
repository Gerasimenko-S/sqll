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
    phone_number VARCHAR(10),
    grupa VARCHAR(10),
    form VARCHAR(3)

)
""")
connection.commit()
connection.close()

connection = sqlite3.connect('students.db')
cursor = connection.cursor()

cursor.execute("""INSERT INTO students (id, name, surname, sex, age, mail, grade, phone_number, grupa, form)
VALUES
     (1, "Елена", "Филатова", "F", 19, "elena@mail.com", 2, "+79854562535", "A1", "Б"),
    (2, "Иван", "Петров", "M", 20, "ivan@mail.com", 3, "+79123456789", "B2", "ВБ"),
    (3, "Анна", "Смирнова", "F", 18, "anna@mail.com", 1, "+79098765432", "A1", "ВБ"),
    (4, "Дмитрий", "Козлов", "M", 21, "dmitry@mail.com", 4, "+79234567890", "C3", "Ц"),
    (5, "Ольга", "Новикова", "F", 19, "olga@mail.com", 2, "+79345678901", "A1", "Б"),
    (6, "Алексей", "Морозов", "M", 20, "alex@mail.com", 3, "+79456789012", "B2", "Ц"),
    (7, "Мария", "Волкова", "F", 18, "maria@mail.com", 1, "+79567890123", "A1", "Б"),
    (8, "Сергей", "Павлов", "M", 22, "sergey@mail.com", 4, "+79678901234", "C3", "ВБ"),
    (9, "Екатерина", "Семенова", "F", 19, "ekaterina@mail.com", 2, "+79789012345", "A1", "Б"),
    (10, "Андрей", "Федоров", "M", 20, "andrey@mail.com", 3, "+79890123456", "B2", "Ц"),
    (11, "Наталья", "Кузнецова", "F", 18, "natalya@mail.com", 1, "+79901234567", "A1", "ВБ"),
    (12, "Артем", "Иванов", "M", 21, "artem@mail.com", 4, "+70012345678", "C3", "Б"),
    (13, "Юлия", "Лебедева", "F", 19, "yulia@mail.com", 2, "+70123456789", "A1", "Б"),
    (14, "Максим", "Соколов", "M", 20, "maxim@mail.com", 3, "+70234567890", "B2", "Ц"),
    (15, "Анастасия", "Козлова", "F", 18, "nastya@mail.com", 1, "+70345678901", "A1", "ВБ"),
    (16, "Павел", "Егоров", "M", 22, "pavel@mail.com", 4, "+70456789012", "C3", "ВБ"),
    (17, "Виктория", "Орлова", "F", 19, "vika@mail.com", 2, "+70567890123", "A1", "Б"),
    (18, "Кирилл", "Андреев", "M", 20, "kirill@mail.com", 3, "+70678901234", "B2", "Ц"),
    (19, "Алина", "Макарова", "F", 18, "alina@mail.com", 1, "+70789012345", "A1", "Б"),
    (20, "Денис", "Захаров", "M", 21, "denis@mail.com", 4, "+70890123456", "C3", "Б")

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




