from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QLineEdit, QCompleter, QVBoxLayout, QWidget

class NumberCompleter(QCompleter):
    def __init__(self, parent=None):
        super(NumberCompleter, self).__init__(parent)
        self.setCaseSensitivity(Qt.CaseInsensitive)
        self.setModel(QStandardItemModel(self))

    def splitPath(self, path):
        # Obtener sugerencias de una función propia o de cualquier otra fuente
        sugerencias = [str(i) for i in range(100) if str(i).startswith(path)]
        self.model().clear()
        for i, sug  erencia in enumerate(sugerencias):
            item = QStandardItem(sugerencia)
            self.model().setItem(i, item)
        return []

app = QApplication([])

widget = QWidget()

layout = QVBoxLayout()

# Creamos un QLineEdit
line_edit = QLineEdit()
layout.addWidget(line_edit)

# Creamos nuestro NumberCompleter personalizado y lo establecemos en el QLineEdit
completer = NumberCompleter()
line_edit.setCompleter(completer)

widget.setLayout(layout)

widget.show()

app.exec_()
