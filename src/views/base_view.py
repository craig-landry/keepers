import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QFile

class BaseView(QWidget):
    def __init__(self, signals, parent=None):
        super().__init__(parent)
        self._signals = signals
        self._ui = None
        self._init_ui()
        self._connect_signals()

    def _init_ui(self):
        """Must be implemented by subclasses to load UI."""
        pass

    def _load_ui(self, ui_filename):
        loader = QUiLoader()
        ui_path = os.path.join(os.path.dirname(__file__), "..", "resources", "ui", ui_filename)
        file = QFile(ui_path)
        if not file.open(QFile.ReadOnly):
            raise IOError(f"Cannot open {ui_path}: {file.errorString()}")
        
        ui = loader.load(file, self)
        file.close()
        return ui

    def _connect_signals(self):
        """Connect UI signals to slots."""
        pass

    def refresh(self):
        """Update the view from the model/state."""
        pass
