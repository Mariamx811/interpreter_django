from .message_producer import MessageStrategy
import sqlite3

class SqliteProducer(MessageStrategy):

    def __init__(self, db_name="software_engineering.db"):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        """Ensure the table exists in the database."""
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS data (
                asset_id TEXT PRIMARY KEY,
                attribute_id INT,
                timestamp TEXT,
                value TEXT
            );
        """)
        connection.commit()
        connection.close()

    def save(self, data):
        print("data saved")
        """Save data to the SQLite database."""
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO data VALUES (?,?,?,?)
        """, (data['asset_id'],data["attribute_id"],data["timestamp"] ,data['value']))
        connection.commit()
        connection.close()