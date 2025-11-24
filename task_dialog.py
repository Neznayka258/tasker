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
        if hasattr(self.ui, "label_user"):
            self.ui.label_user.hide()
        if hasattr(self.ui, "combo_user"):
            self.ui.combo_user.hide()

    def get_data(self) -> dict:
        return {
            "title": self.ui.edit_title.text().strip(),
            "description": self.ui.edit_desc.toPlainText().strip(),
            "due_date": self.ui.edit_date.date().toString("dd.MM.yyyy"),
            "priority": self.ui.combo_prio.currentIndex() + 1,
            "task_type": self.ui.combo_type.currentText()
        }