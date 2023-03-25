from random import randint

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QLabel


class NuevaVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nueva Ventana')
        layout = QVBoxLayout()
        self.etiqueta = QLabel(f"Nueva ventana: {randint(0, 100)}")
        layout.addWidget(self.etiqueta)
        self.setLayout(layout)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.nueva_ventana = NuevaVentana()
        self.setWindowTitle('Ventanas')
        self.boton = QPushButton('Mostrar/Ocultar nueva ventana')
        self.boton.clicked.connect(self.mostrar_nueva_ventana)
        self.setCentralWidget(self.boton)

    def mostrar_nueva_ventana(self):
        if self.nueva_ventana.isVisible():
            self.nueva_ventana.hide()
        else:
            self.nueva_ventana.show()


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
