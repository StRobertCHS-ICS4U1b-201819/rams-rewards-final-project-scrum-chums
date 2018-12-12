from kivy.uix.listview import ListItemButton
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.listview import ListView

from kivy.uix.button import Label
from kivy.uix.button import Button
from kivy.uix.listview import ListItemButton
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.properties import ObjectProperty, ListProperty

Builder.load_string("""
#: import main sry
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton

<BaseTabs>:
    reward_list: rewards_list_view
    orientation: "vertical"   
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
                            ListAdapter(data= ["Club Attendance.1"], cls= main.ListItemButton)
                TabbedPanelItem:
                    text: "Student List"
                    ListView:
                        adapter:
                            ListAdapter(data= root.stud, selection_mode='single', allow_empty_selection=False,cls= main.ListItemButton)
                TabbedPanelItem:
                    text: "Scanner"
""")
class Student(object):
    def __init__(self, firstName, lastName, id, homeroom):
        self.__first_name = firstName
        self.__last_name = lastName
        self.__id = id
        self.__homeroom = homeroom

    def get_id(self):
        print(self.__id)

    def get_student_name(self):
        return self.__first_name + " " + self.__last_name

    def get_homeroom(self):
        return self.__homeroom

    def __str__(self):
        return self.__first_name + " " + self.__last_name

class BaseTabs(BoxLayout):
    stud = ListProperty()

    def __init__(self, idea, **kwargs):
        super(BaseTabs, self).__init__(**kwargs)
        self.stud = idea

    def view_activity(self):
        if self.reward_list.adapter.selection:
            print("hi")
    def view_student(self):
        if self.grade12_list.adapter.selection:
            print("hi")

class ClubTwoScreen(Screen):
    def __init__(self, **kwargs):
        super(ClubTwoScreen, self).__init__(**kwargs)
        stud = []
        student = Student("eryka", "shi shun", 12, "12E")
        student2 = Student("joe", "schmoe", 12, "11E")
        student3 = Student("erin", "chin", 12, "12E")
        student4 = Student("tate", "tate", 12, "9E")

        stud.append(student)
        stud.append(student2)
        stud.append(student3)
        stud.append(student4)

        xx = []
        for i in stud:
            xx.append(i.get_student_name())

        layout = BaseTabs(xx)
        self.add_widget(layout)

class ClubOneScreen(Screen):
    def __init__(self, **kwargs):
        super(ClubOneScreen, self).__init__(**kwargs)
        layout = BaseTabs()
        self.add_widget(layout)

class aaApp(App):

    def build(self):
        return ClubTwoScreen()
x = aaApp()
x.run()