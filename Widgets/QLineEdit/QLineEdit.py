from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit


class Componentes(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Componentes")

        # Componente QLineEdit
        linea_texto = QLineEdit()

        # Establecemos el maximo de caracteres a capturar
        linea_texto.setMaxLength(15)

        # Establecemos un texto de ayuda (placeholder)
        linea_texto.setPlaceholderText("Introduce tu nombre : ")

        # Solo lectura
        # linea_texto.setReadOnly(True)

        # Validacion (mask)
        linea_texto.setInputMask("00-0000-0000")

        # Evento enter, cambio de seleccion de texto, cambio de texto
        linea_texto.returnPressed.connect(self.enter_presionado)
        linea_texto.selectionChanged.connect(self.cambio_seleccion)
        linea_texto.textChanged.connect(self.cambio_texto)

        # Publicamos este componente
        self.setCentralWidget(linea_texto)

    def enter_presionado(self):
        print("Se presiono el enter")
        self.centralWidget().setText("Juan Perez")

    def cambio_seleccion(self):
        print("Cambio seleccion de texto")
        print(self.centralWidget().selectedText())

    def cambio_texto(self, nuevo_texto):
        print("Cambio de texto")
        print(self.centralWidget().cleanText())


if __name__ == "__main__":
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
