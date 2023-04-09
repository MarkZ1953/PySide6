from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication


class Componentes(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Componentes")
        self.setFixedSize(500, 600)

        # Creamos la etiqueta
        etiqueta = QLabel()
        etiqueta.setPixmap(QPixmap("layla.jpg"))
        etiqueta.setScaledContents(True)

        # Publicamos el componente
        self.setCentralWidget(etiqueta)


if __name__ == "__main__":
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
