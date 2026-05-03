# Keepers
Streamlined photo sync from camera to local computer with extras to get photos to where they need to go.

## Usage
Run the main application:
```bash
./venv/bin/python main.py
```

## Testing
Keepers follows a strict TDD workflow. Run the test suite:
```bash
./venv/bin/python -m pytest
```

## Installation
Currently assumes a pre-configured virtual environment in `venv/`.
1. Ensure Python 3.14 is installed.
2. Install dependencies:
```bash
python3 -m pip install -t venv/lib/python3.14/site-packages -r requirements.txt
```

## Development
Keepers is fully vibe coded. See AGENTS.md file for details of how it is built. Like development, design aspects are also done primarily with AI with use of [Open Design](https://github.com/nexu-io/open-design/tree/main). 
