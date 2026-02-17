import sqlite3 as sql

from typing import List, Optional

from usersClass import User 


class DataBank():


    def __init__(self, dataBankName):
        try:
            self.connect = sql.connect(dataBankName) #sqlite://data/user2s.db
            self.cursor = self.connect.cursor()
            self.start()
        
        except Exception as e:
            print("Error:", e)
        




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
            return None
        



    def add_user(self, new_user : User):
        try:
            a, b, c = (new_user.__dict__.values())
            self.cursor.execute("""INSERT INTO users (id, name, email) VALUES (?, ?, ?)""", (a, b, c))
            self.connect.commit()
            return True

        except Exception as e:
            print("Error:", e)
            return False
        


    def search(self, campo : str, info : str):
        try:
            cursor = self.cursor.execute(f"SELECT * FROM users WHERE {campo} = ?", (info,))
            
            found_users : List[User] = []

            for user in cursor.fetchall():
                found_users.append(User(user))
            

            return found_users
        
        except Exception as e:
            print("Error:", e)
            return None
        


    def user_list(self):
        try:
            cursor = self.cursor.execute("SELECT * FROM users")

            list_of_users : List[User] = []

            for user in cursor.fetchall():
                list_of_users.append(User(user))


            return list_of_users
        
        except Exception as e:
            print("Error:", e)
            return None


    def update(self, id : int, campo : str, newInfo : str):
        try:
            self.cursor.execute(f"""UPDATE users SET {campo} = ? WHERE id = ? """, (newInfo, id))
            self.connect.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False


    def delete(self, id : int):
        try:
            self.cursor.execute(f"""DELETE FROM users WHERE id = ?""", (id,))
            self.connect.commit()

            return True
        
        except Exception as e:
            print("Error:", e)
            return False



# Main
bd = DataBank("data/users2.db")


x = bd.user_list()

for i in x:
    print(i.__dict__)