from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Contextual')

    def contextMenuEvent(self, evento):
        menu_contextual = QMenu(self)

        # Creamos los botones, se les agrega imagenes y el texto del boton
        boton_nuevo = QAction(QIcon('nuevo.png'), 'Nuevo', self)
        boton_guardar = QAction(QIcon('guardar.png'), 'Guardar', self)
        boton_salir = QAction('Salir', self)

        # Conectamos los botones a un slot o un metodo
        boton_guardar.triggered.connect(self.activar_boton_guardar)
        boton_nuevo.triggered.connect(self.activar_boton_nuevo)
        boton_salir.triggered.connect(self.activar_boton_salir)

        # Se agregan los botones al menu contextual
        menu_contextual.addAction(boton_nuevo)
        menu_contextual.addAction(boton_guardar)
        menu_contextual.addAction(boton_salir)

        # Recuperamos la posicion del cursor como posicion global de la ventana padre
        # Y ejecutamos el menu contextual
        menu_contextual.exec(evento.globalPos())

    def activar_boton_salir(self):
        print("Saliendo de la aplicacion...")

    def activar_boton_guardar(self):
        print("Guadando...")

    def activar_boton_nuevo(self):
        print("Creando nuevo archivo...")


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
