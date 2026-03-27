import asyncio
import shutil
from pathlib import Path
import sqlite3
import logging
import yaml

logger = logging.getLogger(__name__)

class FileOrganizer:
    def __init__(self, config_path='config.yaml', db_path='history.db'):
        self.config_path = Path(config_path)
        self.db_path = Path(db_path)
        self.categories = {}
        self.load_config()
        self.init_db()

    def load_config(self):
        if not self.config_path.exists():
            # Create default config if not exists
            default_config = {
                'categories': {
                    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
                    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
                    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
                    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
                    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
                    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c'],
                    'Others': []
                }
            }
            with open(self.config_path, 'w') as f:
                yaml.dump(default_config, f)
            self.categories = default_config['categories']
        else:
            with open(self.config_path, 'r') as f:
                config = yaml.safe_load(f)
            self.categories = config.get('categories', {})

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute('''CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.execute('''CREATE TABLE IF NOT EXISTS moves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER,
            source_path TEXT,
            dest_path TEXT,
            FOREIGN KEY (session_id) REFERENCES sessions(id)
        )''')
        conn.commit()
        conn.close()

    async def organize_files(self, directory):
        dir_path = Path(directory)
        if not dir_path.is_dir():
            raise ValueError("Invalid directory")

        # Create session
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO sessions DEFAULT VALUES')
        session_id = cursor.lastrowid
        conn.commit()
        conn.close()

        # Find files
        files = [f for f in dir_path.iterdir() if f.is_file()]

        # Group by category
        moves = []
        for file in files:
            ext = file.suffix.lower()
            dest_folder = None
            for cat, exts in self.categories.items():
                if ext in [e.lower() for e in exts]:
                    dest_folder = cat
                    break
            if not dest_folder:
                dest_folder = 'Others'
            dest_path = dir_path / dest_folder / file.name
            (dir_path / dest_folder).mkdir(exist_ok=True)
            moves.append((file, dest_path, session_id))

        # Async move
        tasks = [self.move_file(src, dest, session_id) for src, dest, sid in moves]
        await asyncio.gather(*tasks)

        return session_id

    async def move_file(self, src, dest, session_id):
        try:
            await asyncio.to_thread(shutil.move, str(src), str(dest))
            # Log to db
            conn = sqlite3.connect(self.db_path)
            conn.execute('INSERT INTO moves (session_id, source_path, dest_path) VALUES (?, ?, ?)',
                         (session_id, str(src), str(dest)))
            conn.commit()
            conn.close()
            logger.info(f"Moved {src} to {dest}")
        except Exception as e:
            logger.error(f"Failed to move {src}: {e}")

    def undo_last_session(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Get last session
        cursor.execute('SELECT id FROM sessions ORDER BY id DESC LIMIT 1')
        row = cursor.fetchone()
        if not row:
            print("No sessions to undo")
            return
        session_id = row[0]
        # Get moves
        cursor.execute('SELECT source_path, dest_path FROM moves WHERE session_id = ?', (session_id,))
        moves = cursor.fetchall()
        # Undo
        for src, dest in reversed(moves):
            try:
                shutil.move(dest, src)
                logger.info(f"Undid move from {dest} to {src}")
            except Exception as e:
                logger.error(f"Failed to undo {dest} to {src}: {e}")
        # Delete session and moves
        cursor.execute('DELETE FROM moves WHERE session_id = ?', (session_id,))
        cursor.execute('DELETE FROM sessions WHERE id = ?', (session_id,))
        conn.commit()
        conn.close()
        print(f"Undid session {session_id}")