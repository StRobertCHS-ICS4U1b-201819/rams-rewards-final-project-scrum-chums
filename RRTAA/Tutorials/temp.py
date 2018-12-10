import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.pagelayout import PageLayout

# test 1 - labels
class TestApp(App):
    def build(self):
        return Label()

test = TestApp()
# test.run()

# test 2 - widgets
class CustomWidget(Widget):
    pass
class CustomWidgetApp(App):

    def build(self):
        return CustomWidget()

customWidget = CustomWidgetApp()
customWidget.run()

# test 3 - float layout
class FloatingApp(App):

    def build(self):
        return FloatLayout()

flApp = FloatingApp()
# flApp.run()

# test 4 - grid layout

class GridLayoutApp(App):

    def build(self):
        return GridLayout()

glApp = GridLayoutApp()
# glApp.run()

# test 5 - box layout

class BoxLayoutApp(App):

    def build(self):
        return BoxLayout()

blApp = BoxLayoutApp()
#blApp.run()

# test 6 - stack layout

class StackLayoutApp(App):

    def build(self):
        return StackLayout()

slApp = StackLayoutApp()
# slApp.run()

# test 7 - page layout

class PageLayoutApp(App):

    def build(self):
        return PageLayout()

plApp = PageLayoutApp()
# plApp.run()

# test 8 - making a calculator

class CalcGridLayout(GridLayout):

    # making the equal sign work / the actual calculations with built in function --eval--
    def calculate(self, calculation): # calculation will be whatever is in the text area entry
        if calculation:
            try:
                self.display.text = str(eval(calculation))# gets what is in entry with calculation and changes the display
            except Exception:
                self.display.text = "yo that was illegal, erin, who you is"

class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()

calcApp = CalculatorApp()
# calcApp.run()