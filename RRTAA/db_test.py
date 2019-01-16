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

# id/ student_name/ student_score/ student_grade
def return_all(connection):
    c = connection.cursor()
    users = "SELECT * FROM students_student"  # select all
    c.execute(users)
    result = c.fetchall()


    return result  # returns list of tuples -> contains the fields of students


def get_id(connection):
    c = connection.cursor()
    users = "SELECT id FROM students_student"  # select all
    c.execute(users)
    result = c.fetchall()

    return result  # returns list of tuples -> contains the fields of students

def get_student_name(connection):
    c = connection.cursor()
    users = "SELECT student_name FROM students_student"  # select all
    c.execute(users)
    result = c.fetchall()

    return result  # returns list of tuples -> contains the fields of students


def get_homeroom(connection):
    c = connection.cursor()
    users = "SELECT student_grade FROM students_student"  # select all
    c.execute(users)
    result = c.fetchall()

    return result  # returns list of tuples -> contains the fields of students


def get_points(connection):
    c = connection.cursor()
    users = "SELECT student_score FROM students_student"  # select all
    c.execute(users)
    result = c.fetchall()

    return result  # returns list of tuples -> contains the fields of students


print(return_all(con))
update_score(con, (23, "Donnor Cong"))
print(get_student_name(con))
print(return_all(con))
