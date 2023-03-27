import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Clase base de Qt (Pyside)
# Se encarga de procesar los eventos (event loop)

app = QApplication()

# Crear un objeto ventana

# ventana = QPushButton("Boton de PySide")

# ventana = QWidget()

ventana = QMainWindow()  # Forma recomendada

# Cualquier componente puede ser una ventana en PySide
# Siempre y cuando sea un componente principal

# Cambiar el titulo de la ventana

ventana.setWindowTitle("Primera Ventana - Pyside")

# Cambiar el tamaño de la ventana

ventana.resize(600, 400)

# Mostrar la ventana

ventana.show()

# Se ejecuta la aplicacion

sys.exit(app.exec())
