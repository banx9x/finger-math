from PySide6.QtCore import Qt, Signal, QObject, QEvent
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QSpinBox


class CustomQSpinBox(QSpinBox):
    validated = Signal(bool)
    returnPressed = Signal()

    def __init__(self, parent):
        super().__init__(parent)

        self.allow_negative = False
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.clear()

    def set_allow_negative(self, value):
        self.allow_negative = value

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        return event.type() != event.Type.KeyPress
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        accept_keys = [Qt.Key.Key_Return,
                       Qt.Key.Key_Backspace,
                       Qt.Key.Key_0,
                       Qt.Key.Key_1,
                       Qt.Key.Key_2,
                       Qt.Key.Key_3,
                       Qt.Key.Key_4,
                       Qt.Key.Key_5,
                       Qt.Key.Key_6,
                       Qt.Key.Key_7,
                       Qt.Key.Key_8,
                       Qt.Key.Key_9,
                       Qt.Key.Key_Left,
                       Qt.Key.Key_Right]

        if self.allow_negative:
            accept_keys.append(Qt.Key.Key_Minus)

        if event.key() not in accept_keys:
            event.ignore()
            return

        if event.key() == Qt.Key.Key_Return:
            self.returnPressed.emit()
            return

        if event.key() == Qt.Key.Key_Minus:
            if self.prefix() == "":
                self.setPrefix("-")
            else:
                self.setPrefix("")

            if self.text() == "" or self.text() == "-":
                self.setValue(0)
                self.clear()

        elif event.key() == Qt.Key.Key_Backspace:
            if self.text() == "" or self.text() == "-":
                self.setPrefix("")
                self.clear()

            super().keyPressEvent(event)
        else:
            super().keyPressEvent(event)
            self.setValue(self.value())

        self.lineEdit().setCursorPosition(len(self.text()))

        value = self.text()

        self.validated.emit((len(value) > 0 and value[0] != "-") or len(value) > 1)

    def get_value(self):
        value = self.text()

        if value == "":
            return None
        else:
            return int(self.text())
