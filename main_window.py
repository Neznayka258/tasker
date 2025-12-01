from PySide6.QtCore import Qt
from PySide6.QtGui import QActionGroup
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
)

from config import DARK_THEME, LIGHT_THEME
from db_manager import DBManager
from main_window_ui import Ui_MainWindow
from task_dialog import TaskEditorDialog



MESSAGE_TEXT = "Функция пока не реализована"


class TaskManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._current_theme = "light"
        self.db = DBManager()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._tasks: list[dict] = []
        self._updating_table = False
        self.ui.table.setColumnHidden(6, True)
        self._connect_buttons()
        self._connect_actions()
        self.ui.table.itemChanged.connect(self._handle_status_change)
        self._refresh_table()
        self._theme_group = QActionGroup(self)
        self._theme_group.setExclusive(True)

    def _connect_buttons(self):
        self.ui.btn_add.clicked.connect(self.show_dialog)
        self.ui.btn_edit.clicked.connect(self.edit_task)
        self.ui.btn_delete.clicked.connect(self.delete_task)
        self.ui.btn_done.clicked.connect(self._is_done_change)
        for button in [self.ui.btn_prev, self.ui.btn_next]:
            button.clicked.connect(self.show_message)
        self.ui.edit_search.textChanged.connect(lambda _: self.show_message())

    def _connect_actions(self):
        if not hasattr(self, "_theme_group"):
            self._theme_group = QActionGroup(self)
            self._theme_group.setExclusive(True)
        action_map = [
            ("actionNew", self.show_message),
            ("actionOpen", self.show_message),
            ("actionSave", self.show_message),
            ("actionExit", self.close),
            ("actionAddTask", self.show_dialog),
            ("actionEdit", self.edit_task),
            ("actionDelete", self.delete_task),
            ("actionDone", self._is_done_change),
            ("actionAll", self.show_message),
            ("actionDoneOnly", self.show_message),
            ("actionUndone", self.show_message),
            ("actionFilterDate", self.show_message),
            ("actionFilterType", self.show_message),
            ("actionThemeLight", self._set_light_theme),
            ("actionThemeDark", self._set_dark_theme),
        ]
        for name, slot in action_map:
            action = getattr(self.ui, name, None)
            if action is not None and slot is not None:
                if name in ("actionThemeLight", "actionThemeDark"):
                    action.setCheckable(True)
                    if action not in self._theme_group.actions():
                        self._theme_group.addAction(action)
                action.triggered.connect(slot)

    def show_dialog(self):
        dialog = TaskEditorDialog(self)
        if dialog.exec():
            data = dialog.get_data()
            if not data["title"]:
                QMessageBox.warning(self, "Ошибка", "Название не может быть пустым.")
                return
            self.db.add_task(
                title=data["title"],
                description=data["description"],
                due_date=data["due_date"],
                priority=data["priority"],
                task_type=data["task_type"],
            )
            self._refresh_table()

    def _refresh_table(self):
        self._tasks = [dict(task) for task in self.db.get_tasks()]
        self._updating_table = True
        tasks = self._tasks
        self.ui.table.setRowCount(len(tasks))
        if not tasks:
            self.ui.stacked.setCurrentIndex(0)
            self.ui.lbl_status.setText("")
            self.ui.table.clearSelection()
            self._updating_table = False
            return
        self.ui.stacked.setCurrentIndex(1)
        self.ui.lbl_status.setText(f"Всего задач: {len(tasks)}")
        for row, task in enumerate(tasks):
            status_item = QTableWidgetItem("")
            status_item.setFlags(
                Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
            )
            status_item.setCheckState(Qt.Checked if task["is_done"] else Qt.Unchecked)
            status_item.setTextAlignment(Qt.AlignCenter)
            self.ui.table.setItem(row, 0, status_item)

            self.ui.table.setItem(row, 1, QTableWidgetItem(task["title"]))
            self.ui.table.setItem(row, 2, QTableWidgetItem(task["description"] or ""))
            self.ui.table.setItem(row, 3, QTableWidgetItem(task["due_date"] or ""))

            priority_item = QTableWidgetItem(str(task["priority"] or ""))
            priority_item.setTextAlignment(Qt.AlignCenter)
            self.ui.table.setItem(row, 4, priority_item)

            self.ui.table.setItem(row, 5, QTableWidgetItem(task["task_type"] or ""))
        self._updating_table = False

    def _get_selected_task(self):
        row = self.ui.table.currentRow()
        if row < 0 or row >= len(self._tasks):
            QMessageBox.warning(self, "Предупреждение", "Сначала выберите задачу в списке.")
            return None
        return self._tasks[row]

    def _get_task_by_row(self, row: int):
        if row < 0 or row >= len(self._tasks):
            return None
        return self._tasks[row]

    def _handle_status_change(self, item: QTableWidgetItem):
        if self._updating_table or item.column() != 0:
            return
        task = self._get_task_by_row(item.row())
        if not task:
            return
        is_done = item.checkState() == Qt.Checked
        self.db.set_task_done(task["id"], is_done)
        task["is_done"] = int(is_done)
        self.ui.lbl_status.setText(f"Всего задач: {len(self._tasks)}")

    def _is_done_change(self, *_):
        task = self._get_selected_task()
        if not task:
            return
        row = self.ui.table.currentRow()
        status_item = self.ui.table.item(row, 0)
        if status_item is None:
            return
        next_state = (
            Qt.Unchecked if status_item.checkState() == Qt.Checked else Qt.Checked
        )
        status_item.setCheckState(next_state)

    def edit_task(self):
        task = self._get_selected_task()
        if not task:
            return
        dialog = TaskEditorDialog(self, task_data=task)
        if dialog.exec():
            data = dialog.get_data()
            if not data["title"]:
                QMessageBox.warning(self, "Ошибка", "Название не может быть пустым.")
                return
            self.db.update_task(
                task_id=task["id"],
                title=data["title"],
                description=data["description"],
                due_date=data["due_date"],
                priority=data["priority"],
                task_type=data["task_type"],
            )
            self._refresh_table()

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

    def show_message(self, *_):
        QMessageBox.information(self, "Информация", MESSAGE_TEXT)

    def _apply_theme(self, theme: str):
        if theme == "dark":
            self.setStyleSheet(DARK_THEME)
        else:
            self.setStyleSheet(LIGHT_THEME)
        self._current_theme = theme
        action_light = getattr(self.ui, "actionThemeLight", None)
        action_dark = getattr(self.ui, "actionThemeDark", None)
        if action_light:
            action_light.setChecked(theme == "light")
        if action_dark:
            action_dark.setChecked(theme == "dark")

    def _set_light_theme(self, *_):
        if self._current_theme != "light":
            self._apply_theme("light")

    def _set_dark_theme(self, *_):
        if self._current_theme != "dark":
            self._apply_theme("dark")