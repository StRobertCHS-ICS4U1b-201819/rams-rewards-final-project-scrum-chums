from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.core.window import Window
from kivy.uix.popup import Popup


Builder.load_string("""
#: import main m
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton
<CustLabel@Label>
    color: 0, 0, 0, 1

<SampBoxLayout>:
    orientation: "vertical"
    padding: 10
    spacing: 10

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


<StudentDB>:
    orientation: "vertical"
    first_name_text_input: first_name
    last_name_text_input: last_name
    student_id_text_input: student_id
    activity_name_text_input: activity_name
    points_rewarded_text_input: points_rewarded
    reward_list: rewards_list_view
    grade12_list: grade12s_list_view
    padding: 10
    spacing: 10
    
    

    BoxLayout:
        size_hint_y: None
        height: "30dp"
        size_hint_x: 1

        Label:
            text: "First name: "
        TextInput:
            id: first_name
        Label:
            text: "Last name: "
        TextInput:
            id: last_name
        Label:
            text: "ID: "
            size_hint_x: 0.5
        TextInput:
            id: student_id
            
        Button:
            text: "Submit Student"            
            on_press: root.submit_student()

    BoxLayout:
        size_hint_y: None
        height: "30dp"
        size_hint_x: 1

        Label:
            text: "Activity Name: "
        TextInput:
            id: activity_name
        Label:
            text: "Point Value: "
        TextInput:
            id: points_rewarded
        Button:
            text: "Submit Activity"
            on_press: root.submit_activity()
        

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Button:
            text: "View"
            size_hint_x: 10
            on_press: root.delete_student()
            
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
                    ListView:
                        id: rewards_list_view
                        adapter:
                            ListAdapter(data= [""], cls= main.RewardListButton)

                TabbedPanelItem:
                    text: "Student List"
                    ListView:
                        id: grade12s_list_view
                        adapter:
                            ListAdapter(data= ["Grace Leung"], cls= main.StudentListButton)


""")

class StudentListButton(ListItemButton):
    pass

class RewardListButton(ListItemButton):
    pass

class CustomPopup(Popup):
    pass



class SampBoxLayout(BoxLayout):

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

class StudentDB(BoxLayout):

    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    student_id_text_input = ObjectProperty()
    activity_name_text_input = ObjectProperty()
    points_rewarded_text_input = ObjectProperty()
    reward_list = ObjectProperty()
    grade12_list = ObjectProperty()



    def submit_student(self):
        student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text

        self.grade12_list.adapter.data.extend([student_name])
        self.grade12_list._trigger_reset_populate()

    def submit_activity(self):
        activity = self.activity_name_text_input.text + ", " + self.points_rewarded_text_input.text + " pts"

        self.reward_list.adapter.data.extend([activity])
        self.reward_list._trigger_reset_populate()

    def delete_student(self):
        if self.grade12_list.adapter.selection:
            selection = self.grade12_list.adapter.selection[0].text
            popup = Popup(title= selection,
                          size_hint=(None, None), size=(400, 400))
            popup.open()



class ListScreen(Screen):
    def __init__(self, **kwargs):
        super(ListScreen, self).__init__(**kwargs)
        layout = StudentDB()
        self.add_widget(layout)
        layout2 = SampBoxLayout()
        self.add_widget(layout2)

class ListScreen2(Screen):
    def __init__(self, **kwargs):
        super(ListScreen2, self).__init__(**kwargs)
        layout = StudentDB()
        self.add_widget(layout)

        layout2 = SampBoxLayout()
        self.add_widget(layout2)


class ListScreen3(Screen):
    def __init__(self, **kwargs):
        super(ListScreen3, self).__init__(**kwargs)
        layout = StudentDB()
        self.add_widget(layout)

        layout2 = SampBoxLayout()
        self.add_widget(layout2)

class ListScreen4(Screen):
    def __init__(self, **kwargs):
        super(ListScreen4, self).__init__(**kwargs)
        layout = StudentDB()
        self.add_widget(layout)

        layout2 = SampBoxLayout()
        self.add_widget(layout2)



class ListScreen5(Screen):
    def __init__(self, **kwargs):
        super(ListScreen5, self).__init__(**kwargs)
        layout = StudentDB()
        self.add_widget(layout)

        layout2 = SampBoxLayout()
        self.add_widget(layout2)

screen_manager = ScreenManager()
screen_manager.add_widget(ListScreen(name= "screen_one"))
screen_manager.add_widget(ListScreen2(name= "screen_two"))
screen_manager.add_widget(ListScreen3(name= "screen_three"))
screen_manager.add_widget(ListScreen4(name= "screen_four"))
screen_manager.add_widget(ListScreen5(name= "screen_five"))




class ExampleApp(App):

    def build(self):
        Window.clearcolor = (0.04, 0.1, .6, 1)
        return screen_manager


ExampleApp().run()