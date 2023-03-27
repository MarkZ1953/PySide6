from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QGridLayout


class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()

        # Indicamos que se pueda agregar un color de fondo
        self.setAutoFillBackground(True)
        paleta_colores = self.palette()

        # Creamos el componente de color de fondo aplicando el nuevo color de fondo
        paleta_colores.setColor(QPalette.Window, QColor(nuevo_color))

        # Aplicamos el nuevo color al componente
        self.setPalette(paleta_colores)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layouts en Pyside")

        # Layout Grid
        layout = QGridLayout()
        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("blue"), 0, 2)
        layout.addWidget(Color("green"), 1, 1)
        layout.addWidget(Color("purple"), 1, 0)
        layout.addWidget(Color("yellow"), 1, 2)

        # Creamos un componente generico para poder publica el layout
        componente = QWidget()
        componente.setLayout(layout)

        # El componente se es expande para cubrir el tamaño disponible
        self.setCentralWidget(componente)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
