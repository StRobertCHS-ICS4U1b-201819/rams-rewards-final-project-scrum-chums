from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.button import Label
from kivy.core.window import Window


class CarouselApp(App):
    def build(self):
        Window.clearcolor = (0.3725, 0.6196, 0.6275, 1)
        carousel = Carousel(direction='left')
        for i in range(1):
            carousel.add_widget(Label(text="Activity Name: " + str(i), size_hint_y=None, height=40))
        return carousel


CarouselApp().run()