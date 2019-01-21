import sqlite3
con = sqlite3.connect("db.sqlite3")
# on return = [0] -> id, [1] -> name, [2] -> grade, [3] -> score, [4] -> id, [5] -> password

def update_score(connection, param):
    try:
        sql = "UPDATE students_student SET student_score = ? WHERE student_name = ?"  # sets the student score
        # question marks are filled in order with the values in param
        # param must have the proper values or it will fail
        # add addition fields to SET using comma as separator "SET score = ?, name = ?"
        cur = connection.cursor()
        cur.execute(sql, param)
        connection.commit()  # commit changes
    except ValueError:
        return False
    return True

def return_all(connection):

    c = connection.cursor()
    users = "SELECT * FROM students_student"  # select all
    c.execute(users)
    result = c.fetchall()


    return result  # returns list of tuples -> contains the fields of students

def return_id(connection):

    c = connection.cursor()
    users = "SELECT student_id FROM students_student"  # select all
    c.execute(users)
    result = c.fetchall()


    return result  # returns list of tuples -> contains the fields of students

def return_act(connection):

    c = connection.cursor()
    users = "SELECT * FROM activities_activitie"  # select all
    c.execute(users)
    result = c.fetchall()


    return result  # returns list of tuples -> contains the fields of students


def get_by_id(connection, student_id):
    sql = "SELECT * FROM students_student WHERE student_id = ?"
    cur = connection.cursor()
    cur.execute(sql, (student_id,))
    result = cur.fetchall()
    return result


def get_by_name(connection, student_id):
    sql = "SELECT * FROM students_student WHERE student_name = ?"
    cur = connection.cursor()
    cur.execute(sql, (student_id,))
    result = cur.fetchall()
    return result

def get_by_act(connection, activitie_id):
    sql = "SELECT * FROM activities_activitie WHERE title = ?"
    cur = connection.cursor()
    cur.execute(sql, (activitie_id,))
    result = cur.fetchall()
    return result

def verify(connection, userid, password):
    sql = "SELECT * FROM students_student WHERE student_id = ? and student_pass = ?"
    cur = connection.cursor()
    cur.execute(sql, (userid, password))
    result = cur.fetchall()
    if len(result) == 0:
        return False
    return True

def update_history(connection, param):
    try:
        sql = "UPDATE students_student SET student_history = ? WHERE student_name = ?"  # sets the student score
        # question marks are filled in order with the values in param
        # param must have the proper values or it will fail
        # add addition fields to SET using comma as separator "SET score = ?, name = ?"
        cur = connection.cursor()
        cur.execute(sql, param)
        connection.commit()  # commit changes
    except NameError:
        return False
    return True

print(return_all(con))

# for resetting data

'''
for student in return_all(con):
    update_history(con, ('', student[1]))
    update_score(con, (0, student[1]))
    print(get_by_name(con, student[1])[0])
    print(student[6].split('.'))
'''


for i in return_id(con):
    print(i[0])
