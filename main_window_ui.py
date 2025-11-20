# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAddTask = QAction(MainWindow)
        self.actionAddTask.setObjectName(u"actionAddTask")
        self.actionEdit = QAction(MainWindow)
        self.actionEdit.setObjectName(u"actionEdit")
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionDone = QAction(MainWindow)
        self.actionDone.setObjectName(u"actionDone")
        self.actionAll = QAction(MainWindow)
        self.actionAll.setObjectName(u"actionAll")
        self.actionDoneOnly = QAction(MainWindow)
        self.actionDoneOnly.setObjectName(u"actionDoneOnly")
        self.actionUndone = QAction(MainWindow)
        self.actionUndone.setObjectName(u"actionUndone")
        self.actionThemeLight = QAction(MainWindow)
        self.actionThemeLight.setObjectName(u"actionThemeLight")
        self.actionThemeLight.setCheckable(True)
        self.actionThemeDark = QAction(MainWindow)
        self.actionThemeDark.setObjectName(u"actionThemeDark")
        self.actionThemeDark.setCheckable(True)
        self.actionFilterDate = QAction(MainWindow)
        self.actionFilterDate.setObjectName(u"actionFilterDate")
        self.actionFilterType = QAction(MainWindow)
        self.actionFilterType.setObjectName(u"actionFilterType")
        self.actionFilterUser = QAction(MainWindow)
        self.actionFilterUser.setObjectName(u"actionFilterUser")
        self.actionAddUser = QAction(MainWindow)
        self.actionAddUser.setObjectName(u"actionAddUser")
        self.actionSelectUser = QAction(MainWindow)
        self.actionSelectUser.setObjectName(u"actionSelectUser")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setSpacing(12)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(16, 16, 8, 8)
        self.top_layout = QHBoxLayout()
        self.top_layout.setSpacing(8)
        self.top_layout.setObjectName(u"top_layout")
        self.lbl_search = QLabel(self.centralwidget)
        self.lbl_search.setObjectName(u"lbl_search")

        self.top_layout.addWidget(self.lbl_search)

        self.edit_search = QLineEdit(self.centralwidget)
        self.edit_search.setObjectName(u"edit_search")

        self.top_layout.addWidget(self.edit_search)

        self.lbl_status = QLabel(self.centralwidget)
        self.lbl_status.setObjectName(u"lbl_status")
        self.lbl_status.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.top_layout.addWidget(self.lbl_status)


        self.main_layout.addLayout(self.top_layout)

        self.stacked = QStackedWidget(self.centralwidget)
        self.stacked.setObjectName(u"stacked")
        self.page_placeholder = QWidget()
        self.page_placeholder.setObjectName(u"page_placeholder")
        self.placeholderLayout = QVBoxLayout(self.page_placeholder)
        self.placeholderLayout.setObjectName(u"placeholderLayout")
        self.placeholderLayout.setContentsMargins(0, 40, 0, 0)
        self.lbl_ph = QLabel(self.page_placeholder)
        self.lbl_ph.setObjectName(u"lbl_ph")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_ph.setFont(font)
        self.lbl_ph.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.placeholderLayout.addWidget(self.lbl_ph)

        self.lbl_ph2 = QLabel(self.page_placeholder)
        self.lbl_ph2.setObjectName(u"lbl_ph2")
        self.lbl_ph2.setStyleSheet(u"color: #6b7280;")
        self.lbl_ph2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.placeholderLayout.addWidget(self.lbl_ph2)

        self.stacked.addWidget(self.page_placeholder)
        self.page_table = QWidget()
        self.page_table.setObjectName(u"page_table")
        self.tableLayout = QVBoxLayout(self.page_table)
        self.tableLayout.setObjectName(u"tableLayout")
        self.tableLayout.setContentsMargins(0, 0, 0, 0)
        self.table = QTableWidget(self.page_table)
        if (self.table.columnCount() < 7):
            self.table.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table.setObjectName(u"table")
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.table.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.table.setColumnCount(7)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)

        self.tableLayout.addWidget(self.table)

        self.stacked.addWidget(self.page_table)

        self.main_layout.addWidget(self.stacked)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setSpacing(8)
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.btn_prev = QPushButton(self.centralwidget)
        self.btn_prev.setObjectName(u"btn_prev")
        self.btn_prev.setMinimumWidth(36)

        self.bottom_layout.addWidget(self.btn_prev)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.bottom_layout.addItem(self.horizontalSpacer)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")

        self.bottom_layout.addWidget(self.btn_add)

        self.btn_edit = QPushButton(self.centralwidget)
        self.btn_edit.setObjectName(u"btn_edit")

        self.bottom_layout.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")

        self.bottom_layout.addWidget(self.btn_delete)

        self.btn_done = QPushButton(self.centralwidget)
        self.btn_done.setObjectName(u"btn_done")

        self.bottom_layout.addWidget(self.btn_done)

        self.btn_next = QPushButton(self.centralwidget)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setMinimumWidth(36)

        self.bottom_layout.addWidget(self.btn_next)


        self.main_layout.addLayout(self.bottom_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 37))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTasks = QMenu(self.menubar)
        self.menuTasks.setObjectName(u"menuTasks")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuTypeHere = QMenu(self.menubar)
        self.menuTypeHere.setObjectName(u"menuTypeHere")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTasks.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTypeHere.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTasks.addAction(self.actionAddTask)
        self.menuTasks.addAction(self.actionEdit)
        self.menuTasks.addAction(self.actionDelete)
        self.menuTasks.addAction(self.actionDone)
        self.menuView.addAction(self.actionAll)
        self.menuView.addAction(self.actionDoneOnly)
        self.menuView.addAction(self.actionUndone)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFilterDate)
        self.menuView.addAction(self.actionFilterType)
        self.menuView.addAction(self.actionFilterUser)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionThemeLight)
        self.menuView.addAction(self.actionThemeDark)
        self.menuTypeHere.addAction(self.actionAddUser)
        self.menuTypeHere.addAction(self.actionSelectUser)

        self.retranslateUi(MainWindow)

        self.stacked.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u0437\u0430\u0434\u0430\u0447", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.actionAddTask.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.actionEdit.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.actionDone.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u0442\u0438\u0442\u044c \u043a\u0430\u043a \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u0443\u044e", None))
        self.actionAll.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.actionDoneOnly.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0435", None))
        self.actionUndone.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0435", None))
        self.actionThemeLight.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f \u0442\u0435\u043c\u0430", None))
        self.actionThemeDark.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0451\u043c\u043d\u0430\u044f \u0442\u0435\u043c\u0430", None))
        self.actionFilterDate.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u043f\u043e \u0434\u0430\u0442\u0435", None))
        self.actionFilterType.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u043f\u043e \u0442\u0438\u043f\u0443 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.actionFilterUser.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440 \u043f\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e", None))
        self.actionAddUser.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.actionSelectUser.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.lbl_search.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a:", None))
        self.edit_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438...", None))
        self.lbl_status.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e: 0", None))
        self.lbl_ph.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447 \u043f\u043e\u043a\u0430 \u043d\u0435\u0442", None))
        self.lbl_ph2.setText("")
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0437\u0430\u0434\u0430\u0447\u0438", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None));
        self.btn_prev.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btn_done.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u0442\u0438\u0442\u044c \u043a\u0430\u043a \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u0443\u044e", None))
        self.btn_next.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menuTasks.setTitle(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434", None))
        self.menuTypeHere.setTitle(QCoreApplication.translate("MainWindow", u"Type Here", None))
    # retranslateUi

