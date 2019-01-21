
import random, cv2
from kivy.app import App
from RRTAA.BarcodeScanner import Scanner
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.uix.listview import ListView
from kivy.animation import Animation
from kivy.uix.stencilview import StencilView
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.properties import (ObjectProperty, NumericProperty, OptionProperty,
                             BooleanProperty, StringProperty, ListProperty)

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.button import Label
from kivy.uix.button import Button
from kivy.uix.listview import ListItemButton
from kivy.uix.image import Image

from kivy.uix.checkbox import CheckBox

from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.stencilview import StencilView
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.properties import (ObjectProperty, NumericProperty, OptionProperty,
                             BooleanProperty, StringProperty)
from kivy.lang import Builder
from kivy.graphics.texture import Texture

# Setting Screen Manager as a variable
screen_manager = ScreenManager()

# Creating a Kivy text file in this window
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

<LoginInput@TextInput>: 
    size_hint_x: None
    size_hint_y: None
    width: 200
    height: 35
    multiline: False

<Login>:
    username_text_input: username
    password_text_input: password

    FloatLayout:
        orientation: "vertical"
        pos_hint_y: 1
        pos_hint_x: 5

        CustLabel:
            text: "Ram Rewards Teacher App"
            color: 0, .5, 0, .9
            pos_hint: {"center_x": 0.5, "center_y": .85}
            font_size: 30

        CustLabel:
            text: "Welcome!"
            pos_hint: {"center_x": 0.5, "center_y": .75}
            font_size: 30

        CustLabel:
            text: "Username"
            pos_hint: {"center_x": 0.43, "center_y": .65}

        LoginInput:
            id: username  
            pos_hint: {"center_x": 0.5, "center_y": .6}

        CustLabel:
            text: "Password"
            pos_hint: {"center_x": 0.43, "center_y": .5}

        LoginInput:
            id: password
            password: True
            pos_hint: {"center_x": 0.5, "center_y": .45}

        Button:
            text: "Login"  
            background_color: 0, 2.2, 0, .8
            size_hint_x: None
            size_hint_y: None
            width: 200
            height: 50
            pos_hint: {"center_x": 0.5, "center_y": .3}
            on_press: root.submit(username.text, password.text)

<NavigationDrawer>:
    size_hint: (1,1)
    _side_panel: sidepanel
    _main_panel: mainpanel
    _join_image: joinimage
    side_panel_width: min(dp(250), 0.5*self.width)
    BoxLayout:
        id: sidepanel
        y: root.y
        x: root.x - \
           (1-root._anim_progress)* \
           root.side_panel_init_offset*root.side_panel_width
        height: root.height
        width: root.side_panel_width
        opacity: root.side_panel_opacity + \
                 (1-root.side_panel_opacity)*root._anim_progress
        canvas:
            Color:
                rgba: (0,0,0,1)
            Rectangle:
                pos: self.pos
                size: self.size
        canvas.after:
            Color:
                rgba: (0,0,0,(1-root._anim_progress)*root.side_panel_darkness)
            Rectangle:
                size: self.size
                pos: self.pos
    BoxLayout:
        id: mainpanel
        x: root.x + \
           root._anim_progress * \
           root.side_panel_width * \
           root.main_panel_final_offset
        y: root.y
        size: root.size
        canvas:
            Color:
                rgba: (0,0,0,1)
            Rectangle:
                pos: self.pos
                size: self.size
        canvas.after:
            Color:
                rgba: (0,0,0,root._anim_progress*root.main_panel_darkness)
            Rectangle:
                size: self.size
                pos: self.pos
    Image:
        id: joinimage
        opacity: min(sidepanel.opacity, 0 if root._anim_progress < 0.00001 \
                 else min(root._anim_progress*40,1))
        mipmap: False
        width: root.separator_image_width
        height: root._side_panel.height
        x: (mainpanel.x - self.width + 1) if root._main_above \
           else (sidepanel.x + sidepanel.width - 1)
        y: root.y
        allow_stretch: True
        keep_ratio: False

<Start>:
    orientation: "vertical"   
    cols: 2
    rows: 1
    padding: 0
    spacing: 0

    BoxLayout:
        orientation: "vertical"
        size_hint_x: 1
        Label:
            size_hint_y: None
            height: 80
            text: "WELCOME! WELCOME! WELCOME! WELCOME! WELCOME! WELCOME!"
            valign: 'middle'

# CHANGE LATER   
<TeacherProfile>:
    CustButton:
        text: "Name: Eric Fabroa"
        pos: 255, 530 

    CustButton:
        text: "Club Coordination: Coding Club, Robotics"
        pos: 255, 490


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
        size_hint_x: 1
        BoxLayout:
            orientation: "horizontal"
            TabbedPanel:
                do_default_tab: False
                tab_width: 180
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


class Start(GridLayout):
    '''
    For adding text to Homepage Screen
    '''

    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)
        image = Image(source= 'robbie.jpg', pos= (100, 100))
        self.add_widget(image)



class TeacherProfile(Widget):
    '''
    For adding text to Teacher Profile Screen
    '''

    pass


class NavigationDrawerException(Exception):
    '''Raised when add_widget or remove_widget called incorrectly on a
    NavigationDrawer.

    '''


class NavigationDrawer(StencilView):

    # Internal references for side, main and image widgets
    _side_panel = ObjectProperty()
    _main_panel = ObjectProperty()
    _join_image = ObjectProperty()

    side_panel = ObjectProperty(None, allownone=True)
    '''Automatically bound to whatever widget is added as the hidden panel.'''
    main_panel = ObjectProperty(None, allownone=True)
    '''Automatically bound to whatever widget is added as the main panel.'''

    # Appearance properties
    side_panel_width = NumericProperty()
    '''The width of the hidden side panel. Defaults to the minimum of
    250dp or half the NavigationDrawer width.'''

    separator_image_width = NumericProperty(dp(1))
    '''The width of the separator image. Defaults to 10dp'''

    # Touch properties
    touch_accept_width = NumericProperty('14dp')
    '''Distance from the left of the NavigationDrawer in which to grab the
    touch and allow revealing of the hidden panel.'''
    _touch = ObjectProperty(None, allownone=True)  # The currently active touch

    # Animation properties
    state = OptionProperty('open', options=('open', 'closed'))
    '''Specifies the state of the widget. Must be one of 'open' or
    'closed'. Setting its value automatically jumps to the relevant state,
    or users may use the anim_to_state() method to animate the
    transition.'''
    anim_time = NumericProperty(0.3)
    '''The time taken for the panel to slide to the open/closed state when
    released or manually animated with anim_to_state.'''
    min_dist_to_open = NumericProperty(0.7)
    '''Must be between 0 and 1. Specifies the fraction of the hidden panel
    width beyond which the NavigationDrawer will relax to open state when
    released. Defaults to 0.7.'''
    _anim_progress = NumericProperty(0)  # Internal state controlling
                                         # widget positions
    _anim_init_progress = NumericProperty(0)

    # Animation controls
    top_panel = OptionProperty('main', options=['main', 'side'])
    '''Denotes which panel should be drawn on top of the other. Must be
    one of 'main' or 'side'. Defaults to 'main'.'''
    _main_above = BooleanProperty(True)

    side_panel_init_offset = NumericProperty(0.5)
    '''Intial offset (to the left of the widget) of the side panel, in
    units of its total width. Opening the panel moves it smoothly to its
    final position at the left of the screen.'''

    side_panel_darkness = NumericProperty(0.8)
    '''Controls the fade-to-black of the side panel in its hidden
    state. Must be between 0 (no fading) and 1 (fades to totally
    black).'''

    side_panel_opacity = NumericProperty(1)
    '''Controls the opacity of the side panel in its hidden state. Must be
    between 0 (fade to transparent) and 1 (no transparency)'''

    main_panel_final_offset = NumericProperty(1)
    '''Final offset (to the right of the normal position) of the main
    panel, in units of the side panel width.'''

    main_panel_darkness = NumericProperty(0)
    '''Controls the fade-to-black of the main panel when the side panel is
    in its hidden state. Must be between 0 (no fading) and 1 (fades to
    totally black).
    '''

    opening_transition = StringProperty('out_cubic')
    '''The name of the animation transition type to use when animating to
    an open state. Defaults to 'out_cubic'.'''

    closing_transition = StringProperty('in_cubic')
    '''The name of the animation transition type to use when animating to
    a closed state. Defaults to 'out_cubic'.'''

    anim_type = OptionProperty('reveal_from_below',
                               options=['slide_above_anim'])
    '''The default animation type to use. Several options are available,
    modifying all possibly animation properties including darkness,
    opacity, movement and draw height. Users may also (and are
    encouaged to) edit these properties individually, for a vastly
    larger range of possible animations. Defaults to reveal_below_anim.
    '''

    def __init__(self, **kwargs):
        super(NavigationDrawer, self).__init__(**kwargs)
        Clock.schedule_once(self.on__main_above, 0)

    def on_anim_type(self, *args):

        self.top_panel = 'side'
        self.side_panel_darkness = 0
        self.side_panel_opacity = 1
        self.main_panel_final_offset = 0.5
        self.main_panel_darkness = 0.5
        self.side_panel_init_offset = 1

    def on_top_panel(self, *args):
        if self.top_panel == 'main':
            self._main_above = True
        else:
            self._main_above = False

    def on__main_above(self, *args):
        newval = self._main_above
        main_panel = self._main_panel
        side_panel = self._side_panel
        self.canvas.remove(main_panel.canvas)
        self.canvas.remove(side_panel.canvas)
        if newval:
            self.canvas.insert(0, main_panel.canvas)
            self.canvas.insert(0, side_panel.canvas)
        else:
            self.canvas.insert(0, side_panel.canvas)
            self.canvas.insert(0, main_panel.canvas)

    def add_widget(self, widget):
        if len(self.children) == 0:
            super(NavigationDrawer, self).add_widget(widget)
            self._side_panel = widget
        elif len(self.children) == 1:
            super(NavigationDrawer, self).add_widget(widget)
            self._main_panel = widget
        elif len(self.children) == 2:
            super(NavigationDrawer, self).add_widget(widget)
            self._join_image = widget
        elif self.side_panel is None:
            self._side_panel.add_widget(widget)
            self.side_panel = widget
        elif self.main_panel is None:
            self._main_panel.add_widget(widget)
            self.main_panel = widget
        else:
            raise NavigationDrawerException(
                'Can\'t add more than two widgets'
                'directly to NavigationDrawer')

    def anim_to_state(self, state):
        '''If not already in state `state`, animates smoothly to it, taking
        the time given by self.anim_time. State may be either 'open'
        or 'closed'.

        '''
        if state == 'open':
            anim = Animation(_anim_progress=1,
                             duration=self.anim_time,
                             t=self.closing_transition)
            anim.start(self)
        elif state == 'closed':
            anim = Animation(_anim_progress=0,
                             duration=self.anim_time,
                             t=self.opening_transition)
            anim.start(self)
        else:
            raise NavigationDrawerException(
                'Invalid state received, should be one of `open` or `closed`')


    def on_touch_down(self, touch):
        col_self = self.collide_point(*touch.pos)
        col_side = self._side_panel.collide_point(*touch.pos)
        col_main = self._main_panel.collide_point(*touch.pos)

        if self._anim_progress < 0.001:  # i.e. closed
            valid_region = (self.x <=
                            touch.x <=
                            (self.x + self.touch_accept_width))
            if not valid_region:
                self._main_panel.on_touch_down(touch)
                return False
        else:
            if col_side and not self._main_above:
                self._side_panel.on_touch_down(touch)
                return False
            valid_region = (self._main_panel.x <=
                            touch.x <=
                            (self._main_panel.x + self._main_panel.width))
            if not valid_region:
                if self._main_above:
                    if col_main:
                        self._main_panel.on_touch_down(touch)
                    elif col_side:
                        self._side_panel.on_touch_down(touch)
                else:
                    if col_side:
                        self._side_panel.on_touch_down(touch)
                    elif col_main:
                        self._main_panel.on_touch_down(touch)
                return False
        Animation.cancel_all(self)
        self._anim_init_progress = self._anim_progress
        self._touch = touch
        touch.ud['type'] = self.state
        touch.ud['panels_jiggled'] = False  # If user moved panels back
                                            # and forth, don't default
                                            # to close on touch release
        touch.grab(self)
        return True

    def on_touch_move(self, touch):
        if touch is self._touch:
            dx = touch.x - touch.ox
            self._anim_progress = max(0, min(self._anim_init_progress +
                                            (dx / self.side_panel_width), 1))
            if self._anim_progress < 0.975:
                touch.ud['panels_jiggled'] = True
        else:
            super(NavigationDrawer, self).on_touch_move(touch)
            return

    def on_touch_up(self, touch):
        if touch is self._touch:
            self._touch = None
            init_state = touch.ud['type']
            touch.ungrab(self)
            jiggled = touch.ud['panels_jiggled']
            if init_state == 'open' and not jiggled:
                if self._anim_progress >= 0.975:
                        self.anim_to_state('closed')
                else:
                    self._anim_relax()
            else:
                self._anim_relax()
        else:
            super(NavigationDrawer, self).on_touch_up(touch)
            return

    def _anim_relax(self):
        '''Animates to the open or closed position, depending on whether the
        current position is past self.min_dist_to_open.

        '''
        if self._anim_progress > self.min_dist_to_open:
            self.anim_to_state('open')
        else:
            self.anim_to_state('closed')


class Code(object):
    '''
    For generating random code numbers
    '''

    def __init__(self):
        self.usedCodes = []

    def get_new_code(self):
        newCode = random.randrange(1000000000000, 9999999999999)
        while newCode not in self.usedCodes:
            newCode = random.randrange(1000000000000, 9999999999999)
            if newCode not in self.usedCodes:
                self.usedCodes.append(newCode)
        return newCode

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

"""
class OGStudents(object):

    def __init__(self):
        self.allStudents = []
        student = Student("Chen Feng", "Zhang", 1, "12E", "")
        student1 = Student("Jason", "Ng", 2, "12E", "Yearbook")
        student2 = Student("Alex", "Negoe", 3, "12E", "Coding Club")
        student3 = Student("Carson", "Tang", 4, "11E", "Coding Club")
        student4 = Student("Natalie", "Tam", 5, "12E", "")
        student5 = Student("Derek", "Shat", 6, "12E", "")
        student6 = Student("Erin", "Chin", 7, "11E", "Psychology Club, Coding Club")
        student7 = Student("Eryka", "Shi-Shun", 8, "12E", "Psychology Club, Coding Club")
        student8 = Student("Kun", "Lee", 9, "12E", "")
        student9 = Student("Grace", "Leung", 10, "12E", "Mural PALS, Psychology Club, Coding Club, Robotics")
        student10 = Student("Shawn", "Nimal", 11, "12E", "Coding Club")
        student11 = Student("Tony", "Ni", 12, "12E", "DECA")
        student12 = Student("Thomas", "Maglietta", 13, "12E", "Coding Club")
        student13 = Student("Allen", "Kim", 14, "12E", "Yearbook, Robotics, Mural PALS, Coding Club")
        student14 = Student("Bonnie", "Li", 15, "12E", "Economics Club, Coding Club")
        student15 = Student("Camille", "Law", 16, "12E", "French, Environmental")
        student16 = Student("Cecil", "Cao", 17, "12E", "Coding Club")
        student17 = Student("Chelsea", "Moon", 18, "12E", "Coding Club")
        student18 = Student("Felix", "Yang", 19, "12E", "Coding Club")
        student19 = Student("Joon", "Kim", 20, "12E", "Coding Club")
        student20 = Student("Sarah", "Wang", 21, "12E", "Coding Club")
        student21 = Student("Darya", "Pascarel", 22, "11E", "Robotics")
        student22 = Student("Caterina", "Paganelli", 23, "12E", "Band, Psychology Club, Politics, Sad Boi Club")

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
        self.allStudents.append(student22)

        q = db_test.return_all(db_test.con)
        for c in q:
            k = c[1].split()
            a = k[0]
            b = k[1]
            #print(a, b)
            studente = Student(a, b, c[0], c[2], "")
            self.allStudents.append(studente)



    # does not work yet
    '''
    def set_student_points(self, who, howMany):
        for i in self.allStudents:
            if i.get_student_name() == who:
                i.set_points(howMany)
    '''


class ChooseStudents(OGStudents):
    '''
    Individually selects students for a specific club
    '''

    def __init__(self, memberList):

        super(ChooseStudents, self).__init__()
        self.members = []

        for i in sorted(memberList):
            for j in self.allStudents:
                if j.get_student_name() == i:
                    self.members.append(j)

    def get_newList(self):
        return self.members


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
        selection = ""

        # finding amount of points for that activity
        if self.reward_list.adapter.selection:
            selection = self.reward_list.adapter.selection[0].text
            for student in self.rewarding_list:
                if student.get_activity_name() == selection:
                    pts = student.get_points()

        # finding selected students and distributing points
        for member, boxes in self.student_checkboxes.items():
            if boxes.active and (selection not in member.get_completed_activities() or selection in ["Club Attendance",
                                                                                                     "Winning Kahoots",
                                                                                                     "Ram of The Month"]):
                member.set_points(pts)
                if selection not in member.get_completed_activities():
                    member.add_completed_activity(selection)
                # below does not work like i want it to
                # self.grade12s_list._trigger_reset_populate()
            elif boxes.active:
                print("Sorry, ", member.get_student_name(), " has already \n recieved the points for this activity.")

    def view_student(self):
        if self.grade12s_list.adapter.selection:
            # getting selected item name
            selection = self.grade12s_list.adapter.selection[0].text

            # creating layout for tab
            co = GridLayout(cols=2)
            content = GridLayout(cols=1)
            help = GridLayout(cols=1)
            content.add_widget(Label(text="Student Name: " + selection))
            for i in self.grade12_list:
                if i.get_student_name() == selection:
                    content.add_widget(Label(text="Homeroom: " + i.get_homeroom()))
                    content.add_widget(Label(text="Student ID: " + str(i.get_id())))
                    content.add_widget(Label(text="Accumulated Points: " + str(i.get_points())))
                    content.add_widget(Label(text="Clubs Involved: " + "\n" + i.get_clubs()))
                    simple_list_adapter = SimpleListAdapter(
                        data=i.get_completed_activities(),
                        cls=Label)
            help.add_widget(Label(text='Student Rewards History', size_hint_y=None, height=40))
            theirRewardsList = ListView(adapter=simple_list_adapter)
            help.add_widget(theirRewardsList)
            co.add_widget(content)
            co.add_widget(help)
            popup = Popup(title=selection,
                          content=co,
                          size_hint=(None, None), size=(800, 500))
            popup.open()


class List(GridLayout):
    teacher_account = ObjectProperty()
    teacher_list = ListProperty()

    def __init__(self, teacherList: list, **kwargs):
        super(List, self).__init__(**kwargs)
        self.teacherList = teacherList
        for teacher in self.teacherList:
            self.teacher_list.append(teacher.get_firstName() + " " + teacher.get_lastName())

    def login(self):
        pass


class Login(Screen):
    username_text_input = ObjectProperty()
    password_text_input = ObjectProperty()

    def submit(self, userN, passW):
        global current_user
        loggedon = False
        for account in teachers:
            if userN == account.get_userName():
                loggedon = True
                if passW == account.get_password():
                    navigationdrawer = NavigationDrawer()

                    side_panel = BoxLayout(orientation='vertical')
                    side_panel.add_widget(
                        Label(text='~~~ * ------------- Menu ------------- * ~~~', size_hint_y=None, height=40))

                    homepage = Button(text='Homepage', background_color=(0, 1, 0.7, 1))
                    homepage.bind(on_press=lambda x: self.change_screen('Homepage'))

                    teach = Button(text='Teacher Profile', background_color=(0, 1, 0.7, 1))
                    teach.bind(on_press=lambda x: self.change_screen('Profile'))

                    gen = Button(text='General Activities', background_color=(0, 1, 0.7, 1))
                    gen.bind(on_press=lambda x: self.change_screen('General'))

                    cc = Button(text='Coding Club', background_color=(0, 1, 0.7, 1))
                    cc.bind(on_press=lambda x: self.change_screen('Coding'))

                    ro = Button(text='Robotics', background_color=(0, 1, 0.7, 1))
                    ro.bind(on_press=lambda x: self.change_screen('Robotics'))

                    scan = Button(text='Scanner', background_color=(0, 1, 0.7, 1))
                    scan.bind(on_press=lambda x: self.change_screen('Scanner'))

                    side_panel.add_widget(homepage)
                    side_panel.add_widget(teach)
                    side_panel.add_widget(gen)
                    side_panel.add_widget(cc)
                    side_panel.add_widget(ro)
                    side_panel.add_widget(scan)
                    navigationdrawer.add_widget(side_panel)

                    main_panel = screen_manager
                    navigationdrawer.add_widget(main_panel)

                    navigationdrawer.anim_type = 'slide_above_anim'
                    navigationdrawer.anim_to_state('open')

                    Window.add_widget(navigationdrawer)

                    current_user = account
                else:
                    passwPop = Popup(title="Login Error",
                                     content=Label(text="Wrong password"),
                                     background='atlas://data/images/defaulttheme/button_pressed',
                                     size_hint=(None, None), size=(400, 150))
                    passwPop.open()
        if not loggedon:
            userPop = Popup(title="Login Error",
                            content=Label(text="Invalid username"),
                            background='atlas://data/images/defaulttheme/button_pressed',
                            size_hint=(None, None), size=(400, 150))
            userPop.open()
    def change_screen(self, page):
        if page == "Homepage" and screen_manager.current != "screen_one":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.001
            screen_manager.current = "screen_one"
        elif page == "Profile" and screen_manager.current != "screen_two":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.001
            screen_manager.current = "screen_two"
        elif page == "General" and screen_manager.current != "screen_three":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.001
            screen_manager.current = "screen_three"
        elif page == "Coding" and screen_manager.current != "screen_four":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.001
            screen_manager.current = "screen_four"
        elif page == "Robotics" and screen_manager.current != "screen_five":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.001
            screen_manager.current = "screen_five"
        elif page == "Scanner" and screen_manager.current != "screen_six":
            screen_manager.transition.direction = "left"
            screen_manager.transition.duration = 0.001
            screen_manager.current = "screen_six"


class HomePageScreen(Screen):

    def __init__(self, **kwargs):
        super(HomePageScreen, self).__init__(**kwargs)
        self.add_widget(Start())

        manager = AccountManager()
        teacherList = manager.get_list_teachers()
        layout = List(teacherList)
        self.add_widget(layout)


class ProfileScreen(Screen):

    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        self.add_widget(TeacherProfile())


class GeneralScreen(Screen):

    def __init__(self, **kwargs):
        super(GeneralScreen, self).__init__(**kwargs)

        # Creates all the members
        members = ChooseStudents(["Chen Feng Zhang", "Jason Ng", "Carson Tang", "Natalie Tam",
                                  "Derek Shat", "Kun Lee", "Shawn Nimal", "Tony Ni", "Thomas Maglietta",
                                  "Caterina Paganelli", "Yelix Fang", "Donner Cong", "Tarson Cang", "Zhen Cheng Feng",
                                  "Ching Chong", "Wing Wong", "Grade Nine"])
        student_list = members.get_newList()

        # Creates all the activities
        rewards = []
        act = Rewards("Ram of The Month", "Does good in life", "Once a month", 20)
        act1 = Rewards("Participate in Inside Ride 2017", "Riding bikes for cancer \n and raising money", "Sometime",
                       100)
        act2 = Rewards("Attend Hockey Buyout 2018", "Watching teachers play \n hockey, school spirit", "Sometime", 50)
        act3 = Rewards("Attend School Dance 2018", "Grade 9 Dance, \n Semi-formal, Formal", "Sometime", 25)
        act4 = Rewards("Participate in Christmas Concert 2018", "Singing, Dancing, etc.", "Sometime", 60)
        act5 = Rewards("Attend Christmas Concert 2018", "Watching students perform", "Sometime", 10)
        act6 = Rewards("Participate in Expresso Self 2018", "Singing, Dancing, etc.", "Sometime", 60)
        act7 = Rewards("Attend Expresso Self 2018", "Watching students perform", "Sometime", 10)
        act8 = Rewards("Winning Kahoots", "Getting Top 5 in \n cafeteria kahoots", "Sometime", 70)
        act9 = Rewards("Participate in School Play 2019", "Acting, Singing, Dancing, etc.", "Sometime", 60)
        act10 = Rewards("Watching School Play 2019", "Watching fun school plays", "Sometime", 10)
        act11 = Rewards("Attend 'Revolution' Art Show 2019", "Looking at some nice art", "Sometime", 40)

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
        rewards.append(act11)

        # Adds the members and activities to the tabs
        layout = BaseTabs(student_list, rewards, members)
        self.add_widget(layout)


class ClubOneScreen(Screen):

    def __init__(self, **kwargs):
        super(ClubOneScreen, self).__init__(**kwargs)

        # Creates all the members
        members = ChooseStudents(["Allen Kim", "Bonnie Li", "Camille Law", "Carson Tang", "Cecil Cao", "Chelsea Moon",
                                  "Erin Chin", "Eryka Shi-Shun", "Felix Yang", "Grace Leung", "Joon Kim", "Sarah Wang",
                                  "Thomas Maglietta"])
        student_list = members.get_newList()

        # Creates all the activities
        rewards = []
        act = Rewards("Club Attendance", "Attends a weekly club meeting", "Every week", 1)
        act1 = Rewards("Coding Competition 2019", "DMOJ", "February 20th", 20)
        rewards.append(act)
        rewards.append(act1)

        # Adds the members and activities to the tabs
        layout = BaseTabs(student_list, rewards, members)
        self.add_widget(layout)


class ClubTwoScreen(Screen):

    def __init__(self, **kwargs):
        super(ClubTwoScreen, self).__init__(**kwargs)


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


class Scanner(Screen):
    def __init__(self, **kwargs):
        super(Scanner, self).__init__(**kwargs)
        self.img1 = Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)
        # opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0 / 33.0)

# Adding Teachers
teachers = []
teachers.append(Teacher("Eric F", 1234, "eric", "hiCarson"))

empty_acc = Teacher("empty", None, "", "")
current_user = empty_acc

# Adding screens to the Screen Manager
screen_manager.add_widget(HomePageScreen(name="screen_one"))
screen_manager.add_widget(ProfileScreen(name="screen_two"))
screen_manager.add_widget(GeneralScreen(name="screen_three"))
screen_manager.add_widget(ClubOneScreen(name="screen_four"))
screen_manager.add_widget(ClubTwoScreen(name="screen_five"))
screen_manager.add_widget(Scanner(name="screen_six"))


class TeacherApp(App):

    def build(self):
        Window.add_widget(Login())



TeacherApp().run()
"""