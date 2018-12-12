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
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.properties import ObjectProperty, ListProperty

# Setting Screen Manager as a variable
screen_manager = ScreenManager()

# Creating a kivy text file in this window
Builder.load_string("""
#: import main CurrentWork
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton

<CustLabel@Label>
    color: 0, 0, 1, 1

<CustButton@Button>:
    font_size: 18
    color: 0, 0, 0, 1 # In RBG then alpha
    size: 450, 25
    background_normal: ''
    background_down: 'why.png.png'
    background_color: .88, .88, .88, 1

<Start>:
    CustButton:
        text: "WELCOME TO MY MESS OF A PROJECT"
        pos: 255, 530 

<Teacher>:
    CustButton:
        text: "Name: Eric Fabroa"
        pos: 255, 530 

    CustButton:
        text: "Club Coordination: Coding Club, Robotics"
        pos: 255, 490

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
    grade12s_list: grade12ss_list_view
    
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
                            ListAdapter(data= root.rewardNames, cls= main.ListItemButton)
                TabbedPanelItem:
                    text: "Student List"
                    ListView:
                        id: grade12ss_list_view
                        adapter:
                            ListAdapter(data= root.names, cls= main.ListItemButton)
                TabbedPanelItem:
                    text: "Scanner"
                    
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

class Start(Widget):
    pass

class Teacher(Widget):
    pass

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

class Rewards(object):

    def __init__(self, activityName, descript, date, amount):
        self.__activity_name = activityName
        self.__description = descript
        self.__date = date
        self.__points = amount

    def get_activity_name(self):
        return self.__activity_name

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_points(self):
        return self.__points

    def __str__(self):
        return self.__activity_name()

class BaseTabs(GridLayout):

    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    student_id_text_input = ObjectProperty()
    reward_list = ObjectProperty()
    grade12s_list = ObjectProperty()

    grade12_list = ObjectProperty()
    names = ListProperty()

    rewarding_list = ObjectProperty()
    rewardNames = ListProperty()

    def __init__(self, studList, reList, **kwargs):
        super(BaseTabs, self).__init__(**kwargs)
        self.grade12_list = studList
        self.rewarding_list = reList
        for i in self.grade12_list:
            self.names.append(i.get_student_name())
        for j in self.rewarding_list:
            self.rewardNames.append(j.get_activity_name())


    def view_activity(self):
        if self.reward_list.adapter.selection:
            selection = self.reward_list.adapter.selection[0].text
            ran = Code()
            s = ran.get_new_code()
            content = GridLayout(cols=1)
            content.add_widget(Label(text="Activity Name: " + selection))
            for i in self.rewarding_list:
                if i.get_activity_name() == selection:
                    content.add_widget(Label(text="Activity Description: " + i.get_description()))
                    content.add_widget(Label(text="Date Completed: " + i.get_date()))
                    content.add_widget(Label(text="Amount of Points: " + str(i.get_points())))
            content.add_widget(Label(text="Rewards Code: " + str(s)))
            content.add_widget(Button(text='Reward Points', size_hint_y=None, height=40))
            popup = Popup(title= selection,
                          content=content,
                          size_hint=(None, None), size=(400, 400))
            popup.open()

    def view_student(self):
        if self.grade12s_list.adapter.selection:
            selection = self.grade12s_list.adapter.selection[0].text

            content = GridLayout(cols=1)
            content.add_widget(Label(text="Student Name: " + selection))
            content.add_widget(Label(text="Homeroom: " + "somewhere"))
            content.add_widget(Label(text= "Student ID: "))
            content.add_widget(Label(text="Accumulated Points: " + str(0)))
            content.add_widget(Label(text="Clubs Involved: " + "but to what degree"))
            content.add_widget(Button(text='View Rewards History', size_hint_y=None, height=40))
            popup = Popup(title= selection,
                          content=content,
                          size_hint=(None, None), size=(400, 400))
            popup.open()

class HomePageScreen(Screen):
    def __init__(self, **kwargs):
        super(HomePageScreen, self).__init__(**kwargs)
        sidebar = SideBar()
        self.add_widget(sidebar)
        content = Start()
        self.add_widget(content)

class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        sidebar = SideBar()
        self.add_widget(sidebar)
        content = Teacher()
        self.add_widget(content)

class GeneralScreen(Screen):
    def __init__(self, **kwargs):
        super(GeneralScreen, self).__init__(**kwargs)
        sidebar = SideBar()
        self.add_widget(sidebar)
        student_list = []
        student = Student("Chen Fen", "Zhang", 12, "12E")
        student1 = Student("Jason", "Ng", 12, "12E")
        student2 = Student("Alex", "Negoe", 12, "12E")
        student3 = Student("Carson", "Tang", 12, "11E")
        student4 = Student("Natalie", "Tam", 12, "12E")
        student5 = Student("Derek", "Shat", 12, "12E")
        student6 = Student("Erin", "Chin", 12, "11E")
        student7 = Student("Eryka", "Shi-Shun", 12, "12E")
        student8 = Student("Kun", "Lee", 12, "12E")
        student9 = Student("Grace", "Leung", 12, "12E")
        student10 = Student("Shawn", "Nimal", 12, "12E")
        student11 = Student("Tony", "Ni", 12, "12E")
        student12 = Student("Thomas", "Maglietta", 12, "12E")

        student_list.append(student)
        student_list.append(student1)
        student_list.append(student2)
        student_list.append(student3)
        student_list.append(student4)
        student_list.append(student5)
        student_list.append(student6)
        student_list.append(student7)
        student_list.append(student8)
        student_list.append(student9)
        student_list.append(student10)
        student_list.append(student11)
        student_list.append(student12)

        rewards = []
        act = Rewards("Ram of The Month", "Does good in life", "Once a month", 20)
        act1 = Rewards("Participate in Inside Ride", "Riding bikes for cancer and raising money", "Sometime", 100)
        act2 = Rewards("Attend Hockey Buyout", "Watching teachers play hockey, school spirit", "Sometime", 50)
        act3 = Rewards("Attend School Dance", "Grade 9 Dance, Semi-formal, Formal", "Sometime", 25)
        act4 = Rewards("Participate in Christmas Concert", "Singing, Dancing, etc.", "Sometime", 60)
        act5 = Rewards("Attend Christmas Concert", "Watching students perform", "Sometime", 10)
        act6 = Rewards("Participate in Expresso Self", "Singing, Dancing, etc.", "Sometime", 60)
        act7 = Rewards("Attend Expresso Self", "Watching students perform", "Sometime", 10)
        act8 = Rewards("Winning Kahoots", "Getting Top 5 in cafeteria kahoots", "Sometime", 70)
        act9 = Rewards("Participate in School Play", "Acting, Singing, Dancing, etc.", "Sometime", 60)
        act10 = Rewards("Watching School Play", "Watching fun school plays", "Sometime", 10)

        rewards.append(act)
        rewards.append(act1)
        rewards.append(act2)
        rewards.append(act3)
        rewards.append(act4)
        rewards.append(act5)
        rewards.append(act6)
        rewards.append(act7)
        rewards.append(act8)
        rewards.append(act9)
        rewards.append(act10)
        layout = BaseTabs(student_list, rewards)
        self.add_widget(layout)

class ClubOneScreen(Screen):
    def __init__(self, **kwargs):
        super(ClubOneScreen, self).__init__(**kwargs)
        sidebar = SideBar()
        self.add_widget(sidebar)
        student_list = []
        student = Student("Allen", "Kim", 12, "12E")
        student1 = Student("Bonnie", "Li", 12, "12E")
        student2 = Student("Camille", "Law", 12, "12E")
        student3 = Student("Carson", "Tang", 12, "11E")
        student4 = Student("Cecil", "Cao", 12, "12E")
        student5 = Student("Chelsea", "Moon", 12, "12E")
        student6 = Student("Erin", "Chin", 12, "11E")
        student7 = Student("Eryka", "Shi-Shun", 12, "12E")
        student8 = Student("Felix", "Yang", 12, "12E")
        student9 = Student("Grace", "Leung", 12, "12E")
        student10 = Student("Joon", "Kim", 12, "12E")
        student11 = Student("Sarah", "Wang", 12, "12E")
        student12 = Student("Thomas", "Maglietta", 12, "12E")

        student_list.append(student)
        student_list.append(student1)
        student_list.append(student2)
        student_list.append(student3)
        student_list.append(student4)
        student_list.append(student5)
        student_list.append(student6)
        student_list.append(student7)
        student_list.append(student8)
        student_list.append(student9)
        student_list.append(student10)
        student_list.append(student11)

        rewards = []
        act = Rewards("Club Attendance", "Attends a weekly club meeting", "Every week", 1)
        rewards.append(act)
        layout = BaseTabs(student_list, rewards)
        self.add_widget(layout)

class ClubTwoScreen(Screen):
    def __init__(self, **kwargs):
        super(ClubTwoScreen, self).__init__(**kwargs)
        sidebar = SideBar()
        self.add_widget(sidebar)
        student_list = []
        student = Student("Allen", "Kim", 12, "12E")
        student1 = Student("Darya", "Pascarel", 12, "11E")
        student2 = Student("Grace", "Leung", 12, "11E")
        student_list.append(student)
        student_list.append(student1)
        student_list.append(student2)

        rewards = []
        act = Rewards("Club Attendance", "Attends a weekly club meeting", "Every week", 1)
        rewards.append(act)
        layout = BaseTabs(student_list, rewards)
        self.add_widget(layout)

# Adding screens to the Screen Manager
screen_manager.add_widget(HomePageScreen(name= "screen_one"))
screen_manager.add_widget(ProfileScreen(name= "screen_two"))
screen_manager.add_widget(GeneralScreen(name= "screen_three"))
screen_manager.add_widget(ClubOneScreen(name= "screen_four"))
screen_manager.add_widget(ClubTwoScreen(name= "screen_five"))


class TeacherApp(App):

    def build(self):
        Window.clearcolor = (0.3725, 0.6196, 0.6275, 1)
        return screen_manager

TeacherApp().run()