# Importing the Kivy application, layouts, and buttons

import random, cv2, pyzbar.pyzbar as pyzbar, numpy as np, barcode
from barcode.writer import ImageWriter
from kivy.app import App
from RRTAA.BarcodeScanner import Scanner
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.uix.listview import ListView

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
from kivy.uix.stencilview import StencilView
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.properties import (ObjectProperty, NumericProperty, OptionProperty,
                             BooleanProperty, StringProperty, ListProperty)
from kivy.lang import Builder
from kivy.graphics.texture import Texture
from kivy.uix.rst import RstDocument

"""
--------------------------------------------------------------------------------------------
Name:		Main.py
Purpose:		
An app that allows teachers to view activities and students, award points, and scan barcodes.

Author:		Leung G.  Tang C. 

Created:		15.12.2018
--------------------------------------------------------------------------------------------
"""

# Setting Screen Manager as a variable
screen_manager = ScreenManager()

# Creating a Kivy text file in this window
Builder.load_string("""
#: import main Main
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton

<CustLabel@Label>
    color: 0, 0, 1, 1

<CustButton@Button>:
    font_size: 18
    color: 1, 1, 1, 1 # In RBG then alpha
    size: 450, 25
    background_color: 21/ 255, 30/255, 11/ 255, 1.0

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

<SideBar>:
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
            height: 40
            text: "WELCOME! WELCOME! WELCOME! WELCOME! WELCOME! WELCOME!"
            valign: 'middle'
            
        Label:
            size_hint_y: None
            height: 40
            text: "In this app, you will be able to reward points to students for completing activities!"
            valign: 'middle'
            
        Image:
            source: 'robbie.jpg'
            size: 400, 400
            pos: (400,400)

<TeacherProfile>:
    orientation: "vertical"   
    cols: 2
    rows: 5
    padding: 0
    spacing: 0
    
    Image:
        source: 'eric.jpg'
        size: 300, 400
    
    BoxLayout:
        orientation: "vertical"
        size_hint_x: 1
        
        CustButton:
            text: " "
            size_hint_y: None
            height: 30
            
        CustButton:
            text: '\\n'.join(("Welcome to your profile, Mr. Fabroa.", \
            "----------------------------------------------------------", " ", " ", \
            "Name: Eric Fabroa", " ", "User Id: eric", " ", "School: St. Robert Catholic High School", " ", \
            "Courses: ICS4U1a, ICS4U1b", " ", "Club Coordination: Coding Club, Robotics", " ", \
            "Bio: A teacher yo."))
            height: 600
            size_hint_y: 1.5
       
        CustButton:
            text: " "
            size_hint_y: 1
            
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
                    GridLayout:     
                        cols: 1
                        rows: 2                  
                        ListView:
                            id: rewards_list_view
                            adapter:
                                ListAdapter(data= root.rewardNames, cls= main.ListItemButton)
                        Button:
                            background_color: (0, 0, 0, .6)
                            text: "View Activity"
                            size_hint_y: None
                            size_hint_x: 1
                            height: 50
                            on_press: root.view_activity()
                TabbedPanelItem:
                    text: "Student List"
                    GridLayout:
                        cols: 1
                        rows: 2
                        ListView:
                            id: grade12ss_list_view
                            adapter:
                                ListAdapter(data= root.names, cls= main.ListItemButton)
                        Button:
                            background_color: (0, 0, 0, .6)
                            text: "View Student"
                            size_hint_y: None
                            size_hint_x: 1
                            height: 50
                            on_press: root.view_student()
    
""")

initCamera = False


def toggleCamera():
    global initCamera
    if initCamera: initCamera = False
    else: initCamera = True


class Start(GridLayout):
    '''
    Adds pictures and messages to the Homepage Screen
    '''

    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)


class TeacherProfile(GridLayout):
    '''
    Creates a Teacher Profile Screen for Mr. Fabroa
    '''

    def __init__(self, **kwargs):
        super(TeacherProfile, self).__init__(**kwargs)


class SideBarException(Exception):
    '''
    Raised when add_widget or remove_widget called incorrectly the SideBar
    '''


class SideBar(StencilView):
    '''
    Creates sidebar and its animation
    '''

    # Internal references for side, main and image widgets
    _side_panel = ObjectProperty()
    _main_panel = ObjectProperty()
    _join_image = ObjectProperty()

    side_panel = ObjectProperty(None, allownone=True)
    main_panel = ObjectProperty(None, allownone=True)

    # Appearance properties
    side_panel_width = NumericProperty()
    separator_image_width = NumericProperty(dp(1))

    # Touch properties
    touch_accept_width = NumericProperty('14dp')
    _touch = ObjectProperty(None, allownone=True)

    # Animation properties
    state = OptionProperty('open', options=('open', 'closed'))
    anim_time = NumericProperty(0.3)
    min_dist_to_open = NumericProperty(0.7)
    _anim_progress = NumericProperty(0)
    _anim_init_progress = NumericProperty(0)

    # Animation controls
    top_panel = OptionProperty('main', options=['main', 'side'])
    _main_above = BooleanProperty(True)
    side_panel_init_offset = NumericProperty(0.5)
    side_panel_darkness = NumericProperty(0.8)
    side_panel_opacity = NumericProperty(1)
    main_panel_final_offset = NumericProperty(1)
    main_panel_darkness = NumericProperty(0)
    opening_transition = StringProperty('out_cubic')
    closing_transition = StringProperty('in_cubic')
    anim_type = OptionProperty('reveal_from_below',
                               options=['slide_above_anim'])

    def __init__(self, **kwargs):
        super(SideBar, self).__init__(**kwargs)
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
            super(SideBar, self).add_widget(widget)
            self._side_panel = widget
        elif len(self.children) == 1:
            super(SideBar, self).add_widget(widget)
            self._main_panel = widget
        elif len(self.children) == 2:
            super(SideBar, self).add_widget(widget)
            self._join_image = widget
        elif self.side_panel is None:
            self._side_panel.add_widget(widget)
            self.side_panel = widget
        elif self.main_panel is None:
            self._main_panel.add_widget(widget)
            self.main_panel = widget
        else:
            raise SideBarException(
                'Can\'t add more than two widgets'
                'directly to NavigationDrawer')

    def anim_to_state(self, state):
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
            raise SideBarException(
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
            super(SideBar, self).on_touch_move(touch)
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
            super(SideBar, self).on_touch_up(touch)
            return

    def _anim_relax(self):
        if self._anim_progress > self.min_dist_to_open:
            self.anim_to_state('open')
        else:
            self.anim_to_state('closed')


class Code(object):
    '''
    For generating random code numbers
    '''

    def __init__(self):
        self.__usedCodes = []

    def get_new_code(self):
        newCode = random.randrange(0, 9999999)
        while newCode not in self.__usedCodes:
            newCode = random.randrange(0, 9999999)
            if newCode not in self.__usedCodes:
                self.__usedCodes.append(newCode)
        return str(newCode)


class Teacher(object):
    '''
    Constructor for Teacher
    '''

    def __init__(self, firstName: str, lastName: str, userName: str, password: str):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__userName = userName
        self.__password = password

    def get_firstName(self) -> str:
        return self.__firstName

    def get_lastName(self) -> str:
        return self.__lastName

    def get_userName(self) -> str:
        return self.__userName

    def get_password(self) -> str:
        return self.__password

    def set_firstName(self, new_firstName: str):
        self.__firstName = new_firstName

    def set_lastName(self, new_lastName: str):
        self.__lastName = new_lastName

    def set_userName(self, new_userName: str):
        self.__userName = new_userName

    def set_password(self, new_password: str):
        self.__password = new_password


class BaseTabs(GridLayout):
    '''
    Makes the tabs look good, distribute points with checkboxes
    '''

    # I'm not quite sure what these do but they are id's that refer to the tab
    reward_list = ObjectProperty()
    grade12s_list = ObjectProperty()

    # These are the actual lists still as properties so i can call their other methods
    grade12_list = ObjectProperty()
    rewarding_list = ObjectProperty()

    # These are the actual lists of just names that make the tab lists
    names = ListProperty()
    rewardNames = ListProperty()

    def __init__(self, studentList, rewardList, **kwargs):
        super(BaseTabs, self).__init__(**kwargs)
        from RRTAA import db_test
        self.codes = Code()

        # members of the clubs as objects
        self.grade12_list = []
        for p in studentList:
            self.grade12_list.append(db_test.get_by_id(db_test.con, p)[0])
        self.rewarding_list = rewardList

        # creating the list of just member names
        for i in self.grade12_list:
            self.names.append(i[1])
        for j in self.rewarding_list:
            self.rewardNames.append(j[1])
        self.names = sorted(self.names)

        # a dictionary? for tying certain checkboxes to students
        self.student_checkboxes = {}

    # for viewing information about certain activities
    def view_activity(self):
        self.update_info()
        if self.reward_list.adapter.selection:
            # the selected item name
            selection = self.reward_list.adapter.selection[0].text

            # creating layout in the tab
            content = GridLayout(cols=2)

            col1 = GridLayout(cols=1)
            col1.add_widget(Label(text="Activity Name: " + selection))
            for rewardObject in self.rewarding_list:
                from RRTAA import db_test
                newCode = self.codes.get_new_code()

                if rewardObject[1] == selection:
                    col1.add_widget(Label(text="Date Completed: " + rewardObject[3]))
                    col1.add_widget(Label(text="Amount of Points: " + str(rewardObject[4])))
                    col1.add_widget(Label(text="Code: " + newCode))
                    db_test.update_codes(db_test.con, (rewardObject[5] + '.' + newCode, rewardObject[1]))
                    col1.add_widget(Label(text="Activity Participants: "))
                    simple_list_adapter = SimpleListAdapter(
                        data=rewardObject[6].split('.')[1:],
                        cls=Label)
                    participants = ListView(adapter=simple_list_adapter)
                    col1.add_widget(participants)
                    col1.add_widget(RstDocument(text="Activity Description: " + rewardObject[2]))

            col2 = GridLayout(cols=2)
            for student in self.grade12_list:
                col2.add_widget(Label(text=student[1]))
                box = CheckBox()
                self.student_checkboxes[student] = box
                col2.add_widget(box)

            # Reward Points Button
            givePoints = Button(text='Reward Points',
                                size_hint_y=None,
                                height=40)
            givePoints.bind(on_press=self.get_active_boxes)
            col1.add_widget(givePoints)

            # adds the layout to the popup tab
            content.add_widget(col1)
            content.add_widget(col2)
            popup = Popup(title=selection,
                          content=content,
                          size_hint=(None, None), size=(800, 500))
            popup.open()

    # for distributing points
    def get_active_boxes(self, *args):
        self.update_info()
        pts = 0
        selection = ""

        # finding amount of points for that activity
        if self.reward_list.adapter.selection:
            selection = self.reward_list.adapter.selection[0].text
            for student in self.rewarding_list:
                if student[1] == selection:
                    pts = student[4]

        # finding selected students and distributing points
        for member, boxes in self.student_checkboxes.items():
            from RRTAA import db_test
            completed_activities = member[6].split('.')
            if boxes.active and (selection not in completed_activities or selection in ['Mass', 'Club Attendance', 'Winning Kahoots', 'Ram of the Month']):
                db_test.update_score(db_test.con, (member[3] + pts, member[1]))
                if selection not in completed_activities:
                    db_test.update_history(db_test.con, (member[6] + '.' + selection, member[1]))
                    activity = db_test.get_by_act(db_test.con, selection)[0]
                    if member[1] not in activity[6].split('.')[1:]:
                        db_test.update_attendants(db_test.con, (activity[6] + '.' + member[1], activity[1]))
            elif boxes.active:
                print("Sorry, ", member[1], " has already \n recieved the points for this activity.")

    # for viewing information on a certain student
    def view_student(self):
        self.update_info()
        if self.grade12s_list.adapter.selection:
            # getting selected item name
            selection = self.grade12s_list.adapter.selection[0].text

            # creating layout for tab
            content = GridLayout(cols=2)
            col1 = GridLayout(cols=1)
            col2 = GridLayout(cols=1)
            col1.add_widget(Label(text="Student Name: " + selection))
            for i in self.grade12_list:
                if i[1] == selection:
                    col1.add_widget(Label(text="Grade: " + i[2]))
                    col1.add_widget(Label(text="Student ID: " + str(i[4])))
                    col1.add_widget(Label(text="Accumulated Points: " + str(i[3])))
                    simple_list_adapter = SimpleListAdapter(
                        data=i[6].split('.')[1:],
                        cls=Label)

            col2.add_widget(Label(text='Student Rewards History', size_hint_y=None, height=40))
            activity_history = ListView(adapter=simple_list_adapter)
            col2.add_widget(activity_history)
            content.add_widget(col1)
            content.add_widget(col2)
            popup = Popup(title=selection,
                          content=content,
                          size_hint=(None, None), size=(800, 500))
            popup.open()

    # Updates the student lists by re-pulling from the database
    def update_info(self):
        from RRTAA import db_test
        self.grade12_list = []
        self.rewarding_list = []
        for m in self.names:
            self.grade12_list.append(db_test.get_by_name(db_test.con, m)[0])
        for n in self.rewardNames:
            self.rewarding_list.append(db_test.get_by_act(db_test.con, n)[0])


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


class Scanner(Screen):
    def __init__(self, **kwargs):
        super(Scanner, self).__init__(**kwargs)
        # sets the refresh rate
        self.my_camera = KivyCamera(fps=12)
        self.add_widget(self.my_camera)


def hashFunction(id: str)->int:
    '''
    Returns 12 digit id which corresponds to any id user provides
    Theoretically no 2 string ids should give the same returned id
    :param id: str, user id
    :return: int, 12 digit id
    '''
    hash = 5381
    mod = 998244353
    for i in id:
        hash = ((hash << 5)+hash) + ord(i)
    hash %= mod
    while len(str(hash)) != 12:
       hash = int(str(hash)+"0")
    return hash


def generate_barcode(userID):
    number = userID
    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(str(number), writer=ImageWriter())
    code = ean.save('barcode'+str(userID))


class KivyCamera(Image):
    '''
    Adding a camera, scans screen and returns code
    '''

    def __init__(self, capture=None, fps=0, **kwargs):
        from RRTAA import db_test
        super(KivyCamera, self).__init__(**kwargs)
        # start screen capture
        self.capture = cv2.VideoCapture(0)
        # repeat screen capture // in order to constantly capture image and check for barcode/qrcode
        Clock.schedule_interval(self.update, 1.0 / fps)
        self.hashed_id = {}
        for i in db_test.return_id(db_test.con):
            self.hashed_id[i[0]] = hashFunction(i[0])
            generate_barcode(self.hashed_id[i[0]])

    def decode(self, im):
        # return list of values decoded
        decodedObjects = pyzbar.decode(im)
        for obj in decodedObjects:
            print('Type : ', obj.type)
            print('Data : ', obj.data, '\n')
            id = str(obj.data).strip('b').strip('\'')
            print('ID : ', id, '\n')
            # ASSIGN USER WITH THIS ID, X POINTS
            self.reward_barcode_points(id)
            # reward_barcode_id(id) -- line 685
        return decodedObjects

    def display(self, im, decodedObjects):
        # convex hull to get boundaries of barcode/qrcode
        for decodedObject in decodedObjects:
            points = decodedObject.polygon
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                hull = list(map(tuple, np.squeeze(hull)))
            else:
                hull = points
            n = len(hull)
            for j in range(0, n):
                cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)
        cv2.imshow("Results", im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def update(self, filler):
        # start screen capture
        ret_val, img = self.capture.read()
        if ret_val:
            # flip the image
            buf1 = cv2.flip(img, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image
            self.texture = image_texture
            # if user is on scanner screen
            if initCamera:
                # recapture image
                ret_val, img = self.capture.read()
                # save and reread image
                cv2.imwrite("code.png", img)
                im = cv2.imread("code.png", 0)
                decodedObjects = self.decode(im)
                self.texture = image_texture
                # break if user clicks 'esc' or no barcode/qrcode found
                if len(decodedObjects) != 0 or cv2.waitKey(1) == 27:
                    # if code found, display
                    self.display(im, decodedObjects)
                    #toggleCamera() -> to stop scanning after barcode found

    def reward_barcode_points(self, rewardID):
        from RRTAA import db_test

        for student in db_test.return_all(db_test.con): # does this even work
            if str(self.hashed_id[student[4]]) == str(rewardID)[:-1]: # idk
                db_test.update_score(db_test.con, (student[3] + 8000, student [1])) # how do i give points here)
                toggleCamera() # stops scanning after barcode found


class Login(Screen):
    '''
    Creates login functionality for teachers or just Mr. Fabroa
    '''

    username_text_input = ObjectProperty()
    password_text_input = ObjectProperty()

    def submit(self, userN, passW):
        global current_user
        loggedon = False
        for account in teachers:
            if userN == account.get_userName():
                loggedon = True
                if passW == account.get_password():
                    navigationdrawer = SideBar()

                    side_panel = BoxLayout(orientation='vertical')
                    side_panel.add_widget(
                        Label(text='~~~ * ------------- Menu ------------- * ~~~', size_hint_y=None, height=40))

                    homepage = Button(text='Homepage', background_color=(0, 1, 0.7, 1))
                    homepage.bind(on_press=lambda x: self.change_screen('Homepage'))

                    teach = Button(text='Teacher Profile', background_color=(0, 1, 0.7, 1))
                    teach.bind(on_press=lambda x: self.change_screen('Profile'))

                    general = Button(text='General Activities', background_color=(0, 1, 0.7, 1))
                    general.bind(on_press=lambda x: self.change_screen('General'))

                    coding = Button(text='Coding Club', background_color=(0, 1, 0.7, 1))
                    coding.bind(on_press=lambda x: self.change_screen('Coding'))

                    robotics = Button(text='Robotics', background_color=(0, 1, 0.7, 1))
                    robotics.bind(on_press=lambda x: self.change_screen('Robotics'))

                    scanner = Button(text='Scanner', background_color=(0, 1, 0.7, 1))
                    scanner.bind(on_press=lambda x: self.change_screen('Scanner'))

                    side_panel.add_widget(homepage)
                    side_panel.add_widget(teach)
                    side_panel.add_widget(general)
                    side_panel.add_widget(coding)
                    side_panel.add_widget(robotics)
                    side_panel.add_widget(scanner)
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

    # for changing the current displayed screen
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
            toggleCamera()


class HomePageScreen(Screen):
    '''
    Creates the HomeScreen
    '''

    def __init__(self, **kwargs):
        super(HomePageScreen, self).__init__(**kwargs)
        self.add_widget(Start())


class ProfileScreen(Screen):
    '''
    Creates teacher profile page
    '''

    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)
        self.add_widget(TeacherProfile())


class GeneralScreen(Screen):
    '''
    The general screen for general school activities not specific to any club
    '''

    def __init__(self, **kwargs):
        super(GeneralScreen, self).__init__(**kwargs)
        from RRTAA import db_test

        # Creates all the members
        student_list = ["userid", "mathg0d", "ballsDPcoder", "chenfengzhang", "chingchangchong", "wingwangwong", "minecraftman1022"]

        # Creates all the activities
        rewards = []
        for i in db_test.return_act(db_test.con):
            if i[1] not in ['Club Attendance', 'Coding Competition 2019']:
                rewards.append(db_test.get_by_act(db_test.con, i[1])[0])

        # Adds the members and activities to the tabs
        layout = BaseTabs(student_list, rewards)
        self.add_widget(layout)


class ClubOneScreen(Screen):
    '''
    Creates a reward page for coding club members
    '''

    def __init__(self, **kwargs):
        super(ClubOneScreen, self).__init__(**kwargs)
        from RRTAA import db_test

        # Creates all the members
        student_list = ["userid", "mathg0d", "ballsDPcoder", "chenfengzhang"]

        # Creates all the activities
        rewards = []
        rewards.append(db_test.get_by_act(db_test.con, 'Club Attendance')[0])
        rewards.append(db_test.get_by_act(db_test.con, 'Coding Competition 2019')[0])

        # Adds the members and activities to the tabs
        layout = BaseTabs(student_list, rewards)
        self.add_widget(layout)


class ClubTwoScreen(Screen):
    '''
    Creates a reward page for robotics members
    '''

    def __init__(self, **kwargs):
        super(ClubTwoScreen, self).__init__(**kwargs)
        from RRTAA import db_test

        # Creates all the members
        student_list = ["chingchangchong", "wingwangwong", "minecraftman1022"]

        # Creates all the activities
        rewards = []
        rewards.append(db_test.get_by_act(db_test.con, 'Club Attendance')[0])

        # Adds the members and activities to the tabs
        layout = BaseTabs(student_list, rewards)
        self.add_widget(layout)


# Adding Teachers
teachers = []
teachers.append(Teacher("Eric F", 1234, "eric", "hiCarson"))
teachers.append(Teacher("grace", 8884, "gg", "g"))
empty_acc = Teacher("empty", None, "", "")
current_user = empty_acc

# Adding screens to the Screen Manager
screen_manager.add_widget(HomePageScreen(name="screen_one"))
screen_manager.add_widget(ProfileScreen(name="screen_two"))
screen_manager.add_widget(GeneralScreen(name="screen_three"))
screen_manager.add_widget(ClubOneScreen(name="screen_four"))
screen_manager.add_widget(ClubTwoScreen(name="screen_five"))
screen_manager.add_widget(Scanner(name="screen_six"))


# Builds the App
class TeacherApp(App):

    def build(self):
        Window.add_widget(Login())

    # exits camera
    def on_stop(self):
        pass

    def on_pause(self):
        return True


TeacherApp().run()
