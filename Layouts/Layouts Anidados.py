from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout


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

        # Anidar Layouts (layout dentro de otro layout)
        # Creamos en primer lugar un layout vertical y despues un horizontal
        layout_horizontal = QHBoxLayout()
        layout_vertical = QVBoxLayout()

        # Agregamos espacio al layout horizontal
        layout_horizontal.setContentsMargins(10, 10, 10, 10)

        # Agregamos un espacio entre cada elemento del layout horizontal
        layout_horizontal.setSpacing(30)

        # Agregamos espacio en el layout vertical
        layout_vertical.setContentsMargins(5, 10, 5, 10)

        # Agregamos un espacio dentro de cada elemento de layout vertical
        layout_vertical.setSpacing(20)

        # Agregamos algunos widgets al layout vertical
        layout_vertical.addWidget(Color("red"))
        layout_vertical.addWidget(Color("green"))
        layout_vertical.addWidget(Color("blue"))

        # Agregamos el layout vertical dentro del layout horizontal
        # Es decir se agrega de manera anidada, un layout dentro de otro
        layout_horizontal.addLayout(layout_vertical)

        # Agregamos mas elementos al layout horizontal
        layout_horizontal.addWidget(Color("yellow"))
        layout_horizontal.addWidget(Color("purple"))

        # Creamos un componente generico para poder publicar el layout
        componente = QWidget()
        componente.setLayout(layout_horizontal)

        # El componente se es expande para cubrir el tamaño disponible
        self.setCentralWidget(componente)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
