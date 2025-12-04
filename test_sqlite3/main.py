import sqlite3

connect = sqlite3.connect("users.db")
cursor = connect.cursor()

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
        print(f"USUARIO {newUser} ADICIONADO")
    except Exception as e:
        print(e)
    connect.commit()

def read(campo : str, searchInfo : str):
    pass


def read_all():
    try:
        users = cursor.execute("SELECT * FROM users")
        print("USERS:")
        for user in users:
            print("\t", user[1])
    except Exception as e:
        print(e)

def update(id : int, campo : str, newInfo : str):
    try:
        cursor.execute(f"""UPDATE users SET {campo} = ? WHERE id = ? """, (newInfo, id))
        print(f"Novo {campo} agora é {newInfo}")
    except Exception as e:
        print(e)
    connect.commit()



def main():
    start()
    read_all()


    cursor.close()
    connect.close()



if __name__ == "__main__":
    main()