from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.listview import ListItemButton
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label


Builder.load_string("""
#: import main student
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton

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
    
    PageLayout:    
        
        FloatLayout:
            
                
            CustButton:
                text: root.curr_name
                pos_hint: {"x": 0, "top": 1}
                size_hint: 1, .2 
                on_press: root.hmrm()
            
            CustButton:
                text: "Points:"
                pos_hint: {"x": 0, "top": .8}
                size_hint: 1, .15 
                on_press: root.history()
       
            CustButton:
                text: "Logout"
                pos_hint: {"x": 0, "top": .1}
                size_hint: .5, .1 
                background_color: 0, 0, 0, 0.2
                on_press: root.manager.current = 'login'
                
            CustButton:
                text: "Settings"
                pos_hint: {"right": 1, "top": .1}
                size_hint: .5, .1 
                
        FloatLayout:
            background_color: 1, 1, 1, 1
            CustLabel: 
                text: "Swipe right to interact"
                font_size: 15
                pos_hint: {"center_x": .2, "top": .75}
            CustLabel: 
                text: "Student ID"
                pos_hint: {"center_x": .3, "top": .7}

            CustLabel:
                text: root.curr_id
                pos_hint: {"center_x": .6, "top": .7}
    BoxLayout:
        orientation: "vertical"

""")

screen_manager = ScreenManager()

class Student(object):
    def __init__(self, name, studentID, user, password):
        self.__name =  StringProperty(name)
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

    def add_points(self, points):
        self.__points += points

    def add_history(self, points):
        self.__history.append(points)



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


    #
    # current_id = current_user.get_id()
    # current_points = current_user.get_points()
    # names = ObjectProperty()
    # namer = StringProperty()

    # def __init__(self, curr_user):
    #     super().__init__()
    #     self.current_user = curr_user
    #     self.current_name = self.current_user.get_name()
    #     self.name = self.current_name

    # def __init__(self, **kwargs):
    #     super(Profile, self).__init__(**kwargs)
    #     # self.names = ""
    #     self.namer = current_user.get_name()
    # def __init__(self):
    #     self.curr_name = current_user.get_name()
    #     self.curr_id = current_user.get_id()
    #
    #

    # name = StringProperty(current_user.get_name())

    curr_name = current_user.get_name()
    curr_id = current_user.get_id()

    global gcurr_name
    global gcurr_id

    # def on_enter(self):
    #     curr_name = gcurr_name
    #     curr_id = gcurr_id

    def on_start(self):
        curr_name = gcurr_name
        curr_id = gcurr_id

    def hmrm(self):

        hmrmPop = Popup(title="Homeroom",
                     content = Label(text="Homeroom: " + current_user.get_hmrm()),
                     size_hint=(None, None),
                     size=(400, 100))
        hmrmPop.open()

    def history(self):
        historyPop = Popup(title = "Points History",
                     content = Label(text= "lol"),
                     size_hint=(None, None),
                     size=(400, 400))
        historyPop.open()

    





rewards = []


screen_manager.add_widget(Login(name = "login"))
screen_manager.add_widget(Profile(name = "profile"))


class LoginApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return screen_manager


rrsa = LoginApp()
rrsa.run()
