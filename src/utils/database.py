import sqlite3

from src.logger.logger import configure_logger
logger = configure_logger()

class SQLiteDB:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            self.cursor = self.conn.cursor()
            logger.info("SQLiteDB connection established")
            return self.conn, self.cursor
        except sqlite3.Error as e:
            logger.error(f"Error connecting to SQLite database: {e}")