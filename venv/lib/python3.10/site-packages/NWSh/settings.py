import json5rw as json

from NWSh.paths import DEFAULT_PREFS_FILE, USER_PREFS_FILE


class Settings:
    def __init__(self):
        self.settings = {}
        self.load()

    def load(self):
        try:
            with DEFAULT_PREFS_FILE.open() as f:
                self.settings = json.load(f)
            with USER_PREFS_FILE.open() as f:
                self.settings |= json.load(f)
        except FileNotFoundError:
            self.save()

    def save(self):
        USER_PREFS_FILE.parent.mkdir(parents=True, exist_ok=True)
        with USER_PREFS_FILE.open("w") as f:
            json.dump(self.settings, f, indent=4, sort_keys=True)

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save()
