from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar, QCheckBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Barra de Herramientas')

        # Publicamos una etiqueta
        etiqueta = QLabel("Hola")
        etiqueta.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(etiqueta)

        # Creamos la barra de herramientas
        barra = QToolBar("Mi barra de herramientas")
        barra.setIconSize(QSize(16, 16))

        #Configuracion para mostrar la barra de herramientas
        # barra.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        # barra.setToolButtonStyle(Qt.ToolButtonTextOnly)
        # barra.setToolButtonStyle(Qt.ToolButtonIconOnly)
        # barra.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # barra.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.addToolBar(barra)

        # Agregamos un elemento a nuestra barra de herramientas
        boton_nuevo = QAction(QIcon("nuevo.png"), "Nuevo", self)
        boton_guardar = QAction(QIcon("guardar.png"), "Guardar", self)
        boton_acerca = QAction(QIcon("acerca.png"), "Acerca", self)

        # Agregamos el boton a la barra
        barra.addAction(boton_nuevo)
        barra.addAction(boton_guardar)
        barra.addAction(boton_acerca)

        # Barra de estado
        self.setStatusBar(QStatusBar(self))

        # Mostramos el mensaje de boton de accion
        boton_nuevo.setStatusTip("Nuevo archivo")
        boton_guardar.setStatusTip("Guardar Archivo")
        boton_acerca.setStatusTip("Acerca")

        # Asociamos el evento click
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardar.triggered.connect(self.click_boton_guardar)
        boton_acerca.triggered.connect(self.click_boton_acerca)

        barra.addSeparator()
        barra.addWidget(QCheckBox())
        barra.addWidget(QLabel("Salir"))

        # Hacemos checable el boton
        # boton_nuevo.setCheckable(True)

    def click_boton_nuevo(self, estado):
        print(f"Nuevo archivo {estado}")

    def click_boton_guardar(self, estado):
        print(f"Gurdando...{estado}")

    def click_boton_acerca(self, estado):
        print(f"Acerca de...{estado}")


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
