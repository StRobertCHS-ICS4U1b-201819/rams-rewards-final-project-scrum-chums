class Teacher(object):
    '''
    Constructor for Teacher
    '''

    def __init__(self, firstName: str, lastName: str, userName: str, password: str):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__userName = userName
        self.__password = password

    def get_firstName(self) -> str:
        return self.__firstName

    def get_lastName(self) -> str:
        return self.__lastName

    def get_userName(self) -> str:
        return self.__userName

    def get_password(self) -> str:
        return self.__password

    def set_firstName(self, new_firstName: str):
        self.__firstName = new_firstName

    def set_lastName(self, new_lastName: str):
        self.__lastName = new_lastName

    def set_userName(self, new_userName: str):
        self.__userName = new_userName

    def set_password(self, new_password: str):
        self.__password = new_password

class AccountManager(object):
    '''
    Constructor for accounts of teachers
    '''

    def __init__(self):
        self.__list_teachers = []

    def add_teacher(self, teacher: Teacher):
        self.__list_teachers.append(teacher)

    def remove_teacher(self, teacher: Teacher):
        if teacher in self.__list_teachers:
            self.__list_teachers.remove(teacher)

    def get_list_teachers(self):
        return self.__list_teachers

    def validLogin(self, teacher: Teacher, password: str) -> bool:
        return teacher.get_password() == password

    def samePassword(self, password1: str, password2: str):
        return password1 == password2

    def change_password(self, teacher: Teacher, old_password: str, new_password: str, new_password2: str):
        if self.samePassword(new_password, new_password2) and self.validLogin(teacher, old_password):
            teacher.set_password(new_password)
            return True
        else:
            return False

    def change_userName(self, teacher: Teacher, new_userName: str, password: str):
        if self.samePassword(password, teacher.get_password()):
            teacher.set_userName(new_userName)
            return True
        else:
            return False

    def change_lastName(self, teacher: Teacher, new_lastName: str, password: str):
        if self.samePassword(password, teacher.get_password()):
            teacher.set_lastName(new_lastName)
            return True
        else:
            return False

    def change_firstName(self, teacher: Teacher, new_firstName: str, password: str):
        if self.samePassword(password, teacher.get_password()):
            teacher.set_firstName(new_firstName)
            return True
        else:
            return False
