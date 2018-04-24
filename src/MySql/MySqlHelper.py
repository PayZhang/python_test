import MySQLdb

db = MySQLdb.connect("193.112.41.233", "pay", "741456", "testdb", charset='utf8' )

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print "Database version : %s " % data

db.close()