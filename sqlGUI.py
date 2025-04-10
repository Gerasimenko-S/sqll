import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QMessageBox, QHBoxLayout)
user1 = ["adminadmin"]
user2 = ["prof123"]
user3 = ["void100"]


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

        # Создаем layout и добавляем элементы
        layout = QVBoxLayout()

        layout.addWidget(self.label_login)
        layout.addWidget(self.edit_login)

        layout.addWidget(self.label_password)
        layout.addWidget(self.edit_password)

        # Горизонтальный layout для кнопки (чтобы она была по центру)
        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(self.button_login)
        h_layout.addStretch()

        layout.addLayout(h_layout)

        self.setLayout(layout)

    def on_login_clicked(self):
        global launch
        login = self.edit_login.text()
        password = self.edit_password.text()

        if password in user1 and login in user1:
            usermain = 1
            launch = 1
        if (password and login) in user2:
            usermain = 2
            launch = 1
        if (password and login) in user3:
            usermain = 3
            launch = 0
        if launch == 1:
            self.main_window = MainWindow()
            self.main_window.show()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Отклоннено в доступе или такой учетной записи не существует ')


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('БД Студенты')
        self.setGeometry(200, 200, 400, 300)

        # Можно добавить любой интерфейс в это окно
        label = QLabel('Добро пожаловать!', self)
        label.move(50, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
