import sys

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication

from src.main_window import TaskManagerWindow


app = QApplication(sys.argv)
font = QFont("Arial", 10)
app.setFont(font)
window = TaskManagerWindow()
window.show()

sys.exit(app.exec())
