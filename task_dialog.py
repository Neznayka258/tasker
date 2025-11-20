from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog

from task_dialog_ui import Ui_TaskDialog

TASK_TYPES = ["Рабочая", "Личная", "Срочная", "Учебная", "Другое"]


class TaskEditorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TaskDialog()
        self.ui.setupUi(self)
        self.ui.edit_date.setDate(QDate.currentDate())
        self.ui.combo_type.clear()
        for name in TASK_TYPES:
            self.ui.combo_type.addItem(name)
        self.ui.combo_user.clear()
        self.ui.combo_user.addItem("Default", 1)
