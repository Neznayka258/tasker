from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QActionGroup
from PySide6.QtWidgets import (
    QApplication,
    QInputDialog,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
)

from config import DARK_THEME, LIGHT_THEME
from db_manager import DBManager, TASK_TYPES
from main_window_ui import Ui_MainWindow
from task_dialog import TaskEditorDialog

MESSAGE_TEXT = "Функция пока не реализована"


class TaskManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._status_group = QActionGroup(self)
        self._search_query = ""
        self._current_theme = "light"
        self._filter_status = "all"
        self._filter_task_type: str | None = None
        self.db = DBManager()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._tasks: list[dict] = []
        self._all_tasks: list[dict] = []
        self._updating_table = False
        self.ui.table.setColumnHidden(6, True)
        self._connect_buttons()
        self._connect_actions()
        self.ui.table.itemChanged.connect(self._handle_status_change)
        self._refresh_table()
        self._theme_group = QActionGroup(self)
        self._default_type_action_text = self.ui.actionFilterType.text()
        self._theme_group.setExclusive(True)



    def _connect_buttons(self):
        self.ui.btn_add.clicked.connect(self.show_dialog)
        self.ui.btn_edit.clicked.connect(self.edit_task)
        self.ui.btn_delete.clicked.connect(self.delete_task)
        self.ui.btn_done.clicked.connect(self._is_done_change)
        for button in [self.ui.btn_prev, self.ui.btn_next]:
            button.clicked.connect(self.show_message)
        self.ui.edit_search.setPlaceholderText("Поиск по названию или описанию")
        self.ui.edit_search.textChanged.connect(self._on_search_changed)

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
            ("actionAll", lambda *_: self._set_status_filter("all")),
            ("actionDoneOnly", lambda *_: self._set_status_filter("done")),
            ("actionUndone", lambda *_: self._set_status_filter("undone")),
            ("actionFilterDate", self.show_message),
            ("actionFilterType", self._set_type_filter),
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
                if name in ("actionAll", "actionDoneOnly", "actionUndone"):
                    action.setCheckable(True)
                    if action not in self._status_group.actions():
                        self._status_group.addAction(action)
                action.triggered.connect(slot)
        self._update_status_actions()

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
        self._all_tasks = [dict(task) for task in self.db.get_tasks()]
        self._tasks = self._apply_filters(self._all_tasks)
        self._updating_table = True
        tasks = self._tasks
        self.ui.table.setRowCount(len(tasks))
        if not tasks:
            self.ui.stacked.setCurrentIndex(0)
            total = len(self._all_tasks)
            if total and (
                    self._search_query
                    or self._filter_status != "all"
                    or self._filter_task_type
            ):
                self.ui.lbl_status.setText("Ничего не найдено по текущему фильтру")
            else:
                self.ui.lbl_status.setText("")
            self.ui.table.clearSelection()
            self._updating_table = False
            return
        self.ui.stacked.setCurrentIndex(1)
        self.ui.lbl_status.setText(
            f"Показано: {len(tasks)} из {len(self._all_tasks)}"
        )
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

    def _set_status_filter(self, status: str):
        if status == self._filter_status:
            return
        self._filter_status = status
        self._update_status_actions()
        self._refresh_table()

    def _update_status_actions(self):
        actions = {
            "all": getattr(self.ui, "actionAll", None),
            "done": getattr(self.ui, "actionDoneOnly", None),
            "undone": getattr(self.ui, "actionUndone", None)
        }
        for key, action in actions.items():
            if action:
                action.setChecked(self._filter_status == key)

    def _set_type_filter(self, *_):
        options = ["Все типы"] + TASK_TYPES
        current = self._filter_task_type or "Все типы"
        if current not in options:
            current = "Все типы"
        ind = options.index(current)
        choice, okay = QInputDialog.getItem(self,
                                            "Филтер по типу",
                                            "Выберите тип задачи",
                                            options, ind, False,)
        if not okay:
            return
        if choice == "Все типы":
            self._filter_task_type = None
        else:
            self._filter_task_type = choice


        if self._filter_task_type:
            self.ui.actionFilterType.setText(f"Тип: {self._filter_task_type}")
        else:
            self.ui.actionFilterType.setText(self._default_type_action_text)
        self._refresh_table()

    def _on_search_changed(self, text: str):
        self._search_query = text.strip()
        self._refresh_table()

    def _apply_filters(self, tasks: list[dict]) -> list[dict]:
        query = self._search_query.lower()
        filtered: list[dict] = []
        for task in tasks:
            if self._filter_status == "done" and not task["is_done"]:
                continue
            if self._filter_status == "undone" and task["is_done"]:
                continue
            if self._filter_task_type:
                task_type = (task.get("task_type") or "").strip()
                if task_type != self._filter_task_type:
                    continue
            if query:
                haystack = f"{task.get('title', '')} {task.get('description', '')}".lower()
                if query not in haystack:
                    continue
            filtered.append(task)
        return filtered