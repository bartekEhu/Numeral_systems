from interface import *

if __name__ == "__main__":
    app = QApplication([])

    login_window = LoginWindow(400, 600)

    app.exec()
