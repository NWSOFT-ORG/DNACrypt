import os
from pathlib import Path

from NWSh.constants import OSX, WINDOWS

# Path to the user preferences folder
if WINDOWS:
    USER_PREFS_DIR = Path(os.getenv("APPDATA")) / "NWSOFT" / "NWSh"
elif OSX:
    USER_PREFS_DIR = Path.home() / "Library" / "Preferences" / "NWSOFT" / "NWSh"
else:
    USER_PREFS_DIR = Path.home() / ".NWSOFT" / "NWSh"

# Path to the user preferences file
USER_PREFS_FILE = USER_PREFS_DIR / "settings.json"
DEFAULT_PREFS_FILE = Path(__file__).parent / "resources" / "settings.json"
