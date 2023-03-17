import sys
from PyQt6.QtWidgets import QApplication, QWidget
from Prueba import Ui_MainWindow


class Main(QWidget):
    def __init__(self):
        super().__init__()

        # use the Ui_login_form
        self.ui = Ui_MainWindow()       
        self.ui.setupUi(self)       
        
        # show the login window
        self.show()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Main()
    sys.exit(app.exec())