import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color,Rectangle

class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 5
        self.add_widget(Button(text='Profile'))
        self.add_widget(Button(text='Activity Rewards'))
        self.add_widget(Button(text='Student Rewards'))
        self.add_widget(Button(text='View Activities'))
        self.add_widget(Button(text='View Students'))
        self.add_widget(Button(text='Settings'))
        with self.canvas.before:
            Color(0,1,0,1)
            self.rect = Rectangle(size=self.size,pos=self.pos)

class MyApp(App):
    def build(self):
        return MainScreen()

MyApp().run()





