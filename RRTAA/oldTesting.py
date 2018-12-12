# Importing the Kivy application, layouts, and buttons
import random
from kivy.app import App

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Label
from kivy.uix.button import Button
from kivy.uix.listview import ListItemButton
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.properties import ObjectProperty

# Setting Screen Manager as a variable
screen_manager = ScreenManager()

# Creating a kivy text file in this window
Builder.load_string("""
#: import main oldTesting
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton

<CustLabel@Label>
    color: 0, 0, 0, 1
        
<SideBar>:
    orientation: "vertical"  
    cols: 2
    rows: 1
    padding: 0
    spacing: 0
    
    BoxLayout:
        orientation: "vertical"
        size_hint_x: 0.34
        Button:
            text: "Homepage"
            size_hint_x: None
            size_hint_y: None
            width: 200
            height: 40
            on_press:root.change_screen("Homepage")
        
        Button:
            text: "Teacher Profile"
            size_hint_x: None
            size_hint_y: None
            width: 200
            height: 60
            on_press: root.change_screen("Profile")
            
        Button:
            text: "General Activities"
            size_hint_x: None
            size_hint_y: None
            width: 200
            height: 60
            on_press: root.change_screen("General")
            
        Button:
            text: "Coding Club"
            size_hint_x: None
            size_hint_y: None
            width: 200
            height: 60
            on_press: root.change_screen("Coding")
                
        Button:
            text: "Robotics"
            size_hint_x: None
            size_hint_y: None
            width: 200
            height: 60
            on_press: root.change_screen("Robotics")
                
        Button:
            text: "+ Add New Club"
            size_hint_x: None
            size_hint_y: None
            width: 200
            height: 325
            
        Label:
            background_color: 1, 1, 1, 1
            size_hint_x: None
            width: 200
      
<BaseTabs>
    reward_list: rewards_list_view
    grade12_list: grade12s_list_view
    
    orientation: "vertical"   
    cols: 2
    rows: 1
    padding: 0
    spacing: 0
    
    BoxLayout:
        orientation: "vertical"
        size_hint_x: 0.34
    
    BoxLayout:
        orientation: "vertical"
        size_hint_x: 1
        BoxLayout:
            orientation: "horizontal"
            TabbedPanel:
                do_default_tab: False
                TabbedPanelItem:
                    text: "Activities"
                    ListView:
                        id: rewards_list_view
                        adapter:
                            ListAdapter(data= [""], cls= main.ListItemButton)
                TabbedPanelItem:
                    text: "Student List"
                    ListView:
                        id: grade12s_list_view
                        adapter:
                            ListAdapter(data= ["Grace Leung 123"], cls= main.ListItemButton)
        BoxLayout:
            size_hint_y: None
            height: "40dp"
            Button:
                text: "View Activity"
                size_hint_x: 10
                on_press: root.view_activity()
            Button:
                text: "View Student"
                size_hint_x: 10
                on_press: root.view_student()
                
""")

class SideBar(GridLayout):

    def change_screen(self, page):
        if page == "Homepage" and screen_manager.current != "screen_one":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_one"
        elif page == "Profile" and screen_manager.current != "screen_two":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_two"
        elif page == "General" and screen_manager.current != "screen_three":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_three"
        elif page == "Coding" and screen_manager.current != "screen_four":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_four"
        elif page == "Robotics" and screen_manager.current != "screen_five":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.01
            screen_manager.current = "screen_five"

class Code(object):

    def __init__(self):
        self.usedCodes = []

    def get_new_code(self):
        rand = random.randrange(0, 9999999)
        while rand not in self.usedCodes:
            rand = random.randrange(0, 9999999)
            if rand not in self.usedCodes:
                self.usedCodes.append(rand)
        return rand

class BaseTabs(GridLayout):

    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    student_id_text_input = ObjectProperty()
    reward_list = ObjectProperty()
    grade12_list = ObjectProperty()

    def view_activity(self):
        if self.reward_list.adapter.selection:
            selection = self.reward_list.adapter.selection[0].text
            ran = Code()
            s = ran.get_new_code()
            content = GridLayout(cols=1)
            content.add_widget(Label(text="Activity Name: " + selection))
            content.add_widget(Label(text="Amount of Points: " + selection))
            content.add_widget(Label(text="Rewards Code: " + str(s)))
            content.add_widget(Button(text='Reward Points', size_hint_y=None, height=40))
            popup = Popup(title= selection,
                          content=content,
                          size_hint=(None, None), size=(400, 400))
            popup.open()

    def view_student(self):
        if self.grade12_list.adapter.selection:
            selection = self.grade12_list.adapter.selection[0].text
            x = selection.split()
            name = x[0] + " " + x[1]
            idd = x[2]
            content = GridLayout(cols=1)
            content.add_widget(Label(text="Student Name: " + name))
            content.add_widget(Label(text= "Student ID: " + idd))
            content.add_widget(Button(text='View Rewards History', size_hint_y=None, height=40))
            popup = Popup(title= name,
                          content=content,
                          size_hint=(None, None), size=(400, 400))
            popup.open()

class HomePageScreen(Screen):
    def __init__(self, **kwargs):
        super(HomePageScreen, self).__init__(**kwargs)
        sidebar = SideBar()
        self.add_widget(sidebar)
        content = GridLayout(cols=1)
        content.add_widget(Label(text="WELCOME TO DEATH"))
        self.add_widget(content)

class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        sidebar = SideBar()
        self.add_widget(sidebar)
        content = GridLayout(cols=1)
        content.add_widget(Label(text="Name: Eric Fabroa"))
        content.add_widget(Label(text="Club Coordination: Coding Club, Robotics"))
        self.add_widget(content)

class GeneralScreen(Screen):
    def __init__(self, **kwargs):
        super(GeneralScreen, self).__init__(**kwargs)
        sidebar = SideBar()
        self.add_widget(sidebar)
        layout = BaseTabs()
        self.add_widget(layout)

class ClubOneScreen(Screen):
    def __init__(self, **kwargs):
        super(ClubOneScreen, self).__init__(**kwargs)
        sidebar = SideBar()
        self.add_widget(sidebar)
        layout = BaseTabs()
        self.add_widget(layout)

class ClubTwoScreen(Screen):
    def __init__(self, **kwargs):
        super(ClubTwoScreen, self).__init__(**kwargs)
        sidebar = SideBar()
        self.add_widget(sidebar)
        layout = BaseTabs()
        self.add_widget(layout)

# Adding screens to the Screen Manager
screen_manager.add_widget(HomePageScreen(name= "screen_one"))
screen_manager.add_widget(ProfileScreen(name= "screen_two"))
screen_manager.add_widget(GeneralScreen(name= "screen_three"))
screen_manager.add_widget(ClubOneScreen(name= "screen_four"))
screen_manager.add_widget(ClubTwoScreen(name= "screen_five"))


class TeacherApp(App):

    def build(self):
        Window.clearcolor = (0.83, 0.83, 1, 1)
        return screen_manager

TeacherApp().run()