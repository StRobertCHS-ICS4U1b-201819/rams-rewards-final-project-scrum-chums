import random

class Code(object):

    def __init__(self):
        self.usedCodes = []

    def get_new_code(self):
        rand = random.randrange(0, 9999999)
        while rand not in self.usedCodes:
            rand = random.randrange(0, 9999999)
            if rand not in self.usedCodes:
                self.usedCodes.append(rand)
        return rand

class Student(object):
    def __init__(self, firstName, lastName, id, homeroom):
        self.__first_name = firstName
        self.__last_name = lastName
        self.__id = id
        self.__homeroom = homeroom

    def get_id(self):
        print(self.__id)

    def get_student_name(self):
        return self.__first_name + " " + self.__last_name

    def get_homeroom(self):
        return self.__homeroom

class Rewards(object):
    def __init__(self):
        self.club = ""
        self.code = 0
        self.__grade9 = []
        self.__grade10 = []
        self.__grade11 = []
        self.__grade12 = []

    def get_club_name(self, club):
        self.club = club # object

    def get_code(self, code):
        return code.get_new_code()

    def get_student_id(self, student):
        return student.get_id()

    def add_student(self, student):
        if student.get_homeroom()[0: -1] == "9":
            self.__grade9.append(student)
        elif student.get_homeroom()[0: -1] == "10":
            self.__grade10.append(student)
        elif student.get_homeroom()[0: -1] == "11":
            self.__grade11.append(student)
        else:
            self.__grade12.append(student)
    def print_students(self):
        print("Grade 9: ")
        for i in self.__grade9:
            print(i.get_student_name())
        print("")

        print("Grade 10: ")
        for j in self.__grade10:
            print(j.get_student_name())
        print("")

        print("Grade 11: ")
        for k in self.__grade11:
            print(k.get_student_name())
        print("")

        print("Grade 12: ")
        for l in self.__grade12:
            print(l.get_student_name())
        print("")



code = Code()
student = Student("eryka", "shi shun", 12, "12E")
student2 = Student("joe", "schmoe", 12, "11E")
student3 = Student("erin", "chin", 12, "12E")
student4 = Student("tate", "tate", 12, "9E")
student5 = Student("grace", "leung", 12, "12E")
student6 = Student("alex", "zhang", 12, "12E")
student7 = Student("carson", "tang", 12, "12E")
student8 = Student("chelsea", "MOON", 12, "12E")




reward = Rewards()
reward.get_code(code)
reward.get_student_id(student)
reward.add_student(student)
reward.add_student(student2)
reward.add_student(student3)
reward.add_student(student4)
reward.add_student(student5)
reward.add_student(student6)
reward.add_student(student7)
reward.add_student(student8)

reward.print_students()

