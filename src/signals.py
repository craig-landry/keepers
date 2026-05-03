from PySide6.QtCore import QObject, Signal

class SignalRegistry(QObject):
    # Define global signals here
    app_started = Signal()
    message_updated = Signal(str)

_instance = None

def get_signals():
    global _instance
    if _instance is None:
        _instance = SignalRegistry()
    return _instance
