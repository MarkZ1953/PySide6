from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QCheckBox, QApplication


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Componentes")

        # Creamos un nuevo checkbox
        checkbox = QCheckBox("Este es un CheckBox")

        # Activamos el tercer estado
        checkbox.setTristate(True)

        # Conectar la señal de cambio del widget
        checkbox.stateChanged.connect(self.mostrar_estado)

        # Publicamos el widget
        self.setCentralWidget(checkbox)

    def mostrar_estado(self, estado):
        print(f"Estado : {estado}")

        """
        #############################
        Trabajamos con las constantes
        #############################
        
        if estado == Qt.Checked:
            print("CheckBox encendido")
        elif estado == Qt.PartiallyChecked:
            print("CheckBox sin estado o parcialmente checado")
        elif estado == Qt.Unchecked:
            print("CheckBox apagado")
        else:
            print("Estado Invalido")
            
        ###########################################################################
        En la version actual de PySide6 NO se pueden manejar los estados de checado
        usando las constantes. (6.4.1)
        ###########################################################################
        """

        if estado == 0:
            print("CheckBox Apagado")
        elif estado == 1:
            print("Sin estado o parcialmente checado")
        elif estado == 2:
            print("CheckBox Encendido")
        else:
            print("Estado Invalido")


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
