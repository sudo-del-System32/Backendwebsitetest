import sqlite3 as sq
from usersClass import User 
from bdClass import DataBank





# ---- MAIN ----

def main():
    bd = DataBank("data/users2.db")
    bd.add_user(User((None, "Chappel Roan", "SheLikesGirls@Diva.com")))


if __name__ == "__main__":
    main()