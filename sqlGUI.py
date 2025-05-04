import sys
from io import text_encoding
import re
from PyQt5 import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QMessageBox, QHBoxLayout, QFrame)
import sqlite3
from sql import get_students

# База данных пользователей (логин, пароль)
user_db = [["admin", "admin"], ["prof", "123"], ["void", "100"]]



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('БД Студенты')
        self.setGeometry(600, 600, 600, 600)

        main_font=QFont("Arial", 12)
        db_label = QLabel(self)
        text_from_db=get_students()
        trash={"]", "["}
        text_from_db=''.join(char for char in text_from_db if char not in trash)

        parts = text_from_db.split("),")
        formatted_text = "),\n".join(parts)
        db_label.setText(formatted_text)
        db_label.move(50, 50)
        db_label.setFrameStyle(QFrame.Box | QFrame.Plain)
        db_label.setFont(main_font)

        hat_label = QLabel("ID   Имя   Фам-ия   Пол   Эл.Почта   Курс   Телефон ",self)
        hat_label.move(50,25)
        hat_label.setFont(main_font)




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