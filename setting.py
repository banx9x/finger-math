# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QCheckBox, QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
                               QLabel)

from customqspinbox import CustomQSpinBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.NonModal)
        Dialog.resize(469, 171)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(u"QFrame {\n"
"	border: 0;\n"
"}\n"
"\n"
"QSpinBox {\n"
"	min-width: 60px;\n"
"}")
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.settings = QFrame(Dialog)
        self.settings.setObjectName(u"settings")
        self.settings.setFrameShape(QFrame.StyledPanel)
        self.settings.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.settings)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.operatorsFrame = QFrame(self.settings)
        self.operatorsFrame.setObjectName(u"operatorsFrame")
        self.operatorsFrame.setFrameShape(QFrame.StyledPanel)
        self.operatorsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.operatorsFrame)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.operatorsLabel = QLabel(self.operatorsFrame)
        self.operatorsLabel.setObjectName(u"operatorsLabel")

        self.horizontalLayout_5.addWidget(self.operatorsLabel)

        self.add = QCheckBox(self.operatorsFrame)
        self.add.setObjectName(u"add")
        self.add.setEnabled(True)
        self.add.setChecked(True)

        self.horizontalLayout_5.addWidget(self.add)

        self.sub = QCheckBox(self.operatorsFrame)
        self.sub.setObjectName(u"sub")
        self.sub.setChecked(False)
        self.sub.setTristate(False)

        self.horizontalLayout_5.addWidget(self.sub)

        self.mul = QCheckBox(self.operatorsFrame)
        self.mul.setObjectName(u"mul")
        self.mul.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.mul)

        self.div = QCheckBox(self.operatorsFrame)
        self.div.setObjectName(u"div")
        self.div.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.div)

        self.group = QCheckBox(self.operatorsFrame)
        self.group.setObjectName(u"group")
        self.group.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.group)


        self.gridLayout_2.addWidget(self.operatorsFrame, 1, 0, 1, 3, Qt.AlignRight)

        self.soundFrame = QFrame(self.settings)
        self.soundFrame.setObjectName(u"soundFrame")
        self.soundFrame.setFrameShape(QFrame.StyledPanel)
        self.soundFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.soundFrame)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.enableSound = QCheckBox(self.soundFrame)
        self.enableSound.setObjectName(u"enableSound")
        self.enableSound.setChecked(False)

        self.horizontalLayout_6.addWidget(self.enableSound)


        self.gridLayout_2.addWidget(self.soundFrame, 4, 1, 1, 2, Qt.AlignRight)

        self.minOperandFrame = QFrame(self.settings)
        self.minOperandFrame.setObjectName(u"minOperandFrame")
        self.minOperandFrame.setFrameShape(QFrame.StyledPanel)
        self.minOperandFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.minOperandFrame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minOperandLabel = QLabel(self.minOperandFrame)
        self.minOperandLabel.setObjectName(u"minOperandLabel")

        self.horizontalLayout_2.addWidget(self.minOperandLabel)

        self.minOperand = CustomQSpinBox(self.minOperandFrame)
        self.minOperand.setObjectName(u"minOperand")
        self.minOperand.setMinimum(1)
        self.minOperand.setMaximum(999)
        self.minOperand.setValue(1)

        self.horizontalLayout_2.addWidget(self.minOperand)


        self.gridLayout_2.addWidget(self.minOperandFrame, 0, 1, 1, 1)

        self.numOfOperandsFrame = QFrame(self.settings)
        self.numOfOperandsFrame.setObjectName(u"numOfOperandsFrame")
        self.numOfOperandsFrame.setFrameShape(QFrame.StyledPanel)
        self.numOfOperandsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.numOfOperandsFrame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.numOfOperandsLabel = QLabel(self.numOfOperandsFrame)
        self.numOfOperandsLabel.setObjectName(u"numOfOperandsLabel")

        self.horizontalLayout.addWidget(self.numOfOperandsLabel)

        self.numOfOperands = CustomQSpinBox(self.numOfOperandsFrame)
        self.numOfOperands.setObjectName(u"numOfOperands")
        self.numOfOperands.setMinimum(1)
        self.numOfOperands.setMaximum(99)
        self.numOfOperands.setValue(2)

        self.horizontalLayout.addWidget(self.numOfOperands)


        self.gridLayout_2.addWidget(self.numOfOperandsFrame, 0, 0, 1, 1)

        self.maxOperandFrame = QFrame(self.settings)
        self.maxOperandFrame.setObjectName(u"maxOperandFrame")
        self.maxOperandFrame.setFrameShape(QFrame.StyledPanel)
        self.maxOperandFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.maxOperandFrame)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.maxOperandLabel = QLabel(self.maxOperandFrame)
        self.maxOperandLabel.setObjectName(u"maxOperandLabel")

        self.horizontalLayout_3.addWidget(self.maxOperandLabel)

        self.maxOperand = CustomQSpinBox(self.maxOperandFrame)
        self.maxOperand.setObjectName(u"maxOperand")
        self.maxOperand.setMinimum(1)
        self.maxOperand.setMaximum(999)
        self.maxOperand.setValue(999)

        self.horizontalLayout_3.addWidget(self.maxOperand)


        self.gridLayout_2.addWidget(self.maxOperandFrame, 0, 2, 1, 1)

        self.otherOptionsFrame = QFrame(self.settings)
        self.otherOptionsFrame.setObjectName(u"otherOptionsFrame")
        self.otherOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.otherOptionsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.otherOptionsFrame)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.allowNegative = QCheckBox(self.otherOptionsFrame)
        self.allowNegative.setObjectName(u"allowNegative")
        self.allowNegative.setChecked(False)

        self.horizontalLayout_4.addWidget(self.allowNegative)


        self.gridLayout_2.addWidget(self.otherOptionsFrame, 2, 2, 1, 1, Qt.AlignRight)


        self.gridLayout.addWidget(self.settings, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"C\u00e0i \u0111\u1eb7t", None))
        self.operatorsLabel.setText(QCoreApplication.translate("Dialog", u"To\u00e1n t\u1eed", None))
        self.add.setText(QCoreApplication.translate("Dialog", u"C\u1ed9ng", None))
        self.sub.setText(QCoreApplication.translate("Dialog", u"Tr\u1eeb", None))
        self.mul.setText(QCoreApplication.translate("Dialog", u"Nh\u00e2n", None))
        self.div.setText(QCoreApplication.translate("Dialog", u"Chia", None))
#if QT_CONFIG(tooltip)
        self.group.setToolTip(QCoreApplication.translate("Dialog", u"Bao g\u1ed3m d\u1ea5u ngo\u1eb7c tr\u00f2n ()", None))
#endif // QT_CONFIG(tooltip)
        self.group.setText(QCoreApplication.translate("Dialog", u"Nh\u00f3m", None))
#if QT_CONFIG(tooltip)
        self.enableSound.setToolTip(QCoreApplication.translate("Dialog", u"\u00c2m b\u00e1o ch\u00ednh x\u00e1c ho\u1eb7c kh\u00f4ng", None))
#endif // QT_CONFIG(tooltip)
        self.enableSound.setText(QCoreApplication.translate("Dialog", u"B\u1eadt \u00e2m thanh", None))
        self.minOperandLabel.setText(QCoreApplication.translate("Dialog", u"S\u1ed1 nh\u1ecf nh\u1ea5t", None))
#if QT_CONFIG(tooltip)
        self.minOperand.setToolTip(QCoreApplication.translate("Dialog", u"S\u1ed1 nh\u1ecf nh\u1ea5t xu\u1ea5t hi\u1ec7n trong bi\u1ec3u th\u1ee9c", None))
#endif // QT_CONFIG(tooltip)
        self.numOfOperandsLabel.setText(QCoreApplication.translate("Dialog", u"S\u1ed1 to\u00e1n h\u1ea1ng", None))
        self.maxOperandLabel.setText(QCoreApplication.translate("Dialog", u"S\u1ed1 l\u1edbn nh\u1ea5t", None))
#if QT_CONFIG(tooltip)
        self.maxOperand.setToolTip(QCoreApplication.translate("Dialog", u"S\u1ed1 l\u1edbn nh\u1ea5t xu\u1ea5t hi\u1ec7n trong bi\u1ec3u th\u1ee9c", None))
#endif // QT_CONFIG(tooltip)
        self.maxOperand.setSuffix("")
#if QT_CONFIG(tooltip)
        self.allowNegative.setToolTip(QCoreApplication.translate("Dialog", u"K\u1ebft qu\u1ea3 c\u1ee7a m\u1ed9t ph\u00e9p t\u00ednh ho\u1eb7c c\u1ee7a c\u1ea3 bi\u1ec3u th\u1ee9c c\u00f3 th\u1ec3 \u00e2m, m\u1eb7c \u0111\u1ecbnh l\u00e0 t\u1eaft, \u0111\u1ea3m b\u1ea3o t\u1ea5t c\u1ea3 c\u00e1c ph\u00e9p t\u00ednh v\u00e0 k\u1ebft qu\u1ea3 cu\u1ed1i c\u00f9ng c\u1ee7a bi\u1ec3u th\u1ee9c lu\u00f4n d\u01b0\u01a1ng", None))
#endif // QT_CONFIG(tooltip)
        self.allowNegative.setText(QCoreApplication.translate("Dialog", u"Ph\u00e9p t\u00ednh c\u00f3 s\u1ed1 \u00e2m", None))
    # retranslateUi

