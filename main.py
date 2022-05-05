
from interface import *

#Uruchomienie okna
if __name__ == "__main__":
    app = QApplication([])

    login_window = LoginWindow()

    app.exec()