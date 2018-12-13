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
from kivy.uix.checkbox import CheckBox

from kivy.uix.button import Label
from kivy.uix.button import Button
from kivy.uix.listview import ListItemButton
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.properties import ObjectProperty, ListProperty, VariableListProperty

Builder.load_string("""
#: import main sry
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton

<BaseTabs>:
    orientation: "vertical"   
    padding: 0
    spacing: 0
    
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
            Button:
                text: "View Activity"
                size_hint_x: 10
                on_press: root.view_activity()
    
""")


class Student(object):
    def __init__(self, firstName, lastName, id, homeroom, clubs):
        self.__first_name = firstName
        self.__last_name = lastName
        self.__id = id
        self.__homeroom = homeroom
        self.__clubsInvolved = clubs

    def get_id(self):
        return self.__id

    def get_student_name(self):
        return self.__first_name + " " + self.__last_name

    def get_homeroom(self):
        return self.__homeroom

    def get_clubs(self):
        return self.__clubsInvolved

class ChooseStudents(object):

    def __init__(self, newList):

        self.people = []
        allStudents = []
        student = Student("Chen Feng", "Zhang", 12, "12E", "")
        student1 = Student("Jason", "Ng", 12, "12E", "")
        student2 = Student("Alex", "Negoe", 12, "12E", "")
        student3 = Student("Carson", "Tang", 12, "11E", "")
        student4 = Student("Natalie", "Tam", 12, "12E", "")
        student5 = Student("Derek", "Shat", 12, "12E", "")
        student6 = Student("Erin", "Chin", 12, "11E", "")
        student7 = Student("Eryka", "Shi-Shun", 12, "12E", "")
        student8 = Student("Kun", "Lee", 12, "12E", "")
        student9 = Student("Grace", "Leung", 12, "12E", "")
        student10 = Student("Shawn", "Nimal", 12, "12E", "")
        student11 = Student("Tony", "Ni", 12, "12E", "")
        student12 = Student("Thomas", "Maglietta", 12, "12E", "")
        student13 = Student("Allen", "Kim", 12, "12E", "")
        student14 = Student("Bonnie", "Li", 12, "12E", "")
        student15 = Student("Camille", "Law", 12, "12E", "")
        student16 = Student("Cecil", "Cao", 12, "12E", "")
        student17 = Student("Chelsea", "Moon", 12, "12E", "")
        student18 = Student("Felix", "Yang", 12, "12E", "")
        student19 = Student("Joon", "Kim", 12, "12E", "")
        student20 = Student("Sarah", "Wang", 12, "12E", "")
        student21 = Student("Darya", "Pascarel", 12, "11E", "Robotics")

        allStudents.append(student)
        allStudents.append(student1)
        allStudents.append(student2)
        allStudents.append(student3)
        allStudents.append(student4)
        allStudents.append(student5)
        allStudents.append(student6)
        allStudents.append(student7)
        allStudents.append(student8)
        allStudents.append(student9)
        allStudents.append(student10)
        allStudents.append(student11)
        allStudents.append(student12)
        allStudents.append(student13)
        allStudents.append(student14)
        allStudents.append(student15)
        allStudents.append(student16)
        allStudents.append(student17)
        allStudents.append(student18)
        allStudents.append(student19)
        allStudents.append(student20)
        allStudents.append(student21)

        for i in sorted(newList):
            for j in allStudents:
                if j.get_student_name() == i:
                    self.people.append(j)

    def get_newList(self):
        return self.people


class BaseTabs(GridLayout):
    def __init__(self, **kwargs):
        super(BaseTabs, self).__init__(**kwargs)
        peeps = ChooseStudents(
            ["Chen Feng Zhang", "Jason Ng", "Alex Negoe", "Carson Tang", "Natalie Tam", "Derek Shat", "Kun Lee",
             "Shawn Nimal", "Tony Ni", "Thomas Maglietta"])
        self.student_list = peeps.get_newList()
        self.check_ref = {}

    def view_activity(self):
        content = GridLayout(cols=2)

        x = GridLayout(cols = 2)
        for i in self.student_list:
            x.add_widget(Label(text= i.get_student_name()))
            c = CheckBox()
            self.check_ref[i.get_student_name()] = c
            x.add_widget(c)
        content.add_widget(x)
        u = Button(text='Reward Points', size_hint_y=None, height=40)
        u.bind(on_press=self.getcheckboxes_active)
        content.add_widget(u)
        popup = Popup(title="help", content=content, size_hint=(None, None), size=(700, 500))
        popup.open()

    def getcheckboxes_active(self, *arg):
        for idx, wgt in self.check_ref.items():
            print(wgt.active, idx)

class ClubOneScreen(Screen):
    def __init__(self, **kwargs):
        super(ClubOneScreen, self).__init__(**kwargs)
        layout = BaseTabs()
        self.add_widget(layout)


class aaApp(App):

    def build(self):
        return ClubOneScreen()
x = aaApp()
x.run()