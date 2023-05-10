from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QDialog

from setting import Ui_Dialog
from lib.generate import Operator


class SettingDialog(QDialog, Ui_Dialog):
    settings_changed = Signal(dict)

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.maxOperand.valueChanged.connect(lambda val: self.minOperand.setMaximum(val - 1))
        self.accepted.connect(self.on_accepted)

    def set_values(self,
                   num_of_operands=3,
                   min_operand=1,
                   max_operand=9,
                   operators=None,
                   allow_negative=False,
                   result_sound=True):
        if operators is None:
            operators = {Operator.ADD: True,
                         Operator.SUB: False,
                         Operator.MUL: False,
                         Operator.DIV: False,
                         Operator.GROUP: False}

        self.numOfOperands.setValue(num_of_operands)
        self.minOperand.setValue(min_operand)
        self.maxOperand.setValue(max_operand)

        self.add.setChecked(operators[Operator.ADD])
        self.sub.setChecked(operators[Operator.SUB])
        self.mul.setChecked(operators[Operator.MUL])
        self.div.setChecked(operators[Operator.DIV])
        self.group.setChecked(operators[Operator.GROUP])

        self.allowNegative.setChecked(allow_negative)
        self.enableSound.setChecked(result_sound)

    @Slot()
    def on_accepted(self):
        num_of_operands = self.numOfOperands.value()
        min_operand = self.minOperand.value()
        max_operand = self.maxOperand.value()
        operators = {Operator.ADD: self.add.checkState() == Qt.CheckState.Checked,
                     Operator.SUB: self.sub.checkState() == Qt.CheckState.Checked,
                     Operator.MUL: self.mul.checkState() == Qt.CheckState.Checked,
                     Operator.DIV: self.div.checkState() == Qt.CheckState.Checked,
                     Operator.GROUP: self.group.checkState() == Qt.CheckState.Checked}
        allow_negative = self.allowNegative.checkState() == Qt.CheckState.Checked
        result_sound = self.enableSound.checkState() == Qt.CheckState.Checked

        settings = dict(num_of_operands=num_of_operands,
                        min_operand=min_operand,
                        max_operand=max_operand,
                        operators=operators,
                        allow_negative=allow_negative,
                        result_sound=result_sound)

        self.settings_changed.emit(settings)
