from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QSpinBox
from PySide6.QtGui import QKeyEvent


class CustomQSpinBox(QSpinBox):
    answer_changed = Signal(bool)

    def __init__(self, parent):
        super().__init__(parent)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.clear()
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        accept_keys = (Qt.Key.Key_Backspace,
                       Qt.Key.Key_Minus,
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
                       Qt.Key.Key_Right
                       )

        if event.key() in accept_keys:
            super().keyPressEvent(event)

            if event.key() != Qt.Key.Key_Backspace:
                self.setValue(int(self.value()))

            self.answer_changed.emit(self.is_not_empty())

    def is_not_empty(self):
        return len(self.text()) > 0

