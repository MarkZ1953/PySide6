from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication


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

        componente_con_color_fondo = Color("blue")

        # El componente se es expande para cubrir el tamaño disponible
        self.setCentralWidget(componente_con_color_fondo)


if __name__ == '__main__':
    app = QApplication([])
    ventana =  VentanaPrincipal()
    ventana.show()
    app.exec()


