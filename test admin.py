import unittest
from sqlGUI import LoginWindow

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.LoginWindow=LoginWindow()
    def logintest(self):
        self.assertEqual(self.LoginWindow.edit_login.text(),"admin")
        self.assertEqual(self.LoginWindow.edit_password.text(), "admin")

if __name__ == '__main__':
    unittest.main()
