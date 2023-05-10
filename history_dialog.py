from PySide6.QtWidgets import QDialog

from history_ui import Ui_HistoryDialog


class HistoryDialog(QDialog, Ui_HistoryDialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
