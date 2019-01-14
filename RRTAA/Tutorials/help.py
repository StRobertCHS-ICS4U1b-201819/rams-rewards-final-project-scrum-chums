from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder
from kivy.uix.button import Button
import random
from kivy.app import App
from RRTAA.BarcodeScanner import Scanner
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.uix.listview import ListView

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Label
from kivy.uix.treeview import TreeViewLabel
from kivy.uix.button import Button
from kivy.uix.listview import ListItemButton
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.properties import ObjectProperty, ListProperty

# Setting Screen Manager as a variable
screen_manager = ScreenManager()

# You could also put the following in your kv file...
Builder.load_string("""
#: import main help
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton

<DragBoxLayout>:
    # Define the properties for the DragLabel
    drag_rectangle: 0, self.y, self.width, self.height
    drag_timeout: 90
    drag_distance: 0

<SideBar>:
    orientation: "vertical"  
    cols: 2
    rows: 1
    padding: 0
    spacing: 0
    
    DragBoxLayout:
        orientation: "vertical"
        size_hint_x: 0.34
        Button:
            text: "Homepage"
            background_normal: ''
            background_color: 0.16, 0.02, 0.39, 1
            background_down: 'why.png.png' 
            size_hint_x: None
            size_hint_y: None
            width: 200
            height: 40
            on_press:root.change_screen("Homepage")
        
        Button:
            text: "Teacher Profile"
            background_normal: ''
            background_color: 0.46, 0.32, 0.69, 1
            background_down: 'why.png.png' 
            size_hint_x: None
            size_hint_y: None
            width: 200
            height: 60
            on_press: root.change_screen("Profile")
            
        Button:
            text: "General Activities"
            background_down: 'why.png.png' 
            size_hint_x: None
            size_hint_y: None
            width: 200
            height: 60
            on_press: root.change_screen("General")
            
        Button:
            text: "Coding Club"
            background_down: 'why.png.png' 
            size_hint_x: None
            size_hint_y: None
            width: 200
            height: 60
            on_press: root.change_screen("Coding")
                
        Button:
            text: "Robotics"
            background_down: 'why.png.png' 
            size_hint_x: None
            size_hint_y: None
            width: 200
            height: 60
            on_press: root.change_screen("Robotics")
        
        Button:
            text: "Scanner"
            background_down: 'why.png.png' 
            size_hint_x: None
            size_hint_y: None
            width: 200
            height: 60
            on_press: root.change_screen("Scanner")
                   
       
            
        Label:
            background_color: 1, 1, 1, 1
            size_hint_x: None
            width: 200
        

""")


class DragBoxLayout(DragBehavior, BoxLayout):
    pass


class SideBar(GridLayout):
    '''
    A Sidebar that switches the screens
    '''

    def change_screen(self, page):
        if page == "Homepage" and screen_manager.current != "screen_one":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.001
            screen_manager.current = "screen_one"

        elif page == "Scanner" and screen_manager.current != "screen_six":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.001
            screen_manager.current = "screen_six"

class HomePageScreen(Screen):

    def __init__(self, **kwargs):
        super(HomePageScreen, self).__init__(**kwargs)
        self.add_widget(SideBar())


class Scanner(Screen):

    def __init__(self, **kwargs):
        super(Scanner, self).__init__(**kwargs)
        sidebar = SideBar()

screen_manager.add_widget(HomePageScreen(name= "screen_one"))

screen_manager.add_widget(Scanner(name= "screen_six"))


class TeacherApp(App):

    def build(self):
        Window.clearcolor = (0.3725, 0.6196, 0.6275, 1)
        return screen_manager

TeacherApp().run()