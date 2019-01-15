import sqlite3
con =  sqlite3.connect("db.sqlite3")
c = con.cursor()
users = ("SELECT * FROM students_student")
c.execute(users)
result = c.fetchall()
print(result)
