from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialogos')

        # Agregamos un boton
        boton = QPushButton("Mostrar dialogo")
        boton.clicked.connect(self.click_boton)

        # Publicamos el boton
        self.setCentralWidget(boton)

    def click_boton(self, estado):
        print(f"Click sobre boton {estado}")

        # Creamos el dialogo
        dialogo = QMessageBox(self)
        dialogo.setWindowTitle("Ventana de Dialogo con Pregunta")
        dialogo.setText("Ventana de Dialogo con Pregunta")

        # Agregamos los botones de la respuesta a la pregunta
        dialogo.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Agregamos un icono a la ventana de dialogo
        dialogo.setIcon(QMessageBox.Question)

        valor_retornado = dialogo.exec()

        # Imprimir el valor retornado
        print(f"Valor retornado : {valor_retornado}")

        if valor_retornado == QMessageBox.Yes:
            print("Regreso el valor de Si")
        else:
            print("Regreso un valor de No")


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
