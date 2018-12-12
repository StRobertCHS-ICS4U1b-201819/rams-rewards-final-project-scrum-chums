from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.core.window import Window
from kivy.uix.textinput import TextInput



class Login(FloatLayout):

    username_text_input = ObjectProperty()
    password_text_input = ObjectProperty()


    def submit(self):
        pass

    def check_username(self):
        pass

    def check_password(self):
        pass

class LoginApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return Login()


risa = LoginApp()
risa.run()
