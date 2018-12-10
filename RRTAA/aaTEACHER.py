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
    
<TabbedPanelStrip>
    canvas:
        Color:
            rgba: (0, 1, 0, 1) # green
        Rectangle:
            size: self.size
            pos: self.pos
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
                text: "Clubs"
                values: ["Coding Club", "Mural Club", "Psychology Club", "Robotics"]
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
                    text: "Activities"
                    Label:
                        text: "This is where students go"

                TabbedPanelItem:
                    text: "Student List"
                    Label:
                        text: " i  d o n ' t  k n o w"

  
    BoxLayout:
        orientation: "horizontal"
        size_hint_x: .15

        BoxLayout:
            orientation: "horizontal"
            size_hint: .15, 0.1

            Spinner:
                text: "Clubs"
                values: ["Coding Club", "Mural Club", "Psychology Club", "Robotics"]
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
                    text: "Activities"
                    Label:
                        text: "A list of students"

                TabbedPanelItem:
                    text: "Student List"
                    Label:
                        text: "REWARD US"
  
    BoxLayout:
        orientation: "horizontal"
        size_hint_x: .15

        BoxLayout:
            orientation: "horizontal"
            size_hint: .15, 0.1

            Spinner:
                text: "Clubs"
                values: ["Coding Club", "Mural Club", "Psychology Club", "Robotics"]
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
                    text: "Activities"
                    Label:
                        text: "People"

                TabbedPanelItem:
                    text: "Student List"
                    Label:
                        text: "Tabs are fun"

    BoxLayout:
        orientation: "horizontal"
        size_hint_x: .15

        BoxLayout:
            orientation: "horizontal"
            size_hint: .15, 0.1

            Spinner:
                text: "Clubs"
                values: ["Coding Club", "Mural Club", "Psychology Club", "Robotics"]
                id: spinner_id
                on_text: root.spinner_clicked(spinner_id.text)
                
<ScreenFive>:
    orientation: "vertical"
    first_name_text_input: first_name
    last_name_text_input: last_name
    grade12_list: grade12s_list_view
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
                    text: "Activities"
                    Label:
                        text: "Where did they go?"

                TabbedPanelItem:
                
                    
                    text: "Student List"
                    
                    BoxLayout:
                        size_hint_y: None
                        height: "40dp"
                
                        Label:
                            text: "First name"
                        TextInput:
                            id: first_name
                        Label:
                            text: "Last name"
                        TextInput:
                            id: last_name
            
                BoxLayout:
                    Button:
                        on_touch_down: root.submit_student()
                    Button:
                        on_press: root.delete_student()
                    Button:
                        on_press: root.replace_student()
            
                ListView:
                    id: grade12s_list_view
                    adapter:
                        ListAdapter(data= ["Grace Leung"], cls= main.StudentListButton)
    BoxLayout:
        orientation: "horizontal"
        size_hint_x: .15

        BoxLayout:
            orientation: "horizontal"
            size_hint: .15, 0.1

            Spinner:
                text: "Clubs"
                values: ["Coding Club", "Mural Club", "Psychology Club", "Robotics"]
                id: spinner_id
                on_text: root.spinner_clicked(spinner_id.text)    
""")


class StudentListButton(ListItemButton):
    pass

class ScreenTwo(Screen):
    def spinner_clicked(self, value):
        if value == "Coding Club":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_two"
        elif value == "Mural Club":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_three"
        elif value == "Psychology Club":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_four"
        else:
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_five"

class ScreenThree(Screen):
    def spinner_clicked(self, value):
        if value == "Coding Club":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_two"
        elif value == "Mural Club":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_three"
        elif value == "Psychology Club":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_four"
        else:
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_five"

class ScreenFour(Screen):

    def spinner_clicked(self, value):
        if value == "Coding Club":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_two"
        elif value == "Mural Club":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_three"
        elif value == "Psychology Club":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_four"
        else:
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_five"



class ScreenFive(Screen):

    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    grade12_list = ObjectProperty()

    def submit_student(self):
        student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text
        self.grade12_list.adapter.data.extend([student_name])
        self.grade12_list._trigger_reset_populate()

    def delete_student(self):
        if self.grade12_list.adapter.selection:
            selection = self.grade12_list.adapter.selection[0].text
            self.grade12_list.adapter.data.remove(selection)
            self.grade12_list._trigger_reset_populate()

    def replace_student(self):
        if self.grade12_list.adapter.selection:
            selection = self.grade12_list.adapter.selection[0].text
            self.grade12_list.adapter.data.remove(selection)
            student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text
            self.grade12_list.adapter.data.extend([student_name])
            self.grade12_list._trigger_reset_populate()

    def spinner_clicked(self, value):
        if value == "Coding Club":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_two"
        elif value == "Mural Club":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_three"
        elif value == "Psychology Club":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_four"
        else:
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_five"


class ScreenOne(Screen):
    def spinner_clicked(self, value):
        if value == "Coding Club":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_two"
        elif value == "Mural Club":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_three"
        elif value == "Psychology Club":
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
