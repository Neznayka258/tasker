# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_TaskDialog(object):
    def setupUi(self, TaskDialog):
        if not TaskDialog.objectName():
            TaskDialog.setObjectName(u"TaskDialog")
        TaskDialog.resize(420, 320)
        self.verticalLayout = QVBoxLayout(TaskDialog)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)
        self.label_title = QLabel(TaskDialog)
        self.label_title.setObjectName(u"label_title")

        self.verticalLayout.addWidget(self.label_title)

        self.edit_title = QLineEdit(TaskDialog)
        self.edit_title.setObjectName(u"edit_title")

        self.verticalLayout.addWidget(self.edit_title)

        self.label_desc = QLabel(TaskDialog)
        self.label_desc.setObjectName(u"label_desc")

        self.verticalLayout.addWidget(self.label_desc)

        self.edit_desc = QTextEdit(TaskDialog)
        self.edit_desc.setObjectName(u"edit_desc")

        self.verticalLayout.addWidget(self.edit_desc)

        self.dates_layout = QHBoxLayout()
        self.dates_layout.setSpacing(12)
        self.dates_layout.setObjectName(u"dates_layout")
        self.date_col = QVBoxLayout()
        self.date_col.setObjectName(u"date_col")
        self.label_date = QLabel(TaskDialog)
        self.label_date.setObjectName(u"label_date")

        self.date_col.addWidget(self.label_date)

        self.edit_date = QDateEdit(TaskDialog)
        self.edit_date.setObjectName(u"edit_date")
        self.edit_date.setCalendarPopup(True)

        self.date_col.addWidget(self.edit_date)


        self.dates_layout.addLayout(self.date_col)

        self.priority_col = QVBoxLayout()
        self.priority_col.setObjectName(u"priority_col")
        self.label_prio = QLabel(TaskDialog)
        self.label_prio.setObjectName(u"label_prio")

        self.priority_col.addWidget(self.label_prio)

        self.combo_prio = QComboBox(TaskDialog)
        self.combo_prio.addItem("")
        self.combo_prio.addItem("")
        self.combo_prio.addItem("")
        self.combo_prio.setObjectName(u"combo_prio")

        self.priority_col.addWidget(self.combo_prio)


        self.dates_layout.addLayout(self.priority_col)


        self.verticalLayout.addLayout(self.dates_layout)

        self.label_type = QLabel(TaskDialog)
        self.label_type.setObjectName(u"label_type")

        self.verticalLayout.addWidget(self.label_type)

        self.combo_type = QComboBox(TaskDialog)
        self.combo_type.setObjectName(u"combo_type")

        self.verticalLayout.addWidget(self.combo_type)

        self.buttonBox = QDialogButtonBox(TaskDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(TaskDialog)
        self.buttonBox.accepted.connect(TaskDialog.accept)
        self.buttonBox.rejected.connect(TaskDialog.reject)

        QMetaObject.connectSlotsByName(TaskDialog)
    # setupUi

    def retranslateUi(self, TaskDialog):
        TaskDialog.setWindowTitle(QCoreApplication.translate("TaskDialog", u"\u0417\u0430\u0434\u0430\u0447\u0430", None))
        self.label_title.setText(QCoreApplication.translate("TaskDialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.edit_title.setPlaceholderText(QCoreApplication.translate("TaskDialog", u"\u041a\u043e\u0440\u043e\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.label_desc.setText(QCoreApplication.translate("TaskDialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.edit_desc.setPlaceholderText(QCoreApplication.translate("TaskDialog", u"\u0414\u0435\u0442\u0430\u043b\u0438, \u0437\u0430\u043c\u0435\u0442\u043a\u0438, \u0448\u0430\u0433\u0438...", None))
        self.label_date.setText(QCoreApplication.translate("TaskDialog", u"\u0414\u0430\u0442\u0430 (\u0434\u0434.\u043c\u043c.\u0433\u0433\u0433\u0433):", None))
        self.edit_date.setDisplayFormat(QCoreApplication.translate("TaskDialog", u"dd.MM.yyyy", None))
        self.label_prio.setText(QCoreApplication.translate("TaskDialog", u"\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442:", None))
        self.combo_prio.setItemText(0, QCoreApplication.translate("TaskDialog", u"1 \u2014 \u043d\u0438\u0437\u043a\u0438\u0439", None))
        self.combo_prio.setItemText(1, QCoreApplication.translate("TaskDialog", u"2 \u2014 \u0441\u0440\u0435\u0434\u043d\u0438\u0439", None))
        self.combo_prio.setItemText(2, QCoreApplication.translate("TaskDialog", u"3 \u2014 \u0432\u044b\u0441\u043e\u043a\u0438\u0439", None))

        self.label_type.setText(QCoreApplication.translate("TaskDialog", u"\u0422\u0438\u043f \u0437\u0430\u0434\u0430\u0447\u0438:", None))    # retranslateUi

