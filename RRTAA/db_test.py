import sqlite3
con = sqlite3.connect("db.sqlite3")
# on return = [0] -> id, [1] -> name, [2] -> grade, [3] -> score, [4] -> id, [5] -> password


def update_score(connection, param):
    '''
    Updates or sets the score of a student
    :param connection: connection to the database
    :param param: int amount of points
    :return: bool
    '''

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
    '''
    Returns a list of tuples which each have their own fields of students
    :param connection: connection to the database
    :return: list of students
    '''

    c = connection.cursor()
    users = "SELECT * FROM students_student"
    c.execute(users)
    result = c.fetchall()

    return result


def return_id(connection):
    '''
    Returns a list of all the student ids
    :param connection: connection to the database
    :return: list of student ids
    '''

    c = connection.cursor()
    users = "SELECT student_id FROM students_student"
    c.execute(users)
    result = c.fetchall()

    return result


def return_act(connection):
    '''
    Returns a list of tuples which each have their own fields of activities
    :param connection: connection to the database
    :return: list of activities
    '''

    c = connection.cursor()
    users = "SELECT * FROM activities_activitie"
    c.execute(users)
    result = c.fetchall()

    return result


def get_by_id(connection, student_id):
    '''
    Finds a student field by id
    :param connection: connection to the database
    :param student_id: str the student id
    :return: list of the student retrieved from the id
    '''

    sql = "SELECT * FROM students_student WHERE student_id = ?"
    cur = connection.cursor()
    cur.execute(sql, (student_id,))
    result = cur.fetchall()

    return result


def get_by_name(connection, student_name):
    '''
    Finds a student field by name
    :param connection: connection to the database
    :param student_name: str the name of the student
    :return: list of the student retrieved from the corresponding name
    '''

    sql = "SELECT * FROM students_student WHERE student_name = ?"
    cur = connection.cursor()
    cur.execute(sql, (student_name,))
    result = cur.fetchall()

    return result


def get_by_act(connection, activitie_id):
    '''
    Finds an activity by activity name
    :param connection: connection to the database
    :param activitie_id: str name of the activity
    :return: list of the activity field retrieved from the name
    '''

    sql = "SELECT * FROM activities_activitie WHERE title = ?"
    cur = connection.cursor()
    cur.execute(sql, (activitie_id,))
    result = cur.fetchall()

    return result


def verify(connection, userid, password):
    '''
    Checks for authentication
    :param connection: connection to the database
    :param userid: str the username or id of the student
    :param password: str the password of the student
    :return: bool
    '''

    sql = "SELECT * FROM students_student WHERE student_id = ? and student_pass = ?"
    cur = connection.cursor()
    cur.execute(sql, (userid, password))
    result = cur.fetchall()
    if len(result) == 0:
        return False
    return True


def update_history(connection, param):
    '''
    Updates the student activity of a student by adding the activity to a string
    :param connection: connection to the database
    :param param: str a string of student activities separated by periods
    :return: bool
    '''

    try:
        sql = "UPDATE students_student SET student_history = ? WHERE student_name = ?"
        cur = connection.cursor()
        cur.execute(sql, param)
        connection.commit()
    except NameError:
        return False
    return True


def update_codes(connection, param):
    '''
    Updates which generated codes are for which activity
    :param connection: connection to the database
    :param param: str a number that is added to a string of all the generated codes
    :return: bool
    '''

    try:
        sql = "UPDATE activities_activitie SET codes = ? WHERE title = ?"
        cur = connection.cursor()
        cur.execute(sql, param)
        connection.commit()
    except NameError:
        return False
    return True


def update_attendants(connection, param):
    '''
    Updates the activity participation of students by adding the student to a string
    :param connection: connection to the database
    :param param: str a string of student that attended the activity separated by periods
    :return: bool
    '''

    try:
        sql = "UPDATE activities_activitie SET participate = ? WHERE title = ?"
        cur = connection.cursor()
        cur.execute(sql, param)
        connection.commit()
    except NameError:
        return False
    return True

# print(return_all(con))

# for resetting data
'''
for student in return_all(con):
    update_history(con, ('', student[1]))
    update_score(con, (0, student[1]))
    print(get_by_name(con, student[1])[0])
    print(student[6].split('.'))

for i in return_act(con):
    update_attendants(con, ('', i[1]))
'''

