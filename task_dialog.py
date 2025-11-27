from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDialog

from task_dialog_ui import Ui_TaskDialog

TASK_TYPES = ["Рабочая", "Личная", "Срочная", "Учебная", "Другое"]


class TaskEditorDialog(QDialog):
    def __init__(self, parent=None, task_data: dict | None = None):
        super().__init__(parent)
        self.ui = Ui_TaskDialog()
        self.ui.setupUi(self)
        self.ui.combo_type.clear()
        for name in TASK_TYPES:
            self.ui.combo_type.addItem(name)
        if hasattr(self.ui, "label_user"):
            self.ui.label_user.hide()
        if hasattr(self.ui, "combo_user"):
            self.ui.combo_user.hide()
        self.ui.edit_date.setDate(QDate.currentDate())
        if task_data:
            self.set_task_data(task_data)

    def set_task_data(self, task_data: dict):
        self.ui.edit_title.setText(task_data.get("title", ""))
        self.ui.edit_desc.setPlainText(task_data.get("description") or "")

        date_str = task_data.get("due_date")
        if date_str:
            date_obj = QDate.fromString(date_str, "dd.MM.yyyy")
            if not date_obj.isValid():
                date_obj = QDate.fromString(date_str, "yyyy-MM-dd")
            if date_obj.isValid():
                self.ui.edit_date.setDate(date_obj)

        priority = task_data.get("priority") or 1
        index = max(0, min(self.ui.combo_prio.count() - 1, int(priority) - 1))
        self.ui.combo_prio.setCurrentIndex(index)

        task_type = task_data.get("task_type")
        if task_type:
            type_index = self.ui.combo_type.findText(task_type)
            if type_index >= 0:
                self.ui.combo_type.setCurrentIndex(type_index)

    def get_data(self) -> dict:
        return {
            "title": self.ui.edit_title.text().strip(),
            "description": self.ui.edit_desc.toPlainText().strip(),
            "due_date": self.ui.edit_date.date().toString("dd.MM.yyyy"),
            "priority": self.ui.combo_prio.currentIndex() + 1,
            "task_type": self.ui.combo_type.currentText(),
            "user": "Default",
        }
