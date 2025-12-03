import json
import os
from datetime import datetime

NOTES_FILE = 'notes.json'
LOG_FILE = 'log.txt'

def save_log(action):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(LOG_FILE, 'a', encoding='utf-8') as log_file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                note_id = kwargs.get('id') or (args[0] if args else 'unknown')
                log_file.write(f"{timestamp} | {action} | id: {note_id}\n")
            return result
        return wrapper
    return decorator

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_notes(notes):
    with open(NOTES_FILE, 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)