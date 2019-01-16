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
        connection.commit()  # commit changes
    except Error:
        return False
    return True


def return_all(connection):
    c = connection.cursor()
    users = "SELECT * FROM students_student"  # select all
    c.execute(users)
    result = c.fetchall()
    return result  # returns list of tuples -> contains the fields of students


def get_by_id(connection, student_id):
    sql = "SELECT * FROM students_student WHERE student_id = ?"
    cur = connection.cursor()
    cur.execute(sql, (student_id,))
    result = cur.fetchall()
    return result


def verifiy(connection, userid, password):
    sql = "SELECT * FROM students_student WHERE student_id = ? and student_pass = ?"
    cur = connection.cursor()
    cur.execute(sql, (userid, password))
    result = cur.fetchall()
    if len(result) == 0:
        return False
    return True


# print(return_all(con))
# update_score(con, (1, "Donnor Cong"))
# print(return_all(con))
id = "userid"
ps = "password"
get_by_id(con, "ballsDPcoder")
if verifiy(con, id, ps):
    student = get_by_id(con, id)[0]
    print(" ".join(("Hello!", student[1])))
