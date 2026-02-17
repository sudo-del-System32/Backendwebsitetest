import sqlite3 as sql

from typing import List, Optional

from usersClass import User 


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



    def search(self, campo : str, info : str):
        try:
            found_users = self.cursor.execute(f"SELECT * FROM users WHERE {campo} = ?", (info,))
            
            print("USERS:")
            for i, user in enumerate(found_users):
                print(f"\tItem[{i+1}]", user[1])

        except Exception as e:
            print("ERROR: ",e)



    def read_all(self):
        try:
            users = self.cursor.execute("SELECT * FROM users")
            
            print("USERS:")
            for i, user in enumerate(users):
                print(f"\tUsuario[{i+1}]", user[1])
        
        except Exception as e:
            print("ERROR:",e)



    def update(self, id : int, campo : str, newInfo : str):
        try:
            self.cursor.execute(f"""UPDATE users SET {campo} = ? WHERE id = ? """, (newInfo, id))
            self.connect.commit()

            print(f"Novo {campo} agora é {newInfo}")

        except Exception as e:
            print("ERROR:",e)



    def delete(self, id : int):
        try:
            self.cursor.execute(f"""DELETE FROM users 
                        WHERE id = ?""", (id,))
            self.connect.commit()

            print(f"Usuario de id {id} foi excluido")
        
        except Exception as e:
            print("ERROR:",e)




# Main
bd = DataBank("data/users2.db")

bd.search("id", 1)
bd.read_all()