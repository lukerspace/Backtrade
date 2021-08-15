import os 
import sys

abs_path=os.path.abspath(os.getcwd())
# pre_path = os.path.abspath("../backtrade/apps/")
# abs_path=abs_path+"\\apps\\"
sys.path.append(abs_path)
print(sys.path)

from apps import db 
from apps.module import *
print("=====INSERT_DATA======")

test=Company_Ark("GOOGL","sWW","dW","ming")

db.session.add(test)
db.session.commit()


# import mysql.connector
# from mysql.connector import pooling
# connection_pool =mysql.connector.pooling.MySQLConnectionPool(
#     pool_name="mysql",
#     pool_size=20,
#     host="localhost",
#     user="root",
#     password="0000"
# )
# cur=connection_pool.get_connection()
# my_cursor=cur.cursor()
# my_cursor.execute("CREATE DATABASE company")
# my_cursor.execute("select * from arkeps")
# my_cursor.execute("show databases")
# my_cursor.execute("USE fund")
# for db in my_cursor:
#     print(db)
