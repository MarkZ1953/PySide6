from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QTabWidget


class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()
        # Indicamos que se puede agregar un color de fondo
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        # Creamos el componente de color de fondo aplicando el nuevo color
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        # Aplicamos el nuevo color al componente
        self.setPalette(paletaColores)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tabulador en PySide')

        # Creamos el componente Tab
        tabulador = QTabWidget()

        # Posicion de las etiquetas del tabulador
        tabulador.setTabPosition(QTabWidget.South) # North, East, South, West

        # Indicamos siq ueremos que se muevan las etiquetas del tabulador
        tabulador.setMovable(True)

        # Para que se vea similar en MacOs
        tabulador.setDocumentMode(True)

        # Agregamos los colores a cada tabulador
        tabulador.addTab(Color("red"), "Rojo")
        tabulador.addTab(Color("blue"), "Azul")
        tabulador.addTab(Color("yellow"), "Amarillo")

        # Creamos un componente generico para poder publicar el layout
        self.setCentralWidget(tabulador)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
