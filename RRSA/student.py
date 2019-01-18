from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.listview import ListItemButton
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.listview import ListView
from kivy.adapters.simplelistadapter import SimpleListAdapter


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
                on_press: root.name_hmrm()
            
            CustButton:
                text: "Point History"
                pos_hint: {"x": 0, "top": .8}
                size_hint: 1, .15 
                on_press: root.history()
                
            TextInput: 
                id: code
                size_hint: .6, .1 
                multiline: False
                pos_hint: {"x": .2, "top": .6}
                
            CustButton:
                text: "Go"
                pos_hint: {"x": .8, "top": .6}
                size_hint: .2, .1 
                background_color: 0, 0, 0, 0.2
                on_press: root.add_activity()
                
       
            CustButton:
                text: "Logout"
                pos_hint: {"x": 0, "top": .1}
                size_hint: .5, .1 
                background_color: 0, 0, 0, 0.2
                on_press: root.manager.current = 'login'
                
            CustButton:
                text: "Quit"
                pos_hint: {"right": 1, "top": .1}
                size_hint: .5, .1 
                on_press: App.get_running_app().stop() 
                
        FloatLayout:
            background_color: 1, 1, 1, 1
            CustLabel: 
                text: "Swipe right to interact"
                font_size: 15
                pos_hint: {"center_x": .2, "top": .75}
                
            CustButton: 
                text: "Student ID"
                pos_hint: {"center_x": .5, "top": .7}
                height: 50
                width: 100
                on_press: root.studentid()

    BoxLayout:
        orientation: "vertical"

""")

screen_manager = ScreenManager()


class Rewards(object):
    def __init__(self, activity, points, code):
        self.__act = activity
        self.__points = points
        self.__code = code

    def get_actName(self):
        return self.__act

    def get_points(self):
        return self.__points

    def get_code(self):
        return self.__code


rewards = []
rewards.append(Rewards("Attendance", 2, "att"))
rewards.append(Rewards("Paint", 5, "paint"))
rewards.append(Rewards("Prom", 10, "prom"))
rewards.append(Rewards("Cafeteria activity", 1, "caf"))
rewards.append(Rewards("Ram of the Month", 20, "ram"))

class Student(object):
    def __init__(self, name, studentID, user, password):
        self.__name =  name
        self.__id = studentID
        self.__user = user
        self.__password = password
        self.__points = 0
        self.__hmrm = "12A"
        self.__history = []
       

    def get_name(self):
        return self.__name

    def get_id(self):
        return str(self.__id)

    def get_hmrm(self):
        return self.__hmrm

    def set_hmrm(self, newhmrm):
        self.__hmrm = newhmrm

    def get_user(self):
        return self.__user

    def get_pass(self):
        return self.__password

    def get_points(self):
        return self.__points

    def __add_points(self, reward):
        self.__points += reward.get_points()

    def __add_history(self, reward):
        self.__history.append(reward.get_actName() + ": " + str(reward.get_points()) + " points")

    def add_reward(self, reward):
        self.__add_history(reward)
        self.__add_points(reward)

    def get_history(self):
        return self.__history



students = []
students.append(Student("Eryka S", 1234, "eryka", "pass"))
students.append(Student("Grace L", 8888, "grace", "pass"))
students.append(Student("Erin C", 9111, "erin", "pass"))
students.append(Student("Carson T", 8765, "carson", "pass"))
students.append(Student("Chen Feng Z", 7878, "chenfeng", "pass"))
admin = Student("admin", 0000, "1", "1")
admin.set_hmrm("YE")
students.append(admin)
empty_acc = Student("empty", None, "", "")
current_user = empty_acc
gcurr_name = current_user.get_name()
gcurr_id = current_user.get_id()


class Login(Screen):

    username_text_input = ObjectProperty()
    password_text_input = ObjectProperty()


    def submit(self):

        global current_user

        global gcurr_name
        global gcurr_id


        loggedon = False
        for account in students:
            if self.username_text_input.text == account.get_user():
                loggedon = True
                if self.password_text_input.text == account.get_pass():
                    current_user = account
                    # update_info()
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


    global gcurr_name
    global gcurr_id


    def on_start(self):
        self.curr_name = gcurr_name
        self.curr_id = gcurr_id

    def name_hmrm(self):
        info = GridLayout(cols=1)
        info.add_widget(Label(text="Name: " + current_user.get_name()))
        info.add_widget(Label(text="Homeroom: " + current_user.get_hmrm()))

        profPop = Popup(title="Profile Information",
                     content = info,
                     size_hint=(None, None),
                     size=(400, 200))
        profPop.open()

    reward_list = ListProperty()


    def history(self):
        self.reward_list = current_user.get_history()

        simple_list_adapter = SimpleListAdapter(
            data=self.reward_list,
            cls=Label)
        con = GridLayout(cols=1)
        con.add_widget(Label(text="Points: " + str(current_user.get_points()), size_hint_y=None, height=40))
        theRewardsList = ListView(adapter=simple_list_adapter)
        con.add_widget(theRewardsList)

        historyPop = Popup(title = "Points History",
                     content = con,
                     size_hint=(None, None),
                     size=(400, 400))
        historyPop.open()

    def add_activity(self):

        added = False

        for activity in rewards:
            if self.code_text_input.text == activity.get_code():
                added = True
                current_user.add_reward(activity)

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
        aPop = Popup(title="Student ID",
                     content=Label(text=current_user.get_id()),
                     size_hint=(None, None),
                     size=(400, 200))
        aPop.open()



screen_manager.add_widget(Login(name = "login"))
screen_manager.add_widget(Profile(name = "profile"))


class LoginApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return screen_manager


rrsa = LoginApp()
rrsa.run()
