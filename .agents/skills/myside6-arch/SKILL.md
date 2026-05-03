Here is the complete Markdown file, incorporating the new sections for naming conventions, signal flow, and best practices.

```markdown
# PySide6 MVC Architecture Instructions

Guidelines for building Python desktop applications using PySide6 with strict MVC architecture where all UI is defined by `.ui` files.

---

## Architecture Overview
```text
┌─────────────────────────────────────────┐
│         View Layer (.ui files)          │
│  Load from Qt Designer, capture input   │
└──────────────────┬──────────────────────┘
                   │ Signals
┌──────────────────▼──────────────────────┐
│           Controller Layer              │
│  Coordinate models & services           │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│            Model Layer                  │
│  Data structures, validation            │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│           Services Layer                │
│  Database, files, network, broker       │
└─────────────────────────────────────────┘
```

## Project Structure
```text
my_app/
├── app.py                    # Bootstrap & DI container
├── __main__.py               # Entry point
├── controllers/
│   ├── base.py                # BaseController
│   └── *_controller.py        # Domain controllers
├── models/
│   ├── base.py                # BaseModel with signals
│   └── *.py                  # Domain models
├── views/
│   ├── base.py                # BaseView
│   └── *.py                  # View classes
├── services/
│   └── *.py                  # External interactions
├── resources/
│   └── ui/                   # .ui files (Qt Designer)
└── utils/
    └── signals.py            # Central signal registry
```

## Core Principles

| Component | Responsibility | Does NOT |
| :--- | :--- | :--- |
| **Model** | Data, validation, serialization | Touch UI, call services |
| **View** | Load .ui files, capture input | Contain business logic |
| **Controller** | Coordinate models & services | Manipulate UI directly |

---

## Widget Naming Conventions (.ui files)

| Widget Type | Pattern | Example |
| :--- | :--- | :--- |
| Label | `*_label` | `job_number_label` |
| Button | `*_btn` | `save_btn` |
| Line Edit | `*_input` | `customer_input` |
| List | `*_list` | `jobs_list` |
| Table | `*_table` | `pieces_table` |
| Combo | `*_combo` | `status_combo` |

---

## Signal Flow

1. **User Action (View)**
2. ↓ View emits signal
3. ↓ **Controller** handles action
4. ↓ **Service** performs operation
5. ↓ `SignalRegistry.emit()`
6. ↓ **Views** call `refresh()`

---

## Base Class Patterns

### Base Model
```python
from PySide6.QtCore import QObject, Signal
from datetime import datetime
from typing import Any

class BaseModel(QObject):
    property_changed = Signal(str, object)  # name, value
    changed = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._updated_at = datetime.now()
    
    def _set_property(self, name: str, old: Any, new: Any) -> bool:
        if old != new:
            self._updated_at = datetime.now()
            self.property_changed.emit(name, new)
            self.changed.emit()
            return True
        return False
```

### Base View
```python
from pathlib import Path
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import QFile, Signal
from PySide6.QtUiTools import QUiLoader

class BaseView(QWidget):
    error_occurred = Signal(str, str)
    
    def _load_ui(self, ui_filename: str) -> QWidget:
        ui_path = Path(__file__).parent.parent / "resources" / "ui" / ui_filename
        loader = QUiLoader()
        ui_file = QFile(str(ui_path))
        
        if ui_file.open(QFile.ReadOnly):
            ui = loader.load(ui_file, self)
            ui_file.close()
            layout = QVBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(ui)
            return ui
        raise FileNotFoundError(f"Cannot open: {ui_path}")
```

---

## Best Practices

### 1. Never Create UI Programmatically
*   **❌ Wrong:** Manually instantiating `QPushButton` and adding to layouts in Python code.
*   **✅ Correct:** 
    ```python
    self._ui = self._load_ui("my_widget.ui")
    self._btn = self._ui.findChild(QPushButton, "action_btn")
    ```

### 2. Controllers Never Touch UI
*   **❌ Wrong:** `self._view.label.setText(job.name)`
*   **✅ Correct:** 
    ```python
    def activate_job(self):
        self._signals.job_changed.emit(job_id) # Views subscribe to this
    ```

### 3. Views Subscribe to Signals
```python
def _connect_signals(self):
    self._signals.job_changed.connect(self._on_job_changed)

def _on_job_changed(self, job_id):
    self.refresh()
```

### 4. Provide Fallback UI
```python
def _init_ui(self):
    try:
        self._ui = self._load_ui("widget.ui")
    except FileNotFoundError:
        self._create_fallback_ui()
```

### 5. Use Services for External Operations
Controllers delegate to specialized services:
*   **Database queries** → Repository services
*   **File operations** → File service
*   **Network calls** → API service

---

## Common Imports
```python
# Qt
from PySide6.QtWidgets import QWidget, QMainWindow
from PySide6.QtCore import Signal, Slot, QFile
from PySide6.QtUiTools import QUiLoader

# Project
from my_app.utils.signals import get_signal_registry
from my_app.controllers.base import BaseController
from my_app.views.base import BaseView
from my_app.models.base import BaseModel
```

## References
*   [Qt Designer Manual](https://doc.qt.io/qt-6/qtdesigner-manual.html)
*   [PySide6 Documentation](https://doc.qt.io/qtforpython-6/)
