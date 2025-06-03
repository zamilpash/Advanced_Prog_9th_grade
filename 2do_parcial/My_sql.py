import pymysql

# Conectarse a la base de dato
db = pymysql.Connect(host = "localhost", user = "test_1", password="test1234")
cursor = db.cursor()

sql = "SELECT VERSION()"
sql2 = "SHOW TABLES"

cursor.execute(sql)
data = cursor.fetchone()
print(f"La version es: {data}")
db.close()