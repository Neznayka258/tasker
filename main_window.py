from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
)

from db_manager import DBManager
from main_window_ui import Ui_MainWindow
from task_dialog import TaskEditorDialog

MESSAGE_TEXT = "Функция пока не реализована"


class TaskManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._tasks: list[dict] = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._connect_buttons()
        self._connect_actions()
        self.ui.stacked.setCurrentIndex(0)
        self.ui.lbl_status.setText("")
        self.ui.table.setColumnHidden(6, True)
        self.db = DBManager()
        self._refresh_table()


    def _connect_buttons(self):
        self.ui.btn_add.clicked.connect(self.show_dialog)
        self.ui.btn_delete.clicked.connect(self.delete_task)
        self.ui.btn_edit.clicked.connect(self.edit_task)
        for button in [
            self.ui.btn_done,
            self.ui.btn_prev,
            self.ui.btn_next,
        ]:
            button.clicked.connect(self.show_message)
        self.ui.edit_search.textChanged.connect(lambda _: self.show_message())

    def _connect_actions(self):
        action_map = {
            self.ui.actionNew: self.show_message,
            self.ui.actionOpen: self.show_message,
            self.ui.actionSave: self.show_message,
            self.ui.actionExit: self.close,
            self.ui.actionAddTask: self.show_dialog,
            self.ui.actionEdit: self.edit_task,
            self.ui.actionDelete: self.delete_task,
            self.ui.actionDone: self.show_message,
            self.ui.actionAll: self.show_message,
            self.ui.actionDoneOnly: self.show_message,
            self.ui.actionUndone: self.show_message,
            self.ui.actionFilterDate: self.show_message,
            self.ui.actionFilterType: self.show_message,
            self.ui.actionThemeLight: self.show_message,
            self.ui.actionThemeDark: self.show_message,
        }
        for action, slot in action_map.items():
            if action is not None:
                action.triggered.connect(slot)

    def show_dialog(self):
        dialog = TaskEditorDialog(self)
        if dialog.exec():
            data = dialog.get_data()
            self.db.add_task(
                title=data["title"],
                description=data["description"],
                due_date=data["due_date"],
                priority=data["priority"],
                task_type=data["task_type"],
            )
            self._refresh_table()

    def show_message(self, *_):
        QMessageBox.information(self, "Информация", MESSAGE_TEXT)

    def _refresh_table(self):
        self._tasks = [dict(task) for task in self.db.get_tasks()]
        self.ui.table.setRowCount(len(self._tasks))
        if not self._tasks:
            self.ui.stacked.setCurrentIndex(0)
            self.ui.lbl_status.setText("")
            return
        self.ui.stacked.setCurrentIndex(1)
        self.ui.lbl_status.setText(f"Всего задач: {len(self._tasks)}")
        for row, task in enumerate(self._tasks):
            done_text = "Да" if task["is_done"] else "Нет"
            status_item = QTableWidgetItem(done_text)
            status_item.setTextAlignment(Qt.AlignCenter)
            self.ui.table.setItem(row, 0, status_item)

            self.ui.table.setItem(row, 1, QTableWidgetItem(task["title"]))
            self.ui.table.setItem(row, 2, QTableWidgetItem(task["description"] or ""))
            self.ui.table.setItem(row, 3, QTableWidgetItem(task["due_date"] or ""))

            priority_item = QTableWidgetItem(str(task["priority"] or ""))
            priority_item.setTextAlignment(Qt.AlignCenter)
            self.ui.table.setItem(row, 4, priority_item)

            self.ui.table.setItem(row, 5, QTableWidgetItem(task["task_type"] or ""))

    def _get_selected_task(self):
        row = self.ui.table.currentRow()
        print(row)
        print(len(self._tasks))
        if row < 0 or row >= len(self._tasks):
            QMessageBox.warning(self, "Предупреждение", "Сначала выберите задачу в списке.")
            return None
        return self._tasks[row]

    def delete_task(self):
        task = self._get_selected_task()
        if not task:
            return
        confirm = QMessageBox.question(
            self,
            "Удаление задачи",
            f'Удалить задачу "{task["title"]}"?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if confirm == QMessageBox.StandardButton.Yes:
            self.db.delete_task(task["id"])
            self._refresh_table()

    def edit_task(self):
        task = self._get_selected_task()
        if not task:
            return
        dialog = TaskEditorDialog(self, task_data=task)
        if dialog.exec():
            data = dialog.get_data()
            self.db.update_task(
                task_id=task["id"],
                title=data["title"],
                description=data["description"],
                due_date=data["due_date"],
                priority=data["priority"],
                task_type=data["task_type"],
                is_done=task["is_done"]
            )
        self._refresh_table()
