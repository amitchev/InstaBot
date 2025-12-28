import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class InstaBot(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.hello_options = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Fuck off!")
        self.text = QtWidgets.QLabel("Fuck you!",
                                     alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.bitch_nigga)

    @QtCore.Slot()
    def bitch_nigga(self):
        self.text.setText(random.choice(self.hello_options))
        












if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = InstaBot()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
