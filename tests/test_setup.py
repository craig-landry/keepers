import pytest
from PySide6.QtWidgets import QApplication

def test_pyside6_available():
    # Simple test to check if PySide6 can be imported and initialized
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    assert app is not None
