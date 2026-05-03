import sys
from PySide6.QtWidgets import QApplication
from src.views.main_view import MainView
from src.signals import get_signals

def main():
    app = QApplication(sys.argv)
    
    signals = get_signals()
    
    # Create the main view
    window = MainView(signals)
    window.setWindowTitle("Keepers - Hello World")
    window.resize(400, 300)
    window.show()
    
    signals.app_started.emit()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
