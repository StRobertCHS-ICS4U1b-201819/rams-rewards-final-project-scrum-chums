import sqlite3
con = sqlite3.connect("db.sqlite3")


def update_score(connection, param):
    try:
        sql = "UPDATE students_student SET student_score = ? WHERE student_name = ?"  # sets the student score
        # question marks are filled in order with the values in param
        # param must have the proper values or it will fail
        # add addition fields to SET using comma as separator "SET score = ?, name = ?"
        cur = connection.cursor()
        cur.execute(sql, param)
        connection.commit() # commit changes
    except Error:
        return False
    return True


def return_all(connection):
    c = connection.cursor()
    users = "SELECT * FROM students_student"  # select all
    c.execute(users)
    result = c.fetchall()
    return result  # returns list of tuples -> contains the fields of students


print(return_all(con))
update_score(con, (1, "Donnor Cong"))
print(return_all(con))
