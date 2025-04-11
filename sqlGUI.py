import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QMessageBox, QHBoxLayout)

# База данных пользователей (логин, пароль)
user_db = [["admin", "admin"], ["prof", "123"], ["void", "100"]]


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('БД Студенты')
        self.setGeometry(200, 200, 400, 300)


        label = QLabel('Добро пожаловать!', self)
        label.move(50, 50)


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