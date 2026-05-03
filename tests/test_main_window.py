import pytest
from PySide6.QtWidgets import QLabel
from src.views.main_view import MainView
from src.signals import get_signals

def test_main_window_shows_hello_world(qtbot):
    """Test that the main window loads and contains the hello message."""
    signals = get_signals()
    
    # This should fail initially because MainView doesn't exist
    view = MainView(signals)
    qtbot.addWidget(view)
    
    # We expect a label named 'message_label' with specific text
    message_label = view.findChild(QLabel, "message_label")
    assert message_label is not None
    assert message_label.text() == "Hello, Keepers!"
