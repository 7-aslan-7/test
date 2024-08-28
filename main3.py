# абдурохманов азизбек

import sqlite3


class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def open_connection(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close_connection(self):
        if self.conn:
            self.conn.close()

class User:
    def __init__(self, db_manager, user_id=None, username=None, role=None):
        self.db_manager = db_manager
        self.user_id = user_id
        self.username = username
        self.role = role

    def add_user(self):
        self.db_manager.cursor.execute(
            "INSERT INTO users (username, role) VALUES (?, ?)", 
            (self.username, self.role)
        )
        self.db_manager.conn.commit()

    def get_user_by_id(self):
        self.db_manager.cursor.execute(
            "SELECT * FROM users WHERE id=?", (self.user_id,)
        )
        return self.db_manager.cursor.fetchone()

    def delete_user(self):
        self.db_manager.cursor.execute(
            "DELETE FROM users WHERE id=?", (self.user_id,)
        )
        self.db_manager.conn.commit()


class Admin(User):
    def add_admin(self, extra_field):
        self.db_manager.cursor.execute(
            "INSERT INTO admins (user_id, extra_field) VALUES (?, ?)", 
            (self.user_id, extra_field)
        )
        self.db_manager.conn.commit()

class Customer(User):
    def add_customer(self, customer_info):
        self.db_manager.cursor.execute(
            "INSERT INTO customers (user_id, customer_info) VALUES (?, ?)", 
            (self.user_id, customer_info)
        )
        self.db_manager.conn.commit()

    def find_user_by_name(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        return self.cursor.fetchone()
    
    def execute_transaction(self, operations):
        try:
            self.conn.execute("BEGIN")
            for operation in operations:
                self.cursor.execute(*operation)
            self.conn.commit()
        except sqlite3.Error:
            self.conn.rollback()
            raise
