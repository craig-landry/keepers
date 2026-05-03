from PySide6.QtCore import QObject

class BaseController(QObject):
    def __init__(self, signals, service=None, parent=None):
        super().__init__(parent)
        self._signals = signals
        self._service = service
