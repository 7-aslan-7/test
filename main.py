# султанов нурмухаммед
import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def open_connection(self):
        self.conn = sqlite3.connect(self.db_file)
        self.conn.row_factory = sqlite3.Row

    def close_connection(self):
        if self.conn:
            self.conn.close()
            self.conn = None

class User(DatabaseManager):
    def __init__(self, db_file):
        super().__init__(db_file)
        self.table_name = "geeks" 

    def create_table(self):
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS geeks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        self.conn.commit()
        self.close_connection()

    def add_user(self, username, password):
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(
            f"INSERT INTO {self.table_name} (username, password) VALUES (?, ?)",
            (username, password),
        )
        self.conn.commit()
        self.close_connection()

    def get_user_by_id(self, user_id):
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(
            f"SELECT * FROM {self.table_name} WHERE id = ?", (user_id,)
        )
        user = cursor.fetchone() 
        self.close_connection()
        return dict(user) if user else None

    def delete_user(self, user_id):

        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?", (user_id,)
        )
        self.conn.commit()
        self.close_connection()

db_file = "mydatabase.db"
user_manager = User(db_file)
user_manager.create_table()
user_manager.add_user("Kutman", "dengibabki")
user = user_manager.get_user_by_id(1)
print(user)
user_manager.delete_user(1)

