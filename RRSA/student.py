from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

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
    
    
<Login>:

    username_text_input: username
    password_text_input: password
   
    
    FloatLayout:
        orientation: "vertical"
        pos_hint_y: 1
        pos_hint_x: 5
        
        CustLabel:
            text: "Ram Rewards Student App"
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
            
        Button:
            text: "Login"  
            background_color: 0, 2.2, 0, .8
            size_hint_x: None
            size_hint_y: None
            width: 200
            height: 50
            pos_hint: {"center_x": 0.5, "center_y": .3}
            on_press: root.manager.current = 'profile'
                


<Profile>:

    PageLayout:    
        FloatLayout:
                
            CustButton:
                text: "Name"
                pos_hint: {"x": 0, "top": 1}
                size_hint: 1, .2 
            
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

            CustLabel: 
                text: "Student ID"
                pos_hint: {"center_x": .3, "top": .7}

            CustLabel:
                text: "123213131"
                pos_hint: {"center_x": .6, "top": .7}
            

""")

screen_manager = ScreenManager()


class Login(Screen):

    username_text_input = ObjectProperty()
    password_text_input = ObjectProperty()


    def submit(self):
        pass

    def check_username(self):
        pass

    def check_password(self):
        pass



class Profile(Screen):

    def history(self):
        pass


class Student(object):
    def __init__(self, name, studentID, user, password):
        self.__name = name
        self.__id = studentID
        self.__user = user
        self.__password = password
        self.__points = 0

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_user(self):
        return self.__user

    def get_pass(self):
        return self.__password

    def get_points(self):
        return self.__points




students = []
students.append(Student("Eryka S", 1234, "eryka", "pass"))
students.append(Student("Grace L", 8888, "grace", "pass"))
students.append(Student("Erin C", 9111, "erin", "pass"))
students.append(Student("Carson T", 8765, "carson", "pass"))
students.append(Student("Chen Feng Z", 7878, "chenfeng", "pass"))




screen_manager.add_widget(Login(name = "login"))
screen_manager.add_widget(Profile(name = "profile"))

class LoginApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return screen_manager


rrsa = LoginApp()
rrsa.run()
