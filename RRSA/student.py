from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
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
    font_size: 32
    size: 150, 50
    color: 0, 0, 0, 1
    background_normal: ''
    background_color: 1, 1, 1, 1

    

<CustLabel@Label>:
    font_size: 30
    color: 0, 0, 0, 1
    
<LoginInput@TextInput>
    size: 150, 50


<Login>:
    username_text_input: username
    password_text_input: password
    
    
    FloatLayout:

        
        CustLabel:
            text: "Username"
            
            
        LoginInput:
            id: username
            size_hint: .5, .1

        CustLabel:
            text: "Password"
            size_hint: .5, .1
            
        LoginInput:
            id: password
            
        
        Button:
            text: "Submit"
            pos_hint: {"center_x": .5, "center_y": .3}
            background_color: 0, 2.2, 0, .8
            size_hint: .3, .1
            on_press:
                root.manager.current = 'profile'
                


<Profile>:

    FloatLayout:
            
            
        Button:
            text: "Name"
            pos_hint: {"x": 0, "top": 1}
            size_hint: 1, .2 

        Button:
            text: ""
            pos_hint: {"x": 0, "top": .8}
            size_hint: 1, .2 
            
        Button:
            text: "Points:"
            pos_hint: {"x": 0, "top": .6}
            size_hint: 1, .2 
            on_press: root.history()


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


screen_manager.add_widget(Login(name = "login"))
screen_manager.add_widget(Profile(name = "profile"))

class LoginApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return screen_manager


risa = LoginApp()
risa.run()
