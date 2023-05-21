import os
from typing import Tuple

from PySide6.QtCore import Qt, Slot, QUrl, Signal
from PySide6.QtGui import QIcon, QFontDatabase, QKeyEvent
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView

from history_dialog import HistoryDialog
from interface import Ui_MainWindow
from lib.generate import Operator, generator
from setting_dialog import SettingDialog

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    app_id = 'banx.kidlearnfingermath'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
except ImportError:
    pass


class Window(QMainWindow, Ui_MainWindow):
    _expr = None
    _checked = False
    _num_of_operands = 2
    _min_operand = 1
    _max_operand = 9
    _operators = {Operator.ADD: True,
                  Operator.SUB: False,
                  Operator.MUL: False,
                  Operator.DIV: False,
                  Operator.GROUP: False}
    _allow_negative = False
    _enable_sound = True
    _correct = 0
    _incorrect = 0
    _history = []

    MESSAGE = "Kết quả bằng bao nhiêu nhỉ?"
    CORRECT_MESSAGE = "Chính xác!!!"
    INCORRECT_MESSAGE = "Chưa chính xác!!! Đáp án đúng là {}"
    BUTTON_LABEL = "Kiểm tra"
    BUTTON_CHECKED_LABEL = "Tiếp tục"

    settings_changed = Signal(Tuple[int, int, int])
    expression_changed = Signal()

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.expression.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.answer.returnPressed.connect(self.check_result)

        self.correct_sound = QSoundEffect()
        self.correct_sound.setSource(QUrl.fromLocalFile(os.path.join(basedir, u"assets/sounds/correct.wav")))

        self.incorrect_sound = QSoundEffect()
        self.incorrect_sound.setSource(QUrl.fromLocalFile(os.path.join(basedir, u"assets/sounds/incorrect.wav")))

        self.change_expression()

    @property
    def expr(self):
        return self._expr

    @expr.setter
    def expr(self, expression):
        self._expr = expression
        self.expression_changed.emit()

    @property
    def checked(self):
        return self._checked

    @checked.setter
    def checked(self, value):
        self._checked = value

    @property
    def num_of_operands(self):
        return self._num_of_operands

    @num_of_operands.setter
    def num_of_operands(self, value):
        self._num_of_operands = value

    @property
    def min_operand(self):
        return self._min_operand

    @min_operand.setter
    def min_operand(self, value):
        self._min_operand = value

    @property
    def max_operand(self):
        return self._max_operand

    @max_operand.setter
    def max_operand(self, value):
        self._max_operand = value

    @property
    def operators(self):
        return self._operators

    @operators.setter
    def operators(self, value):
        self._operators = value

    @property
    def allow_negative(self):
        return self._allow_negative

    @allow_negative.setter
    def allow_negative(self, value):
        self._allow_negative = value
        self.answer.set_allow_negative(self.allow_negative)

    @property
    def enable_sound(self):
        return self._enable_sound

    @enable_sound.setter
    def enable_sound(self, value):
        self._enable_sound = value

    @property
    def correct(self):
        return self._correct

    @correct.setter
    def correct(self, value):
        self._correct = value

    @property
    def incorrect(self):
        return self._incorrect

    @incorrect.setter
    def incorrect(self, value):
        self._incorrect = value

    @Slot()
    def handle_expression_changed(self):
        self.expression.setText(f"{self.expr} = ??")
        self.checked = False

        self.answer.setPrefix("")
        self.answer.clear()
        self.answer.setEnabled(True)
        self.answer.setFocus()

        self.btnCheck.setEnabled(False)
        self.btnCheck.setText(self.BUTTON_LABEL)

    @Slot()
    def handle_settings_changed(self):
        self.change_expression()

    @Slot()
    def change_expression(self):
        operators = [op for op, enable in self.operators.items() if enable]
        self.expr = generator(operators,
                              self.num_of_operands,
                              self.min_operand,
                              self.max_operand,
                              self.allow_negative)

    @Slot()
    def check_result(self):
        answer = self.answer.get_value()

        if answer is None:
            return

        result = eval(self.expr)
        is_correct = answer == result

        self._history.append((self.expr, answer, result))

        if is_correct:
            self.correct += 1
        else:
            self.incorrect += 1

        self.numOfCorrect.setText(str(self.correct))
        self.numOfIncorrect.setText(str(self.incorrect))

        if self.enable_sound:
            if is_correct:
                self.correct_sound.play()
            else:
                self.incorrect_sound.play()

        self.expression.setText(f"{self.expr} = {result}")
        self.answer.setEnabled(False)
        self.checked = True
        self.btnCheck.setText(self.BUTTON_CHECKED_LABEL)

    @Slot()
    def handle_click(self):
        self.change_expression() if self.checked else self.check_result()

    @Slot()
    def show_history_dialog(self):
        dialog = HistoryDialog()
        dialog.historyTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        dialog.historyTable.setColumnWidth(0, 300)
        dialog.historyTable.setRowCount(len(self._history))

        for row, item in enumerate(self._history):
            expr, answer, result = item

            dialog.historyTable.setItem(row, 0, QTableWidgetItem(expr))
            dialog.historyTable.setItem(row, 1, QTableWidgetItem(str(answer)))
            dialog.historyTable.setItem(row, 2, QTableWidgetItem(str(result)))

        dialog.exec()

    @Slot()
    def show_setting_dialog(self):
        dialog = SettingDialog()
        dialog.setFocus()
        dialog.set_values(self.num_of_operands, self.min_operand, self.max_operand, self.operators, self.allow_negative, self.enable_sound)
        dialog.settings_changed.connect(self.change_settings)
        dialog.exec()

    @Slot(dict)
    def change_settings(self, values):
        self.num_of_operands = values["num_of_operands"]
        self.min_operand = values["min_operand"]
        self.max_operand = values["max_operand"]
        self.operators = values["operators"]
        self.allow_negative = values["allow_negative"]
        self.enable_sound = values["enable_sound"]

        self.settings_changed.emit()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Return and self.checked:
            self.change_expression()


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir, u"assets/calculator.ico")))

    QFontDatabase.addApplicationFont(u":/fonts/assets/fonts/SunnyspellsRegular.otf")

    window = Window()
    window.show()

    sys.exit(app.exec())
