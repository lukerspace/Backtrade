import mysql.connector
from mysql.connector import pooling


connection_pool =mysql.connector.pooling.MySQLConnectionPool(
    pool_name="mysql",
    pool_size=20,
    host="localhost",
    user="root",
    password="0000"
)

cur=connection_pool.get_connection()
my_cursor=cur.cursor()

# my_cursor.execute("CREATE DATABASE company")

# my_cursor.execute("select * from arkeps")
my_cursor.execute("show databases")
# my_cursor.execute("USE fund")
# my_cursor.execute("SHOW ables")
for db in my_cursor:
    print(db)