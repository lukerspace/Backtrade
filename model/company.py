import mysql.connector
import mysql.connector
from mysql.connector import pooling


connection_pool =mysql.connector.pooling.MySQLConnectionPool(
    pool_name="Mysql",
    pool_size=20,
    host="localhost",
    user="root",
    password="0000",
    database="company"
)

cur=connection_pool.get_connection()
cursor=cur.cursor()

print(cursor.fetchall())