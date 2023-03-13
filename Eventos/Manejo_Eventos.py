from PySide6.QtWidgets import QMainWindow,QPushButton, QApplication
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Señales y Eventos")
        boton = QPushButton("Click Aqui")
        self.setCentralWidget(boton)

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())