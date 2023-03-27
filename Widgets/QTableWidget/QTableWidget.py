import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear una tabla con 2 columnas y 3 filas
        table = QTableWidget(self)
        table.setColumnCount(2)
        table.setRowCount(3)

        # Agregar datos a la tabla
        table.setItem(0, 0, QTableWidgetItem("Juan"))
        table.setItem(0, 1, QTableWidgetItem("25"))
        table.setItem(1, 0, QTableWidgetItem("María"))
        table.setItem(1, 1, QTableWidgetItem("30"))
        table.setItem(2, 0, QTableWidgetItem("Pedro"))
        table.setItem(2, 1, QTableWidgetItem("35"))

        # Ajustar tamaño de columnas y filas
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        # Agregar la tabla al layout principal
        self.setCentralWidget(table)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
