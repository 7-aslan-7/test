# асылбеков бекназар


import sqlite3


class DatabaseManager:
    def __init__(self):
        self.connect=sqlite3.connect("database.db")
        self.cursor=self.connect.cursor()
        self.connect.execute("""
                                CREATE TABLE IF NOT EXISTS users(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT,
                                    age INTEGER,
                                    role TEXT
                                    )""")
        
    def find_user_by_name(self,name1):
        self.cursor.execute(f"""SELECT name,age FROM users WHERE name=='{name1}'""")
        print(self.cursor.fetchall())

    def close(self):
        self.connect.close()


class User(DatabaseManager):
    def __init__(self):
        DatabaseManager.__init__(self)

    def add_user(self,name,age):
        self.cursor.execute(f"INSERT INTO users (name,age) VALUES('{name}','{age}');")
        self.connect.commit()

    def find_user(self,id):
        self.cursor.execute(f"""SELECT name,age FROM users WHERE id={id}""")
        print(self.cursor.fetchall())
    def remove_user(self,id):
        self.cursor.execute(f"""DELETE FROM users WHERE id={id}""")
        print(self.cursor.fetchall())
        self.connect.commit()



class Admin(User):
    def __init__(self):
        User.__init__(self)
        self.connect.execute("""
                                CREATE TABLE IF NOT EXISTS admins(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT,
                                    age INTEGER
                                    )""")
    
    def add_user(self,name,age):
        self.cursor.execute(f"INSERT INTO admins (name,age) VALUES('{name}','{age}');")
        self.cursor.execute(f"INSERT INTO users (name,age,role) VALUES('{name}','{age}','admin');")
        self.connect.commit()

    def find_user(self,id):
        self.cursor.execute(f"""SELECT name,age FROM admins WHERE id={id}""")
        print(self.cursor.fetchall())

    def remove_user(self,id):
        self.cursor.execute(f"""DELETE FROM admins WHERE id={id}""")
        print(self.cursor.fetchall())
        self.connect.commit()
    



class Customer(User):
    def __init__(self):
        User.__init__(self)
        self.connect.execute("""
                                CREATE TABLE IF NOT EXISTS customers(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT,
                                    age INTEGER
                                    )""")
        
    def add_user(self,name,age):
        self.cursor.execute(f"INSERT INTO customers (name,age) VALUES('{name}','{age}');")
        self.cursor.execute(f"INSERT INTO users (name,age,role) VALUES('{name}','{age}','customer');")
        self.connect.commit()

    def find_user(self,id):
        self.cursor.execute(f"""SELECT name,age FROM customers WHERE id={id}""")
        print(self.cursor.fetchall())
    def remove_user(self,id):
        self.cursor.execute(f"""DELETE FROM customers WHERE id={id}""")
        print(self.cursor.fetchall())
        self.connect.commit()
    

beka=Admin()

beka.find_user_by_name("beka")
beka.remove_user(1)