import pytest
from PyQt5.QtWidgets import QApplication
from sqlGUI import LoginWindow, MainWindow, user_db, delete_student_sql, get_students
import sqlite3
import sys

@pytest.fixture(scope="session")
def sqlapp():
    app = QApplication(sys.argv)
    yield app
    app.quit()


def test_login_right(sqlapp):
    login_window = LoginWindow()
    login_window.edit_login.setText("admin")
    login_window.edit_password.setText("admin1")
    assert login_window.on_login_clicked() == True

def test_login_wrong(sqlapp):
    login_window = LoginWindow()
    login_window.edit_login.setText("admin")
    login_window.edit_password.setText("admin")
    assert login_window.on_login_clicked() is None

def test_window_open(sqlapp, monkeypatch):
    login_window = LoginWindow()
    login_window.edit_login.setText("admin")
    login_window.edit_password.setText("admin")

    mock_mainwindow = None

    def mock_show(self):
        nonlocal mock_mainwindow
        mock_mainwindow = self

    monkeypatch.setattr(MainWindow, 'show', mock_show)

    login_window.on_login_clicked()
    assert isinstance(mock_mainwindow, MainWindow)



def test_window_not_open(sqlapp, monkeypatch):
    login_window = LoginWindow()
    login_window.edit_login.setText("wrong")
    login_window.edit_password.setText("wrong")

    mock_mainwindow = None

    def mock_show(self):
        nonlocal mock_mainwindow
        mock_mainwindow = self

    monkeypatch.setattr(MainWindow, 'show', mock_show)

    login_window.on_login_clicked()
    assert mock_mainwindow is None



def test_delete_student_from_db():

    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO students (id, name, surname, sex, age, mail, grade, phone_number)"
        " VALUES (99, 'Test', 'Student', 'M', 20, 'test@mail.com', 1, '1234567890')")
    connection.commit()
    connection.close()

    students_before = get_students()
    assert "'Test'" in students_before

    delete_student_sql(99)

    students_after = get_students()
    assert "'Test'" not in students_after