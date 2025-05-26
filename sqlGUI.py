import sys
import re
from PyQt5 import Qt
from PyQt5.QtCore import Qt as QtCoreQt, QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QMessageBox, QHBoxLayout, QFrame, QTableWidget,
                             QTableWidgetItem, QInputDialog, QComboBox)

import sqlite3
from sql import get_students, delete_student_sql
user_db = [["admin", "admin", 3], ["prof", "123", 2], ["void", "100", 1]]



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.btn_delete = QPushButton("Удалить")
        self.btn_add = QPushButton("Добавить")
        self.btn_refresh = QPushButton("Обновить")
        self.setWindowTitle('БД Студенты')
        self.setGeometry(600, 450, 800, 600)
        self.setFixedSize(800, 550)
        self.setStyleSheet("background-color: #d0f4f7;")

        self.current_user_label = QLabel()
        self.current_user_label.setAlignment(QtCoreQt.AlignCenter)

        self.table = QTableWidget(self)
        self.table.setFixedHeight(400)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.load_student_data()

        self.setup_right_panel()

        self.create_buttons()
        self.setup_layout()

    def load_student_data(self):
        students_data = get_students()
        if students_data and students_data != "no data":
            if isinstance(students_data, str):
                try:
                    students_data = eval(students_data)
                except:
                    students_data = []
        if students_data and isinstance(students_data, (list, tuple)):
            self.table.setRowCount(len(students_data))
            self.table.setColumnCount(10)
            headers = ["ID", "Name", "Surname", "Gend", "Age", "Email", "Grade", "Phone", "Group", "Form"]
            self.table.setHorizontalHeaderLabels(headers)

            for row_idx, student in enumerate(students_data):
                for col_idx, value in enumerate(student):
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(row_idx, col_idx, item)
            self.table.resizeColumnsToContents()
            self.table.setAlternatingRowColors(True)
            self.table.setStyleSheet("alternate-background-color: #a0e1e8; background-color: #65bfb9;")

    def setup_right_panel(self):
        self.right_panel = QFrame()
        self.right_panel.setFixedWidth(200)
        self.right_panel.setStyleSheet("background-color: #b0e4e7; padding: 10px;")

        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["По умолчанию", "По курсу", "По возрасту", "По группе"])
        self.filter_combo.setCurrentIndex(0)
        self.filter_combo.currentIndexChanged.connect(self.apply_filter)

        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("Введите для поиска...")
        self.search_edit.setStyleSheet("padding: 5px;")

        self.search_button = QPushButton("Найти")
        self.search_button.setStyleSheet("padding: 5px; background-color: #65bfb9; color: black;")
        self.search_button.clicked.connect(self.execute_search)

        #self.search_edit.returnPressed.connect(self.execute_search)

        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("Фильтры:"))
        right_layout.addWidget(self.filter_combo)
        right_layout.addSpacing(20)
        right_layout.addWidget(QLabel("Поиск:"))
        right_layout.addWidget(self.search_edit)
        right_layout.addWidget(self.search_button)
        right_layout.addStretch()

        self.right_panel.setLayout(right_layout)
    def setup_layout(self):
        main_layout = QHBoxLayout(self)

        left_layout = QVBoxLayout()
        user_controls = QVBoxLayout()
        user_controls.addWidget(self.current_user_label)
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.btn_delete)
        buttons_layout.addWidget(self.btn_add)
        buttons_layout.addWidget(self.btn_refresh)
        buttons_layout.setSpacing(30)
        buttons_layout.setContentsMargins(0, 0, 0, 0)

        self.btn_delete.setFixedSize(100,50)
        self.btn_add.setFixedSize(100,50)
        self.btn_refresh.setFixedSize(100,50)
        self.btn_delete.setStyleSheet("background-color: #65bfb9; color: black;")
        self.btn_add.setStyleSheet("background-color: #65bfb9; color: black;")
        self.btn_refresh.setStyleSheet("background-color: #65bfb9; color: black;")
        user_controls.addLayout(buttons_layout)
        left_layout.addLayout(user_controls)
        left_layout.addWidget(self.table)

        main_layout.addLayout(left_layout)
        main_layout.addWidget(self.right_panel)

    def create_buttons(self):
        self.btn_delete.clicked.connect(self.delete_student)
        self.btn_refresh.clicked.connect(self.refresh_table)
        self.btn_add.clicked.connect(self.add_student)

    def current_user_commit(self, i=None):
            if current_user == user_db[i][0]:
                current_user_role=user_db[i][2]

            self.btn_delete.setEnabled(current_user_role == 3)
            self.btn_add.setEnabled(current_user_role in [2, 3])

    def apply_filter(self, index):
        students_data = get_students()
        if isinstance(students_data, str):
            try:
                students_data = eval(students_data)
            except:
                students_data = []

        if index == 0:
            sorted_data = sorted(students_data, key=lambda x: x[0])
        elif index == 1:
            sorted_data = sorted(students_data, key=lambda x: x[6])
        elif index == 2:
            sorted_data = sorted(students_data, key=lambda x: x[4])
        elif index == 3:
            sorted_data = sorted(students_data, key=lambda x: x[8])


        self.table.setRowCount(0)
        self.table.setRowCount(len(sorted_data))

        for row_idx, student in enumerate(sorted_data):
            for col_idx, value in enumerate(student):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row_idx, col_idx, item)



    def execute_search(self):
        search_text = self.search_edit.text()
        self.apply_search(search_text)

    def apply_search(self, text):

        try:
            search_text = text.lower().strip()

            if not search_text:
                self.refresh_table()
                return

            students_data = get_students()

            if not students_data or students_data == "no data":
                QMessageBox.information(self, "Поиск", "Нет данных для поиска")
                return

            if isinstance(students_data, str):
                students_data = eval(students_data)

            matched_rows = []
            for student in students_data:
                if any(search_text in str(field).lower() for field in student):
                    matched_rows.append(student)

            self.table.setRowCount(0)

            if matched_rows:
                self.table.setRowCount(len(matched_rows))
                for row_idx, student in enumerate(matched_rows):
                    for col_idx, value in enumerate(student):
                        item = QTableWidgetItem(str(value))
                        if search_text in str(value).lower():
                            item.setBackground(QtCoreQt.yellow)
                        self.table.setItem(row_idx, col_idx, item)
            else:
                QMessageBox.information(self, "Поиск", "Совпадений не найдено")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка поиска", f"Ошибка при поиске: {str(e)}")

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
                self.table.removeRow(row)
                delete_student_sql(student_id)

    def add_student(self):
        try:
            dialog = QInputDialog(self)
            dialog.setWindowTitle("Добавить студента")
            dialog.setLabelText(
                "Введите данные через запятую:\nИмя,Фамилия,Пол(M/Ж),Возраст,Email,Курс,Телефон,Группа,Форма(Б/К/Ц/ВБ)")

            if dialog.exec_():
                input_data = dialog.textValue()
                data = [x.strip() for x in input_data.split(',')]

                if len(data) != 9:
                    raise ValueError("Нужно ввести ровно 9 параметров")


                if data[2] not in ['М', 'Ж']:
                    raise ValueError("Пол должен быть M или Ж")

                if not data[3].isdigit() or not data[5].isdigit():
                    raise ValueError("Возраст и курс должны быть числами")

                if self.save_to_database(data):
                    self.refresh_table()
                    QMessageBox.information(self, "Успех", "Студент добавлен")

        except ValueError as ve:
            QMessageBox.warning(self, "Ошибка ввода", str(ve))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка: {str(e)}")
    def save_to_database(self, student_data):
        try:
            connection = sqlite3.connect('students.db')
            cursor = connection.cursor()

            # SQL-запрос для вставки данных
            cursor.execute("""
            INSERT INTO students (name, surname, gend, age, mail, grade, phone_number, grupa, form)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, student_data)

            connection.commit()
            connection.close()
            return True
        except Exception as e:
            QMessageBox.critical(self, "Ошибка БД", f"Ошибка при сохранении: {str(e)}")
            return False
    def refresh_table(self):
        students_data = get_students()
        self.table.setRowCount(0)

        if students_data and students_data != "no data":
            if isinstance(students_data, str):
                try:
                    students_data = eval(students_data)
                except:
                    students_data = []

            self.table.setRowCount(len(students_data))
            for row_idx, student in enumerate(students_data):
                for col_idx, value in enumerate(student):
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(row_idx, col_idx, item)


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Авторизация')
        self.setGeometry(200, 200, 300, 250)
        self.init_ui()

    def init_ui(self):
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
                global current_user
                current_user = login
                break

        if auth:
            self.main_window = MainWindow()
            # Устанавливаем текст лейбла
            self.main_window.current_user_label.setText(f"Текущий пользователь: {current_user}")
            self.main_window.show()
            self.close()
            return True
        else:
            QMessageBox.warning(self, 'Ошибка', 'Неверные данные или доступ отклонен')
            return None
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())