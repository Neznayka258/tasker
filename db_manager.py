import sqlite3
from pathlib import Path

DB_NAME = "tasks.db"
TASK_TYPES = ["Рабочая", "Личная", "Срочная", "Учебная", "Другое"]


class DBManager:
    def __init__(self, db_path: str = DB_NAME):
        self.path = Path(db_path)


    def switch_database(self, db_path: str):
        self.path = Path(db_path)

    def export_to(self, destination: str):
        dest = Path(destination)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text("export\n", encoding="utf-8")

