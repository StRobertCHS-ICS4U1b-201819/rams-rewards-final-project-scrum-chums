# Importing the Kivy application, layouts, and buttons
import random
from kivy.app import App

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

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
    '''
    For adding text to Homepage Screen
    '''

    pass


class Teacher(Widget):
    '''
    For adding text to Teacher Profile Screen
    '''

    pass


class SideBar(GridLayout):
    '''
    A Sidebar that switches the screens
    '''

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
    '''
    For generating random code numbers
    '''

    def __init__(self):
        self.usedCodes = []

    def get_new_code(self):
        newCode = random.randrange(0, 9999999)
        while newCode not in self.usedCodes:
            newCode = random.randrange(0, 9999999)
            if newCode not in self.usedCodes:
                self.usedCodes.append(newCode)
        return newCode


class Student(object):
    '''
    For creating each student
    '''

    def __init__(self, firstName, lastName, id, homeroom, clubs):
        self.__first_name = firstName
        self.__last_name = lastName
        self.__id = id
        self.__homeroom = homeroom
        self.__clubsInvolved = clubs
        self.__points = 0

    def get_id(self):
        return self.__id

    def get_student_name(self):
        return self.__first_name + " " + self.__last_name

    def get_homeroom(self):
        return self.__homeroom

    def get_clubs(self):
        return self.__clubsInvolved

    def get_points(self):
        return self.__points

    def set_points(self, morePts):
        self.__points += morePts


class Rewards(object):
    '''
    Creates each Activity
    '''

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


class ChooseStudents(object):
    '''
    Individually selects students for a specific club
    '''

    def __init__(self, memberList):

        self.members = []
        self.allStudents = []
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
        student13 = Student("Allen", "Kim", 12, "12E", "k")
        student14 = Student("Bonnie", "Li", 12, "12E", "")
        student15 = Student("Camille", "Law", 12, "12E", "")
        student16 = Student("Cecil", "Cao", 12, "12E", "")
        student17 = Student("Chelsea", "Moon", 12, "12E", "")
        student18 = Student("Felix", "Yang", 12, "12E", "")
        student19 = Student("Joon", "Kim", 12, "12E", "")
        student20 = Student("Sarah", "Wang", 12, "12E", "")
        student21 = Student("Darya", "Pascarel", 12, "11E", "Robotics")

        self.allStudents.append(student)
        self.allStudents.append(student1)
        self.allStudents.append(student2)
        self.allStudents.append(student3)
        self.allStudents.append(student4)
        self.allStudents.append(student5)
        self.allStudents.append(student6)
        self.allStudents.append(student7)
        self.allStudents.append(student8)
        self.allStudents.append(student9)
        self.allStudents.append(student10)
        self.allStudents.append(student11)
        self.allStudents.append(student12)
        self.allStudents.append(student13)
        self.allStudents.append(student14)
        self.allStudents.append(student15)
        self.allStudents.append(student16)
        self.allStudents.append(student17)
        self.allStudents.append(student18)
        self.allStudents.append(student19)
        self.allStudents.append(student20)
        self.allStudents.append(student21)

        for i in sorted(memberList):
            for j in self.allStudents:
                if j.get_student_name() == i:
                    self.members.append(j)

    def get_newList(self):
        return self.members

    # does not work yet
    def set_student_points(self, who, howMany):
        for i in self.allStudents:
            if i.get_student_name() == who:
                i.set_points(howMany)


class BaseTabs(GridLayout):
    '''
    Makes the tabs look good, distribute points with checkboxes; very bad and inefficient carson pls help
    '''

    # not in use, were for when i was inputting students in program
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()

    # I'm sure what these do but they are id's that refer to the tab
    reward_list = ObjectProperty()
    grade12s_list = ObjectProperty()

    # This was for use in one function, but that one doesn't work, so this is useless
    peeps = ObjectProperty()

    # These are the actual lists still as properties so i can call their other methods
    grade12_list = ObjectProperty()
    rewarding_list = ObjectProperty()

    # These are the actual lists of just names that make the tab lists
    names = ListProperty()
    rewardNames = ListProperty()

    def __init__(self, studentList, rewardList, test, **kwargs):
        super(BaseTabs, self).__init__(**kwargs)

        # members of the clubs as objects
        self.grade12_list = studentList
        self.rewarding_list = rewardList
        self.test = test

        # creating the list of just member names
        for i in self.grade12_list:
            self.names.append(i.get_student_name())
        for j in self.rewarding_list:
            self.rewardNames.append(j.get_activity_name())

        # a dictionary? for tying certain checkboxes to students
        self.student_checkboxes = {}

    # for viewing information about certain activities
    def view_activity(self):
        if self.reward_list.adapter.selection:
            # the selected item name
            selection = self.reward_list.adapter.selection[0].text

            # for generating new code
            code = Code()
            rewardCode = code.get_new_code()

            # creating layout in the tab
            content = GridLayout(cols=2)

            col1 = GridLayout(cols=1)
            col1.add_widget(Label(text="Activity Name: " + selection))
            for rewardObject in self.rewarding_list:
                if rewardObject.get_activity_name() == selection:
                    col1.add_widget(Label(text="Activity Description: " + rewardObject.get_description()))
                    col1.add_widget(Label(text="Date Completed: " + rewardObject.get_date()))
                    col1.add_widget(Label(text="Amount of Points: " + str(rewardObject.get_points())))
            col1.add_widget(Label(text="Rewards Code: " + str(rewardCode)))

            col2 = GridLayout(cols=2)
            for student in self.grade12_list:
                col2.add_widget(Label(text=student.get_student_name()))
                box = CheckBox()
                self.student_checkboxes[student] = box
                col2.add_widget(box)
            givePoints = Button(text='Reward Points',
                                size_hint_y=None,
                                height=40)
            givePoints.bind(on_press=self.get_active_boxes)
            col1.add_widget(givePoints)

            # adds layout to popup to tab
            content.add_widget(col1)
            content.add_widget(col2)
            popup = Popup(title=selection,
                          content=content,
                          size_hint=(None, None), size=(700, 500))
            popup.open()

    def get_active_boxes(self, *args):
        pts = 0

        # finding amount of points for that activity
        if self.reward_list.adapter.selection:
            selection = self.reward_list.adapter.selection[0].text
            for student in self.rewarding_list:
                if student.get_activity_name() == selection:
                     pts = student.get_points()

        # finding selected students and distributing points
        for member, boxes in self.student_checkboxes.items():
            if boxes.active:
                member.set_points(pts)

    def view_student(self):
        if self.grade12s_list.adapter.selection:
            # getting selected item name
            selection = self.grade12s_list.adapter.selection[0].text

            # creating layout for tab
            content = GridLayout(cols=1)
            content.add_widget(Label(text="Student Name: " + selection))
            for i in self.grade12_list:
                if i.get_student_name() == selection:
                    content.add_widget(Label(text="Homeroom: " + i.get_homeroom()))
                    content.add_widget(Label(text="Student ID: " + str(i.get_id())))
                    content.add_widget(Label(text="Accumulated Points: " + str(i.get_points())))
                    content.add_widget(Label(text="Clubs Involved: " + i.get_clubs()))
            content.add_widget(Button(text='View Rewards History', size_hint_y=None, height=40))
            popup = Popup(title= selection,
                          content=content,
                          size_hint=(None, None), size=(400, 400))
            popup.open()


class HomePageScreen(Screen):

    def __init__(self, **kwargs):
        super(HomePageScreen, self).__init__(**kwargs)
        self.add_widget(SideBar())
        self.add_widget(Start())


class ProfileScreen(Screen):

    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        self.add_widget(SideBar())
        self.add_widget(Teacher())


class GeneralScreen(Screen):

    def __init__(self, **kwargs):
        super(GeneralScreen, self).__init__(**kwargs)
        self.add_widget(SideBar())

        # Creates all the members
        members = ChooseStudents(["Chen Feng Zhang", "Jason Ng", "Alex Negoe", "Carson Tang", "Natalie Tam",
                                "Derek Shat", "Kun Lee", "Shawn Nimal", "Tony Ni", "Thomas Maglietta"])
        student_list = members.get_newList()

        # Creates all the activities
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

        # Adds the members and activities to the tabs
        layout = BaseTabs(student_list, rewards, members)
        self.add_widget(layout)


class ClubOneScreen(Screen):

    def __init__(self, **kwargs):
        super(ClubOneScreen, self).__init__(**kwargs)
        self.add_widget(SideBar())

        # Creates all the members
        members = ChooseStudents(["Allen Kim", "Bonnie Li", "Camille Law", "Carson Tang", "Cecil Cao", "Chelsea Moon",
                                "Erin Chin", "Eryka Shi-Shun", "Felix Yang", "Grace Leung", "Joon Kim", "Sarah Wang", "Thomas Maglietta"])
        student_list = members.get_newList()

        # Creates all the activities
        rewards = []
        act = Rewards("Club Attendance", "Attends a weekly club meeting", "Every week", 1)
        act1 = Rewards("Coding Competitions", "DMOJ", " ", 20)
        rewards.append(act)
        rewards.append(act1)

        # Adds the members and activities to the tabs
        layout = BaseTabs(student_list, rewards, members)
        self.add_widget(layout)


class ClubTwoScreen(Screen):

    def __init__(self, **kwargs):
        super(ClubTwoScreen, self).__init__(**kwargs)
        sidebar = SideBar()
        self.add_widget(sidebar)

        # Creates all the members
        members = ChooseStudents(["Allen Kim", "Darya Pascarel", "Grace Leung"])
        student_list = members.get_newList()

        # Creates all the activities
        rewards = []
        act = Rewards("Club Attendance", "Attends a weekly club meeting", "Every week", 1)
        rewards.append(act)

        # Adds the members and activities to the tabs
        layout = BaseTabs(student_list, rewards, members)
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