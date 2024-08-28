# Шергазы уулу Бекназар

#1

import sqlite3

class DatabaseManager:
    def __init__(self, db_name):       
        self.db_name = db_name
        self.connection = None
        self.cursor = None
    def open_connection(self):               
        if self.connection is not None:
            raise Exception()
        




#2
        
import sqlite3

class User:
    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )
            ''')
            conn.commit()

    def add_user(self, name, email):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (name, email)
                VALUES (?, ?)
            ''', (name, email))
            conn.commit()

    def get_user_by_id(self, user_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM users WHERE id = ?
            ''', (user_id,))
            user = cursor.fetchone()
            return user

    def delete_user(self, user_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM users WHERE id = ?
            ''', (user_id,))
            conn.commit()



#3


class Admin(User):
    __tablename__ = 'admins'
    
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    admin_level = Column(Integer, nullable=False)
    
    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }

    user = relationship("User", back_populates="admin")

class Customer(User):
    __tablename__ = 'customers'
    
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    customer_type = Column(String, nullable=False)


#4
class DatabaseManager:
    def __init__(self, db_name):
        
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def get_user_data(self, username):

        try:            
            query = "SELECT * FROM users WHERE username = ?"            
          
            self.cursor.execute(query, (username,))            
            
            user_data = self.cursor.fetchone()           
            
            if user_data:
                return user_data
            else:
                return None

        except sqlite3.Error as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return None

    def close(self):
        self.conn.close()