import sqlite3 as sql

from typing import List, Optional

from test_sqlite3.usersClass import User 


class DataBank():

    user_list : List[User] = []

    def __init__(self, dataBankName):
        try:
            self.connect = sql.connect(dataBankName) #sqlite://data/user2s.db
            self.cursor = self.connect.cursor()
        
        except Exception as e:
            print("Error:", e)
        
        self.start()

    def start(self):
        
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        email TEXT UNIQUE
                )
            """)
            
            self.connect.commit()
        except Exception as e:
            print("Error:", e)

        self.bank_to_ram()

    def bank_to_ram(self):
        try:
            user_list = self.cursor.execute("SELECT * FROM users")
        except Exception as e:
            print("ERROR:",e)

    def new_user(self, new_user : User):
        try:
            self.cursor.execute("""INSERT INTO users (id, name, email) VALUES (?, ?, ?)""", (User))
            self.connect.commit()
            print(f"USUARIO {User.name} ADICIONADO")
        except Exception as e:
            print("ERROR:", e)

