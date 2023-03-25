from PySide6.QtWidgets import QMainWindow, QApplication, QSlider
from PySide6.QtCore import Qt


class Componentes(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Componentes")

        # QSlider es para valores numericos enteros en un slider (deslizadora)
        slider = QSlider()
        # slider = QSlider(Qt.Horizontal)
        # slider.setMinimum(-5)
        # slider.setMaximum(8)
        slider.setRange(-5, 8)

        # Conectamos a la señales
        slider.valueChanged.connect(self.cambio_valor)
        slider.sliderMoved.connect(self.slider_cambio_posicion)
        slider.sliderPressed.connect(self.slider_presionado)
        slider.sliderReleased.connect(self.slider_liberado)

        # Publicamos este componente
        self.setCentralWidget(slider)

    def cambio_valor(self, nuevo_valor):
        print(f"Nuevo valor : {nuevo_valor}")

    def slider_cambio_posicion(self, nueva_posicion):
        print(f"Nueva posicion : {nueva_posicion}")

    def slider_presionado(self):
        print("Slider Presionado")

    def slider_liberado(self):
        print("Slider Liberado")


if __name__ == "__main__":
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
