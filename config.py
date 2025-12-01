LIGHT_THEME = """
QMainWindow, QWidget {
    background-color: #ffffff;
    color: #1f2933;
}
QTableWidget {
    background-color: #ffffff;
    alternate-background-color: #f5f5f5;
    gridline-color: #d1d5db;
}
QHeaderView::section {
    background-color: #e5e7eb;
    color: #1f2933;
    padding: 4px;
    border: none;
}
"""

DARK_THEME = """
QMainWindow, QWidget {
    background-color: #1f2933;
    color: #e5e7eb;
}
QLineEdit, QTextEdit, QComboBox, QDateEdit {
    background-color: #111827;
    color: #e5e7eb;
    border: 1px solid #374151;
}
QTableWidget {
    background-color: #111827;
    alternate-background-color: #1f2933;
    gridline-color: #374151;
    color: #e5e7eb;
}
QHeaderView::section {
    background-color: #374151;
    color: #f9fafb;
    padding: 4px;
    border: none;
}
QPushButton {
    background-color: #2563eb;
    color: #ffffff;
    border: none;
    padding: 6px 12px;
}
QPushButton:hover {
    background-color: #1d4ed8;
}
"""