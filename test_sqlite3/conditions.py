import sys

# Testar caminho em outros computadores
sys.path.append(sys.path[0] + "/..")


import sqlite3 as sq
from test_sqlite3.usersClass import User 
from test_sqlite3.bdClass import DataBank





# ---- MAIN ----

def main():
    bd = DataBank("data/users2.db")
    bd.add_user(User((None, "Chappel Roan", "SheLikesGirls@Diva.com")))


if __name__ == "__main__":
    main()