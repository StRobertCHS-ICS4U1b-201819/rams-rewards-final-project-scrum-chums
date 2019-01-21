class Student(object):
    '''
    For creating each student
    '''

    def __init__(self, firstName, lastName, id, homeroom, clubs):
        self.__first_name = firstName
        self.__last_name = lastName
        self.__id = id
        self.__homeroom = homeroom
        self.__clubsInvolved = clubs
        self.__points = 0
        self._completed = []

    def get_id(self):
        return self.__id

    def get_student_name(self):
        return self.__first_name + " " + self.__last_name

    def get_homeroom(self):
        return self.__homeroom

    def get_clubs(self):
        return self.__clubsInvolved

    def get_points(self):
        return self.__points

    def set_points(self, morePts):
        self.__points += morePts

    def get_completed_activities(self):
        return self._completed

    def add_completed_activity(self, activity):
        self._completed.append(activity)
