# images have to be in same file to register
import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class SampleGridlayout(GridLayout):
    pass

class SampleApp(App):
    def build(self):
        return SampleGridlayout()

sample_app = SampleApp()
sample_app.run()