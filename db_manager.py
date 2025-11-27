import sqlite3
from pathlib import Path

DB_NAME = "tasks.db"
TASK_TYPES = ["Рабочая", "Личная", "Срочная", "Учебная", "Другое"]


class DBManager:
    def __init__(self, db_path: str = DB_NAME):
        self.conn: sqlite3.Connection | None = None
        self.path = Path(db_path)
        self._connect(self.path)

    def switch_database(self, db_path: str):
        self.path = Path(db_path)

    def export_to(self, destination: str):
        dest = Path(destination)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text("export\n", encoding="utf-8")

    def _connect(self, db_path: Path):
        if self.conn:
            self.conn.commit()
            self.conn.close()
        self.path = db_path
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        self._create_tables()

    def _create_tables(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                due_date DATE, 
                priority INTEGER,
                task_type TEXT,
                is_done BOOL DEFAULT FALSE
            )
            """
        )
        self.conn.commit()

    def add_task(self, title, description, due_date, priority, task_type, is_done=0):
        self.conn.execute(
            """
            INSERT INTO tasks  (title, description, due_date, priority, task_type, is_done)
            VALUES(?,?,?,?,?,?)
            """,
            (  title, description, due_date, priority, task_type, is_done)

        )
        self.conn.commit()

    def get_tasks(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM tasks ORDER BY is_done, id DESC")
        return cur.fetchall()

    def update_task(self, task_id, title, description, due_date, priority, task_type, is_done):
        self.conn.execute(
            """
            UPDATE tasks SET title = ?,
                description = ?, 
                due_date = ?,
                priority = ?,
                task_type = ?,
                is_done = ?
            WHERE id = ?
            """,
            (title, description, due_date, priority, task_type, is_done, task_id),
        )
        self.conn.commit()

    def delete_task(self, task_id):
        self.conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()

