from PySide6.QtWidgets import QMainWindow,QLabel,QApplication
from PySide6.QtCore import Qt

class Componentes(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Componentes")

        #Creamos la etiqueta
        etiqueta = QLabel("Hola")

        #Modificamos el valor inicial
        etiqueta.setText("Saludos")

        #Modificar la fuente
        fuente = etiqueta.font()
        fuente.setPointSize(25) #Valor default = 12
        etiqueta.setFont(fuente)

        #Modificar la alineacion de la etiqueta
        # etiqueta.setAlignment(Qt.AlignCenter)
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        #Publicamos el componente
        self.setCentralWidget(etiqueta)

if __name__ == "__main__":

    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
        