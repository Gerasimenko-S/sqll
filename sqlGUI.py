import sys
import re
from PyQt5 import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QMessageBox, QHBoxLayout, QFrame, QTableWidget, QTableWidgetItem, QInputDialog)
import sqlite3
from sql import get_students, delete_student_sql

# База данных пользователей (логин, пароль)
user_db = [["admin", "admin", 3], ["prof", "123", 2], ["void", "100", 1]]


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.btn_delete = QPushButton("Удалить")
        self.btn_add = QPushButton("Добавить")
        self.btn_refresh = QPushButton("Обновить")
        self.setWindowTitle('БД Студенты')
        self.setGeometry(600, 600, 600, 600)
        self.setStyleSheet("background-color: #d0f4f7;")

        # Создаем таблицу
        self.table = QTableWidget(self)

        # Получаем данные
        students_data = get_students()

        # Настраиваем таблицу
        if students_data and students_data != "no data":
            if isinstance(students_data, str):
                try:
                    students_data = eval(students_data)
                except:
                    students_data = []

        if students_data and isinstance(students_data, (list, tuple)):
            self.table.setRowCount(len(students_data))
            self.table.setColumnCount(8)
            headers = ["ID", "Name", "Surname", "Sex", "Age", "Email", "Grade", "Phone"]
            self.table.setHorizontalHeaderLabels(headers)

            for row_idx, student in enumerate(students_data):
                for col_idx, value in enumerate(student):
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(row_idx, col_idx, item)

            self.table.resizeColumnsToContents()
            self.table.setAlternatingRowColors(True)
            self.table.setStyleSheet("alternate-background-color: #a0e1e8;")
        else:
            no_data_label = QLabel("Нет данных для отображения", self)
            no_data_label.move(50, 50)

        # Создаем кнопки и layout
        self.create_buttons()
        self.setup_layout()  # Это ключевая строка, которую вы пропустили


    def setup_layout(self):
        # Горизонтальный layout для кнопок
        button_layout = QHBoxLayout()
       # button_layout.addWidget(self.btn_refresh)
       # button_layout.addWidget(self.btn_add)
        button_layout.addWidget(self.btn_delete)

        # Основной вертикальный layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table)
        main_layout.addLayout(button_layout)

        # Устанавливаем layout для главного окна
        self.setLayout(main_layout)

    def create_buttons(self):
        self.btn_delete = QPushButton("Удалить", self)
        self.btn_delete.clicked.connect(self.delete_student)
        self.btn_delete.setEnabled(False)


    def delete_student(self):
        selected = self.table.selectedItems()
        if selected:
            row = selected[0].row()
            student_id = self.table.item(row, 0).text()

            reply = QMessageBox.question(
                self, 'Подтверждение',
                f"Удалить студента ID {student_id}?",
                QMessageBox.Yes | QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                print(f"Удаляем студента ID {student_id}")
                delete_student_sql(student_id)
                self.refresh_data()


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Авторизация')
        self.setGeometry(200, 200, 300, 250)
        self.init_ui()

    def init_ui(self):
        # Создаем элементы интерфейса
        self.label_login = QLabel('Логин:')
        self.edit_login = QLineEdit()
        self.edit_login.setPlaceholderText('Введите ваш логин')

        self.label_password = QLabel('Пароль:')
        self.edit_password = QLineEdit()
        self.edit_password.setPlaceholderText('Введите ваш пароль')

        self.button_login = QPushButton('Войти')
        self.button_login.clicked.connect(self.on_login_clicked)

        layout = QVBoxLayout()

        layout.addWidget(self.label_login)
        layout.addWidget(self.edit_login)

        layout.addWidget(self.label_password)
        layout.addWidget(self.edit_password)

        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(self.button_login)
        h_layout.addStretch()

        layout.addLayout(h_layout)

        self.setLayout(layout)

    def on_login_clicked(self):
        login = self.edit_login.text()
        password = self.edit_password.text()
        auth = False
        for user in user_db:
            if user[0] == login and user[1] == password:
                auth = True
                break

        if auth:
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Отклонено в доступе или такой учетной записи не существует')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
