# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QFrame, QHBoxLayout, QHeaderView,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_HistoryDialog(object):
    def setupUi(self, HistoryDialog):
        if not HistoryDialog.objectName():
            HistoryDialog.setObjectName(u"HistoryDialog")
        HistoryDialog.resize(574, 356)
        HistoryDialog.setMinimumSize(QSize(574, 356))
        HistoryDialog.setMaximumSize(QSize(574, 356))
        self.verticalLayout = QVBoxLayout(HistoryDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Container = QFrame(HistoryDialog)
        self.Container.setObjectName(u"Container")
        self.Container.setFrameShape(QFrame.StyledPanel)
        self.Container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.historyTable = QTableWidget(self.Container)
        if (self.historyTable.columnCount() < 3):
            self.historyTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.historyTable.setObjectName(u"historyTable")
        self.historyTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.historyTable.setSelectionMode(QAbstractItemView.NoSelection)
        self.historyTable.setRowCount(0)
        self.historyTable.setColumnCount(3)
        self.historyTable.horizontalHeader().setCascadingSectionResizes(True)
        self.historyTable.horizontalHeader().setMinimumSectionSize(100)
        self.historyTable.verticalHeader().setVisible(False)

        self.horizontalLayout.addWidget(self.historyTable)


        self.verticalLayout.addWidget(self.Container)

        self.ButtonBox = QDialogButtonBox(HistoryDialog)
        self.ButtonBox.setObjectName(u"ButtonBox")
        self.ButtonBox.setOrientation(Qt.Horizontal)
        self.ButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.ButtonBox)


        self.retranslateUi(HistoryDialog)
        self.ButtonBox.accepted.connect(HistoryDialog.accept)
        self.ButtonBox.rejected.connect(HistoryDialog.reject)

        QMetaObject.connectSlotsByName(HistoryDialog)
    # setupUi

    def retranslateUi(self, HistoryDialog):
        HistoryDialog.setWindowTitle(QCoreApplication.translate("HistoryDialog", u"L\u1ecbch s\u1eed", None))
        ___qtablewidgetitem = self.historyTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("HistoryDialog", u"Bi\u1ec3u th\u1ee9c", None));
        ___qtablewidgetitem1 = self.historyTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("HistoryDialog", u"Tr\u1ea3 l\u1eddi", None));
        ___qtablewidgetitem2 = self.historyTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("HistoryDialog", u"\u0110\u00e1p \u00e1n", None));
    # retranslateUi

