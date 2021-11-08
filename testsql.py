import sqlite3

conn = sqlite3.connect('db.sqlite3')

print("Opened database successfully")
cursor = conn.execute("select building,ap,client from freespace_capacity")
for row in cursor:
    print(row[0])
    print(row[1])
    print(row[2])
print("Done!")
conn.close()