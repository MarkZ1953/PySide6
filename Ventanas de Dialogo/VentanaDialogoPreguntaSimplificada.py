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

        # Creamos el Dialogo
        dialogo = QMessageBox.question(self, "Pregunta", "Esta es una ventana de dialogo de pregunta simplificada")

        if dialogo == QMessageBox.Yes:
            print("Regreso el valor de Si")
        else:
            print("Regreso un valor de No")


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
