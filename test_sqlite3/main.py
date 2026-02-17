import sqlite3

connect = sqlite3.connect("data/users.db") #sqlite://data/user2s.db
cursor = connect.cursor()

class Users:

    id : int
    name : str
    email : str

    def __init__(self, tuple : tuple):
        self.id , self.name, self.email = tuple 

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

user_list : list[Users] = []


def start():
    #pode se usar connect.execute e sera diretamente executado sem a necessidade de um commit,
    # todavia irei manter dessa forma como uma boa medidade de preservaçao
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT UNIQUE
        )
    """)
    connect.commit()

def create(name : str, email : str):
    try:
        cursor.execute("""INSERT INTO users (name, email) VALUES (?, ?)""", (name, email))
        connect.commit()
        print(f"USUARIO {name} ADICIONADO")
    except Exception as e:
        print("ERROR:",e)

def search(campo : str, info : str):
    try:
        users = cursor.execute(f"SELECT * FROM users WHERE {campo} = ?", (info,))
        print("USERS:")
        for user in users:
            print("\t",user[1])
    except Exception as e:
        print("ERROR: ",e)


def read_all():
    try:
        users = cursor.execute("SELECT * FROM users")
        print("USERS:")
        for user in users:
            #user_list.append(Users(user)) 
            print("\t", user[1])
    except Exception as e:
        print("ERROR:",e)

def update(id : int, campo : str, newInfo : str):
    try:
        cursor.execute(f"""UPDATE users SET {campo} = ? WHERE id = ? """, (newInfo, id))
        connect.commit()
        print(f"Novo {campo} agora é {newInfo}")
    except Exception as e:
        print("ERROR:",e)

def delete(id : int):
    try:
        cursor.execute(f"""DELETE FROM users 
                       WHERE id = ?""", (id,))
        connect.commit()
        print(f"Usuario de id {id} foi excluido")
    
    except Exception as e:
        print("ERROR:",e)


def main():
    start()


    read_all()

    cursor.close()
    connect.close()



if __name__ == "__main__":
    main()