import kivy
kivy.require('1.9.1')

from kivy.app import App
# put all the kivy data into the python file
from kivy.lang import Builder
# manage screens and switching
from kivy.uix.screenmanager import ScreenManager, Screen

# create kivy code directly to python
Builder.load_string("""
<ScreenOne>:
    BoxLayout:
        Button:
            text: "Go to nowhere"
            # when button is pressed go to screen two (works for any events with active an not active)           
            on_press: 
                # define direction screen will slide in
                root.manager.transition.direction = "left"
                # define duration to slide
                root.manager.transition.duration = 1
                # actually changing the screen
                root.manager.current = "screen_two"
<ScreenTwo>:
    BoxLayout:
        Button:
            text: "Go to somewhere"
            # when button is pressed go to screen two (works for any events with active an not active)           
            on_press: 
                # define direction screen will slide in
                root.manager.transition.direction = "left"
                # define duration to slide
                root.manager.transition.duration = 1
                # actually changing the screen, this says the screen name
                root.manager.current = "screen_one"            
""")

class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

# controls movement between screens

screen_manager = ScreenManager()

# add screen to screenmanager by supplying the name

screen_manager.add_widget(ScreenOne(name= "screen_one"))
screen_manager.add_widget(ScreenTwo(name= "screen_two"))

class KivyTut2App(App):

    def build(self):
        return screen_manager

sample_app = KivyTut2App()
sample_app.run()
