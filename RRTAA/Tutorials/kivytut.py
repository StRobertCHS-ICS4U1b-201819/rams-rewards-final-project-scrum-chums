# images have to be in same file to register
import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup

class SampleGridlayout(GridLayout):
    pass

class SampleApp(App):
    def build(self):
        return SampleGridlayout()

sample_app = SampleApp()
# sample_app.run()

# Tutorial 5
class CustomPopup(Popup):
    pass

class SampBoxLayout(BoxLayout):
    # to talk back and forth between kivy and python file
    checkbox_is_active = ObjectProperty(False)

    def checkbox_18_clicked(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox is Unchecked")

    # radio buttons are grouped checkboxes, only one radio button can be active at a time
    blue = ObjectProperty(True)
    red = ObjectProperty(False)
    green = ObjectProperty(False)

    def switch_on(self, instance, value):
        if value is True:
            print("Switch on")
        else:
            print("Switch off")

    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

    def spinner_clicked(self, value):
        print("Spinner Value: " + value)

class Sample2App(App):
    def build(self):
        # changes colour for whole window
        Window.clearcolor = (1, 1, 1, 1)
        return SampBoxLayout()

sample_app2 = Sample2App()
sample_app2.run()