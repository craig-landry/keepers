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

### Sample Data
The `sample-images/` directory contains real photos from a Fuji XE-4. 

### Core Philosophy: Source-to-Destination
Keepers is not a local photo management or storage tool. Its purpose is to act as a high-speed conduit between the source (e.g., your camera) and final destinations.

- **Work from Source:** The program operates directly on files from the connected source (Camera via MTP or local samples).
- **Selection over Storage:** The goal is to identify "keeper" images and dispatch them immediately.
- **API-First Destinations:** Photos are sent to external services like digital photo frame APIs and Immich servers.
- **Transient Caching:** For performance, images may be cached in a local temporary directory. This is strictly a transient cache and should not be treated as a permanent copy or backup.
