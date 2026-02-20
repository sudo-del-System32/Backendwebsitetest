import sys

sys.path.append(sys.path[0] + "/..")

from test_sqlite3.usersClass import User 
from test_sqlite3.bdClass import DataBank

import pandas as pd

bd = DataBank("data/users2.db")

bd.start_connection()

df = pd.read_sql_query("SELECT id as NumEntrada, name, email from users", bd.connect)

print(df.head())

bd.connect.close()
