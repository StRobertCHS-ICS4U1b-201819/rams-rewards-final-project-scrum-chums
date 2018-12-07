import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

class StudentListButton(ListItemButton):
    pass


# create kivy code directly to python
Builder.load_string("""
#: import main aaTEACHER
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton


<CustLabel@Label>
    color: 0, 0, 0, 1

<ScreenOne>:
    orientation: "vertical"
    padding: 10
    spacing: 10
    
    
    Label:
        text: "WELCOME"
        pos: root.x, 60
            
    BoxLayout:
        orientation: "horizontal"
        size_hint_x: .15

        BoxLayout:
            orientation: "horizontal"
            size_hint: .15, 0.1

            Spinner:
                text: "Student List"
                values: ["Grade 12", "Grade 11", "Grade 10", "Grade 9"]
                id: spinner_id
                on_text: root.spinner_clicked(spinner_id.text)

                

    
<ScreenTwo>:
    orientation: "vertical"
    padding: 10
    spacing: 10
    
    BoxLayout:
        orientation: "horizontal"
        height: 30

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25

            TabbedPanel:
                # nothing will be highlighted
                do_default_tab: False

                # to put anything inside your tab
                TabbedPanelItem:
                    text: "Student List"
                    Label:
                        text: "This is where students go"

                TabbedPanelItem:
                    text: "Reward Code"
                    Label:
                        text: " i  d o n ' t  k n o w"

  
    BoxLayout:
        orientation: "horizontal"
        size_hint_x: .15

        BoxLayout:
            orientation: "horizontal"
            size_hint: .15, 0.1

            Spinner:
                text: "Student List"
                values: ["Grade 12", "Grade 11", "Grade 10", "Grade 9"]
                id: spinner_id
                on_text: root.spinner_clicked(spinner_id.text)     
                
<ScreenThree>:
    orientation: "vertical"
    padding: 10
    spacing: 10
    
    BoxLayout:
        orientation: "horizontal"
        height: 30

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25

            TabbedPanel:
                # nothing will be highlighted
                do_default_tab: False

                # to put anything inside your tab
                TabbedPanelItem:
                    text: "Student List"
                    Label:
                        text: "A list of students"

                TabbedPanelItem:
                    text: "Reward Code"
                    Label:
                        text: "REWARD US"
  
    BoxLayout:
        orientation: "horizontal"
        size_hint_x: .15

        BoxLayout:
            orientation: "horizontal"
            size_hint: .15, 0.1

            Spinner:
                text: "Student List"
                values: ["Grade 12", "Grade 11", "Grade 10", "Grade 9"]
                id: spinner_id
                on_text: root.spinner_clicked(spinner_id.text)    
                
<ScreenFour>:
    orientation: "vertical"
    padding: 10
    spacing: 10
    
    BoxLayout:
        orientation: "horizontal"
        height: 30

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25

            TabbedPanel:
                # nothing will be highlighted
                do_default_tab: False

                # to put anything inside your tab
                TabbedPanelItem:
                    text: "Student List"
                    Label:
                        text: "People"

                TabbedPanelItem:
                    text: "Reward"
                    Label:
                        text: "Tabs are fun"

    BoxLayout:
        orientation: "horizontal"
        size_hint_x: .15

        BoxLayout:
            orientation: "horizontal"
            size_hint: .15, 0.1

            Spinner:
                text: "Student List"
                values: ["Grade 12", "Grade 11", "Grade 10", "Grade 9"]
                id: spinner_id
                on_text: root.spinner_clicked(spinner_id.text)
                
<ScreenFive>:
    orientation: "vertical"
    padding: 10
    spacing: 10
    
    BoxLayout:
        orientation: "horizontal"
        height: 30

        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .25

            TabbedPanel:
                # nothing will be highlighted
                do_default_tab: False

                # to put anything inside your tab
                TabbedPanelItem:
                    text: "Student List"
                    Label:
                        text: "Where did they go?"

                TabbedPanelItem:
                    text: "OH YEA ACTIVITIES"
                    Label:
                        text: "please help"
   
    BoxLayout:
        orientation: "horizontal"
        size_hint_x: .15

        BoxLayout:
            orientation: "horizontal"
            size_hint: .15, 0.1

            Spinner:
                text: "Student List"
                values: ["Grade 12", "Grade 11", "Grade 10", "Grade 9"]
                id: spinner_id
                on_text: root.spinner_clicked(spinner_id.text)      
""")

class ScreenTwo(Screen):
    def spinner_clicked(self, value):
        if value == "Grade 9":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_two"
        elif value == "Grade 10":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_three"
        elif value == "Grade 11":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_four"
        else:
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_five"

class ScreenThree(Screen):
    def spinner_clicked(self, value):
        if value == "Grade 9":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_two"
        elif value == "Grade 10":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_three"
        elif value == "Grade 11":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_four"
        else:
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_five"

class ScreenFour(Screen):
    def spinner_clicked(self, value):
        if value == "Grade 9":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_two"
        elif value == "Grade 10":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_three"
        elif value == "Grade 11":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_four"
        else:
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_five"

class ScreenFive(Screen):
    def spinner_clicked(self, value):
        if value == "Grade 9":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_two"
        elif value == "Grade 10":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_three"
        elif value == "Grade 11":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_four"
        else:
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_five"

class ScreenOne(Screen):
    def spinner_clicked(self, value):
        if value == "Grade 9":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_two"
        elif value == "Grade 10":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_three"
        elif value == "Grade 11":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_four"
        else:
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_five"

# controls movement between screens

screen_manager = ScreenManager()

# add screen to screenmanager by supplying the name

screen_manager.add_widget(ScreenOne(name= "screen_one"))
screen_manager.add_widget(ScreenTwo(name= "screen_two"))
screen_manager.add_widget(ScreenThree(name= "screen_three"))
screen_manager.add_widget(ScreenFour(name= "screen_four"))
screen_manager.add_widget(ScreenFive(name= "screen_five"))


class KivyTut2App(App):

    def build(self):
        Window.clearcolor = (0.04, 0.1, .6, 1)
        return screen_manager

sample_app = KivyTut2App()
sample_app.run()
