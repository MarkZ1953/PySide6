from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialogos')
        # Agregamos un boton
        boton = QPushButton('Mostrar dialogo')
        boton.clicked.connect(self.click_boton)

        # Publicamos el boton
        self.setCentralWidget(boton)

    def click_boton(self, s):
        print(f'Click sobre boton: {s}')
        # Creamos el dialogo personalizada
        dialogo = QMessageBox.critical(self, 'Problema Critico',
                                       'Ventana con problema critico',
                                       buttons=QMessageBox.Discard |
                                       QMessageBox.NoToAll |
                                       QMessageBox.Ignore,
                                       defaultButton=QMessageBox.Discard)

        # Revisamos cual boton se presiono
        if dialogo == QMessageBox.Discard:
            print('Regreso el valor Discard')
        elif dialogo == QMessageBox.NoToAll:
            print('Regreso el valor de NoToAll')
        else:
            print('Se presiono el boton de Ignore (ignorar)')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()