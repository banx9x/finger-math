# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from customqspinbox import CustomQSpinBox
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(870, 463)
        MainWindow.setMinimumSize(QSize(870, 463))
        MainWindow.setStyleSheet(u"QFrame {\n"
"	border: 0;\n"
"}\n"
"\n"
"QLabel#numOfCorrect, QLabel#numOfIncorrect {\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLabel#expression {\n"
"	font-family: \"Sunny Spells\";\n"
"	font-size: 60px;\n"
"}\n"
"\n"
"QLabel#equal {\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"QLabel#equal {\n"
"	font-size: 30px;\n"
"}\n"
"\n"
"QSpinBox#answer {\n"
"	font-family: \"Sunny Spells\";\n"
"	height: 50px;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	border: 0;\n"
"	font-size: 36px;\n"
"}\n"
"\n"
"QPushButton#btnCheck {\n"
"	width: 100px;\n"
"	height: 50px;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	text-transform: uppercase;\n"
"}\n"
"QLabel#message {\n"
"	font-size: 32px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.correctLabel = QLabel(self.header)
        self.correctLabel.setObjectName(u"correctLabel")

        self.horizontalLayout_2.addWidget(self.correctLabel)

        self.numOfCorrect = QLabel(self.header)
        self.numOfCorrect.setObjectName(u"numOfCorrect")

        self.horizontalLayout_2.addWidget(self.numOfCorrect)

        self.incorrectLabel = QLabel(self.header)
        self.incorrectLabel.setObjectName(u"incorrectLabel")

        self.horizontalLayout_2.addWidget(self.incorrectLabel)

        self.numOfIncorrect = QLabel(self.header)
        self.numOfIncorrect.setObjectName(u"numOfIncorrect")

        self.horizontalLayout_2.addWidget(self.numOfIncorrect)

        self.btnHistory = QPushButton(self.header)
        self.btnHistory.setObjectName(u"btnHistory")

        self.horizontalLayout_2.addWidget(self.btnHistory)

        self.btnSetting = QPushButton(self.header)
        self.btnSetting.setObjectName(u"btnSetting")

        self.horizontalLayout_2.addWidget(self.btnSetting)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignRight)

        self.board = QFrame(self.centralwidget)
        self.board.setObjectName(u"board")
        self.board.setFrameShape(QFrame.StyledPanel)
        self.board.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.board)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.expression = QLabel(self.board)
        self.expression.setObjectName(u"expression")
        self.expression.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.expression)

        self.container = QFrame(self.board)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.container.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.container)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacerLeft = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacerLeft)

        self.inner = QFrame(self.container)
        self.inner.setObjectName(u"inner")
        self.inner.setFrameShape(QFrame.StyledPanel)
        self.inner.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.inner)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.answer = CustomQSpinBox(self.inner)
        self.answer.setObjectName(u"answer")
        self.answer.setMinimumSize(QSize(150, 0))
        self.answer.setMaximumSize(QSize(150, 16777215))
        self.answer.setMinimum(0)
        self.answer.setMaximum(9999)

        self.verticalLayout_4.addWidget(self.answer)

        self.btnCheck = QPushButton(self.inner)
        self.btnCheck.setObjectName(u"btnCheck")
        self.btnCheck.setEnabled(False)
        self.btnCheck.setCheckable(False)
        self.btnCheck.setFlat(False)

        self.verticalLayout_4.addWidget(self.btnCheck)


        self.horizontalLayout.addWidget(self.inner)

        self.horizontalSpacerRight = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacerRight)


        self.verticalLayout_2.addWidget(self.container)


        self.verticalLayout.addWidget(self.board, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btnCheck.clicked.connect(MainWindow.handle_click)
        self.answer.answer_changed.connect(self.btnCheck.setEnabled)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kid Learn Finger Math", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.correctLabel.setText(QCoreApplication.translate("MainWindow", u"\u0110\u00fang", None))
        self.numOfCorrect.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.incorrectLabel.setText(QCoreApplication.translate("MainWindow", u"Sai", None))
        self.numOfIncorrect.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnHistory.setText(QCoreApplication.translate("MainWindow", u"L\u1ecbch s\u1eed", None))
        self.btnSetting.setText(QCoreApplication.translate("MainWindow", u"C\u00e0i \u0111\u1eb7t", None))
        self.expression.setText(QCoreApplication.translate("MainWindow", u"1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = ?", None))
        self.answer.setSpecialValueText("")
        self.answer.setPrefix("")
        self.btnCheck.setText(QCoreApplication.translate("MainWindow", u"KI\u1ec2M TRA", None))
    # retranslateUi

