from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.listview import ListView
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.uix.image import Image


"""
-------------------------------------------------------------------------------
Name:		student.py
Purpose:		
An app that lets users view and interact with their profiles and point tallies 

Author:		Shi-Shun E. 

Created:		15.12.2018
------------------------------------------------------------------------------
"""

Builder.load_string("""
#: import main student
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
 
<CustButton@Button>:
    font_size: 25
    color: 0, 0, 0, 1
    background_normal: ''
    background_color: 1, 1, 1, 1

<CustLabel@Label>:
    font_size: 20
    color: 0, 0, 0, 1

<LoginInput@TextInput>: 
    size_hint_x: None
    size_hint_y: None
    width: 200
    height: 35
    multiline: False
    
<Login>:

    username_text_input: username
    password_text_input: password
    
    FloatLayout:
        orientation: "vertical"
        pos_hint_y: 1
        pos_hint_x: 5
        
        CustLabel:
            text: "Ram Rewards Student App"
            color: 0, .5, 0, .9
            pos_hint: {"center_x": 0.5, "center_y": .85}
            font_size: 30
            
        CustLabel:
            text: "Welcome!"
            pos_hint: {"center_x": 0.5, "center_y": .75}
            font_size: 30
        
        CustLabel:
            text: "Username"   
            pos_hint: {"center_x": 0.43, "center_y": .65}
                   
        LoginInput:
            id: username  
            pos_hint: {"center_x": 0.5, "center_y": .6}
            
        CustLabel:
            text: "Password"
            pos_hint: {"center_x": 0.43, "center_y": .5}
            
        LoginInput:
            id: password
            pos_hint: {"center_x": 0.5, "center_y": .45}
            password: True
            
        Button:
            text: "Login"  
            background_color: 0, 2.2, 0, .8
            size_hint_x: None
            size_hint_y: None
            width: 200
            height: 50
            pos_hint: {"center_x": 0.5, "center_y": .3}
            on_press: root.submit()  


<Profile>:  
    code_text_input: code
    
    PageLayout:    
        
        FloatLayout:      
            CustButton:
                text: "Profile Information"
                pos_hint: {"x": 0, "top": 1}
                size_hint: 1, .2 
                on_press: root.info()
            
            CustButton:
                text: "Point History"
                pos_hint: {"x": 0, "top": .8}
                size_hint: 1, .15 
                on_press: root.history()
                
            TextInput: 
                id: code
                size_hint: .6, .1 
                multiline: False
                pos_hint: {"x": .15, "top": .6}
                
            CustButton:
                text: "Go"
                pos_hint: {"x": .8, "top": .6}
                size_hint: .2, .1 
                background_color: 0, 0, 0, 0.2
                on_press: root.add_activity()
                
            CustButton:
                text: "Quit"
                pos_hint: {"right": 1.1, "top": .1}
                color: 1, 1, 1, 0
                size_hint: .55, .1 
                background_color: 0, 0, 0, 1
                on_press: App.get_running_app().stop()    
                 
            CustButton:
                text: "Logout"
                pos_hint: {"x": 0, "top": .1}
                size_hint: .55, .1 
                background_color: 0, 0, 0, 0.2
                on_press: root.manager.current = 'login'
                    
                
        FloatLayout:
            CustButton: 
                text: "Student ID"
                pos_hint: {"x": -.1, "top": .5}
                size_hint: 1.1, .4 
                on_press: root.studentid()
            

    BoxLayout:
        orientation: "vertical"
        
            
        
""")

screen_manager = ScreenManager()

class Rewards(object):
    '''
    A class representing the rewarded points gotten from activities
    '''

    def __init__(self, activity, points, code):
        self.__act = activity
        self.__points = points
        self.__code = code

    def get_actName(self):
        '''
        get the name of an activity
        :return: self.__act: str
        '''
        return self.__act

    def get_points(self):
        '''
        get the value of points of an activity
        :return: self.__points: int
        '''
        return self.__points

    def get_code(self):
        '''
        get the code of an activity
        :return: self.__code: str
        '''
        return self.__code


rewards = []
rewards.append(Rewards("Attendance", 2, "att"))
rewards.append(Rewards("Paint", 5, "paint"))
rewards.append(Rewards("Prom", 10, "prom"))
rewards.append(Rewards("Cafeteria activity", 1, "caf"))
rewards.append(Rewards("Ram of the Month", 20, "ram"))

class Student(object):
    '''
    A class representing a student user
    '''
    def __init__(self, name, studentID, user, password):
        self.__name =  name
        self.__id = studentID
        self.__barcode = Image(source='indbarcode.jpg')
        self.__user = user
        self.__password = password
        self.__points = 0
        self.__hmrm = "12A"
        self.__history = []
       

    def get_name(self):
        '''
        get the name of a student
        :return: self.__name: str
        '''
        return self.__name

    def get_id(self):
        '''
        get the id of a student
        :return: self.__id: int
        '''
        return str(self.__id)

    def get_barcode(self):
        '''
        get the barcode of a student
        :return: self.__barcode: Image
        '''
        return self.__barcode

    def get_hmrm(self):
        '''
        get the homeroom of a student
        :return: self.__hmrm: str
        '''
        return self.__hmrm

    def set_hmrm(self, newhmrm):
        '''
        set the homeroom of a student
        :param newhmrm: str new homeroom
        :return: None
        '''
        self.__hmrm = newhmrm

    def get_user(self):
        '''
        get the username of a student
        :return: self.__user: str
        '''
        return self.__user

    def get_pass(self):
        '''
        get the password of a student
        :return: self.__password: str
        '''
        return self.__password

    def get_points(self):
        '''
        get the value of how many points a student has
        :return: self.__points: int
        '''
        return self.__points

    def __add_points(self, reward):
        '''
        Give a student points
        :param reward: Object
        :return: None
        '''
        self.__points += reward.get_points()

    def __add_history(self, reward):
        '''
        Add reward content to a student's history
        :param reward: Object
        :return: None
        '''
        self.__history.append(reward.get_actName() + ": " + str(reward.get_points()) + " points")

    def add_reward(self, reward):
        '''
        Add reward content to history and points
        :param reward: Object
        :return: None
        '''
        self.__add_history(reward)
        self.__add_points(reward)

    def get_history(self):
        '''
        get the rewards history of a student
        :return: self.__history: list
        '''
        return self.__history

students = []
students.append(Student("Eryka S", 1234, "eryka", "pass"))
students.append(Student("Grace L", 8888, "grace", "pass"))
students.append(Student("Erin C", 9111, "erin", "pass"))
students.append(Student("Carson T", 8765, "carson", "pass"))
students.append(Student("Chen Feng Z", 7878, "chenfeng", "pass"))
admin = Student("admin", 1000, "1", "1")
students.append(admin)
empty_acc = Student("empty", None, "", "")
current_user = empty_acc


class Login(Screen):
    username_text_input = ObjectProperty()
    password_text_input = ObjectProperty()

    def submit(self):
        '''
        Validates the username and password input to change the current user
        :return: None
        '''
        global current_user
        loggedon = False
        for account in students:
            if self.username_text_input.text == account.get_user():
                loggedon = True
                if self.password_text_input.text == account.get_pass():
                    current_user = account
                    self.username_text_input.text = ""
                    self.password_text_input.text = ""
                    screen_manager.current = 'profile'

                else:
                    passwPop = Popup(title="Login Error",
                                     content= Label(text="Wrong password"),
                                     background='atlas://data/images/defaulttheme/button_pressed',
                                    size_hint=(None, None), size=(400, 150))
                    passwPop.open()

        if not loggedon:
            userPop = Popup(title="Login Error",
                             content=Label(text="Invalid username"),
                             background='atlas://data/images/defaulttheme/button_pressed',
                             size_hint=(None, None), size=(400, 150))
            userPop.open()

class Profile(Screen):
    code_text_input = ObjectProperty()
    global current_user

    def info(self):
        '''
        Opens popup that displays student name, id and homeroom
        :return:
        '''
        info = GridLayout(cols=1)
        info.add_widget(Label(text="Name: " + current_user.get_name()))
        info.add_widget(Label(text="Student ID: " + current_user.get_id()))
        info.add_widget(Label(text="Homeroom: " + current_user.get_hmrm()))

        profilePop = Popup(title="Profile Information",
                     content = info,
                     size_hint=(None, None),
                     size=(400, 200))
        profilePop.open()

    def history(self):
        '''
        Opens popup that displays a list of a student's history
        :return: None
        '''
        con = GridLayout(cols=1)
        con.add_widget(Label(text="Points: " + str(current_user.get_points()), size_hint_y=None, height=40))
        self.reward_list = current_user.get_history()
        simple_list_adapter = SimpleListAdapter(data=self.reward_list, cls=Label)
        rewardsList = ListView(adapter=simple_list_adapter)
        con.add_widget(rewardsList)

        historyPop = Popup(title = "Points History",
                     content = con,
                     size_hint=(None, None),
                     size=(400, 300))
        historyPop.open()

    def add_activity(self):
        '''
        Verifies inputed code and adds reward to student
        :return: None
        '''
        added = False

        for activity in rewards:
            if self.code_text_input.text == activity.get_code():
                added = True
                current_user.add_reward(activity)
                self.code_text_input.text = ""

                activityPop = Popup(title="Reward Verification",
                                   content= Label(text="Added " + activity.get_actName() + ": " + str(activity.get_points()) + " points"),
                                   size_hint=(None, None),
                                   size=(400, 150))
                activityPop.open()

        if not added:
            verfPop = Popup(title="Reward Verification",
                         content=Label(text="Sorry, that was not a valid code. Please try again."),
                         size_hint=(None, None),
                         size=(400, 150))
            verfPop.open()

    def studentid(self):
        '''
        Opens popup that displays image of barcode and student ID
        :return: None
        '''

        id_content = GridLayout(cols=1)
        id_content.add_widget(current_user.get_barcode())
        id_content.add_widget(Label(text=current_user.get_id()))

        aPop = Popup(title="Student ID",
                     content=id_content,
                     size_hint=(None, None),
                     size=(400, 300))
        aPop.open()


screen_manager.add_widget(Login(name = "login"))
screen_manager.add_widget(Profile(name = "profile"))


class LoginApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return screen_manager


rrsa = LoginApp()
rrsa.run()
