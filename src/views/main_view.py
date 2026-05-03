from src.views.base_view import BaseView

class MainView(BaseView):
    def _init_ui(self):
        self._ui = self._load_ui("main_window.ui")
        # BaseView's _load_ui sets the UI as a child of this widget, 
        # but the .ui file has a QMainWindow as the top level.
        # Often it's better to layout the BaseView (a QWidget) 
        # and add the loaded UI's centralwidget to it, 
        # or just use the loaded UI directly if it matches the class.
        
        # For simplicity and following the pattern:
        from PySide6.QtWidgets import QVBoxLayout
        layout = QVBoxLayout(self)
        layout.addWidget(self._ui)
        layout.setContentsMargins(0, 0, 0, 0)
