import MySQLdb
db = MySQLdb.connect("localhost","root","@19135nm","test")
cursor = db.cursor()
sql="SELECT test FROM test"
cursor.execute(sql)
data = cursor.fetchall()
print data
db.close()
