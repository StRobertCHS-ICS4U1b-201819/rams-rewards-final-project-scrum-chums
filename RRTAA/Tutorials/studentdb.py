import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout # box and grid layouts work very well
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton # an adapter to select items


class StudentListButton(ListItemButton):
    pass

class SampBoxLayout(BoxLayout):

    def spinner_clicked(self, value):
        print("Spinner Value: " + value)

class StudentDB(BoxLayout):

    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    student_id_text_input = ObjectProperty()
    grade12_list = ObjectProperty()

    def submit_student(self):
        # Get the students name from text inputs
        student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text

        # Add student to ListView
        self.grade12_list.adapter.data.extend([student_name])

        # Reset the ListView
        self.grade12_list._trigger_reset_populate()

    def delete_student(self):
        # If a list item is selected
        # communicates to list with an adapter
        if self.grade12_list.adapter.selection:

            # Get the text rom the item selected
            selection = self.grade12_list.adapter.selection[0].text

            # Remove the matching item
            self.grade12_list.adapter.data.remove(selection)

            # Reset the ListView
            self.grade12_list._trigger_reset_populate()

    def replace_student(self):
        # If a list item is selected
        if self.grade12_list.adapter.selection:

            # Get the text rom the item selected
            selection = self.grade12_list.adapter.selection[0].text

            # Remove the matching item
            self.grade12_list.adapter.data.remove(selection)

            # Get the students name from text inputs
            student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text

            # Add the updated data to the list
            self.grade12_list.adapter.data.extend([student_name])

            # Reset the ListView
            self.grade12_list._trigger_reset_populate()


class StudentDBApp(App):
    def build(self):
        return StudentDB()

dbApp = StudentDBApp()
dbApp.run()

