from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QGridLayout, QPushButton, QWidget, QApplication, QVBoxLayout, QLineEdit


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.botones = {}
        self.grid_layout = None
        self.entrada_texto = None

        self.setWindowTitle("Calculadora")
        self.setFixedSize(235, 270)

        # Creamos un layout principal
        self.layout_principal = QVBoxLayout()

        # Llamamos al metodo que crea la entrada de texto
        self.crear_entrada_de_texto()

        # Creamos los botones
        self.crear_botones()

        # Agregamos el QGridLayout al layout principal
        self.layout_principal.addWidget(self.entrada_texto)
        self.layout_principal.addLayout(self.grid_layout)

        # Creamos un componente QWidget para alojar al layout principal
        self.componente_general = QWidget(self)
        self.componente_general.setLayout(self.layout_principal)

        # Publicamos el componente general
        self.setCentralWidget(self.componente_general)

    def crear_entrada_de_texto(self):

        # Creamos la entrada de texto
        self.entrada_texto = QLineEdit()

        # Modificamos algunas propiedades
        self.entrada_texto.setReadOnly(True)
        self.entrada_texto.setFixedHeight(35)
        self.entrada_texto.setAlignment(Qt.AlignmentFlag.AlignRight)

    def crear_botones(self):
        # Creamos el grid layout donde estan estaran los botones
        self.grid_layout = QGridLayout()

        botones = {
            "C": (0, 0),
            "\u232B": (0, 2),
            "/": (0, 3),
            "7": (1, 0),
            "8": (1, 1),
            "9": (1, 2),
            "*": (1, 3),
            "4": (2, 0),
            "5": (2, 1),
            "6": (2, 2),
            "-": (2, 3),
            "1": (3, 0),
            "2": (3, 1),
            "3": (3, 2),
            "+": (3, 3),
            "0": (4, 0),
            ".": (4, 2),
            "=": (4, 3)
        }

        for texto_boton, posicion in botones.items():
            self.botones[texto_boton] = QPushButton(texto_boton)
            self.botones[texto_boton].setFixedHeight(40)
            self.botones[texto_boton].pressed.connect(lambda k=texto_boton: self.boton_pulsado(k))

            if texto_boton == "C":
                self.botones[texto_boton].setShortcut(Qt.Key.Key_Delete)
                self.grid_layout.addWidget(self.botones[texto_boton], posicion[0], posicion[1], 1, 2)
            elif texto_boton == "\u232B":
                self.botones[texto_boton].setShortcut(Qt.Key.Key_Backspace)
                self.grid_layout.addWidget(self.botones[texto_boton], posicion[0], posicion[1])
            elif texto_boton == "0":
                self.grid_layout.addWidget(self.botones[texto_boton], posicion[0], posicion[1], 1, 2)
            elif texto_boton == "=":
                self.botones[texto_boton].setShortcut(Qt.Key.Key_Return)
                self.grid_layout.addWidget(self.botones[texto_boton], posicion[0], posicion[1])
            else:
                self.grid_layout.addWidget(self.botones[texto_boton], posicion[0], posicion[1])

    def keyPressEvent(self, event) -> None:

        # print(f"Se presiono la Key : {event.key()}")

        permitidos = [Qt.Key.Key_1,
                      Qt.Key.Key_2,
                      Qt.Key.Key_3,
                      Qt.Key.Key_4,
                      Qt.Key.Key_5,
                      Qt.Key.Key_6,
                      Qt.Key.Key_7,
                      Qt.Key.Key_8,
                      Qt.Key.Key_9,
                      Qt.Key.Key_0,
                      Qt.Key.Key_Slash,
                      Qt.Key.Key_Minus,
                      Qt.Key.Key_Plus,
                      Qt.Key.Key_Asterisk]

        if event.key() == Qt.Key.Key_Return and (self.entrada_texto.text() != ""):
            self.boton_pulsado("=")

        if self.entrada_texto.text() == "\u232B":
            self.borrar_ultimo_caracter()

        if event.key() in permitidos:
            if self.entrada_texto.text() in ["Ocurrio un Error", "No puedes Dividir por Cero"]:
                self.entrada_texto.clear()
                self.entrada_texto.insert(str(event.text()))
            else:
                self.entrada_texto.insert(str(event.text()))

    def boton_pulsado(self, texto_boton):

        try:
            if texto_boton == "C":
                self.entrada_texto.clear()
            elif texto_boton == "=":
                resultado = str(eval(self.entrada_texto.text()))
                self.entrada_texto.clear()
                self.entrada_texto.insert(resultado)
            elif texto_boton == "\u232B":
                self.borrar_ultimo_caracter()
            else:
                if self.entrada_texto.text() in ["Ocurrio un Error", "No puedes Dividir por Cero"]:
                    self.entrada_texto.clear()
                    self.entrada_texto.insert(texto_boton)
                else:
                    self.entrada_texto.insert(texto_boton)
        except ZeroDivisionError:
            self.entrada_texto.clear()
            self.entrada_texto.insert("No puedes Dividir por Cero")
        except Exception:
            self.entrada_texto.clear()
            self.entrada_texto.insert("Ocurrio un Error")

    def borrar_ultimo_caracter(self):
        texto = self.entrada_texto.text()
        self.entrada_texto.clear()
        self.entrada_texto.insert(texto[:-1])


if __name__ == '__main__':
    app = QApplication([])
    ventana = Calculadora()
    ventana.show()
    app.exec()
