import sqlite3

connect = sqlite3.connect("data/users2.db") #sqlite://data/user2s.db
cursor = connect.cursor()


#can also connect.execute(query) then doenst need connect.commit!
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT UNIQUE
    )
''')
connect.commit()


connect.execute("""INSERT INTO users (name, email) VALUES (?, ?)""", ("Daniel", "fcobertini@gmail.com"))
connect.commit()

cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Leticia", "letébemlegal@gmail.com"))
connect.commit()

lista = cursor.execute("SELECT * FROM users")



for x in lista:
    print(x)

cursor.close()
connect.close()