import os
import keyboard
keyboard._os_keyboard.setup_tables()
from pprint import pprint
pprint(keyboard._os_keyboard.to_scan_code)