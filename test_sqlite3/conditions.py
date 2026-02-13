import sqlite3 as sq
from test_sqlite3.usersClass import User 
from test_sqlite3.bdClass import DataBank





# ---- MAIN ----

def main():
    bd = DataBank("data/t1.db")
    bd.create(User("Daniel", "Email@Yahoo.com"))



if __name__ == "__main__":
    main()