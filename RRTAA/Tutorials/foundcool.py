
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.stencilview import StencilView
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.properties import (ObjectProperty, NumericProperty, OptionProperty,
                             BooleanProperty, StringProperty)
from kivy.lang import Builder


Builder.load_string('''
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
''')


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
    state = OptionProperty('closed', options=('open', 'closed'))
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

    def toggle_state(self, animate=True):
        '''Toggles from open to closed or vice versa, optionally animating or
        simply jumping.'''
        if self.state == 'open':
            if animate:
                self.anim_to_state('closed')
            else:
                self.state = 'closed'
        elif self.state == 'closed':
            if animate:
                self.anim_to_state('open')
            else:
                self.state = 'open'

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


if __name__ == '__main__':
    from kivy.base import runTouchApp
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.uix.popup import Popup
    from kivy.uix.image import Image
    from kivy.core.window import Window

    navigationdrawer = NavigationDrawer()

    side_panel = BoxLayout(orientation='vertical')
    side_panel.add_widget(Label(text='Panel label'))
    first_button = Button(text='Popup\nbutton')
    side_panel.add_widget(first_button)
    side_panel.add_widget(Button(text='Another\nbutton'))
    navigationdrawer.add_widget(side_panel)


    main_panel = BoxLayout(orientation='vertical')
    label_bl = BoxLayout(orientation='horizontal')

    label_bl.add_widget(Widget(size_hint_x=None, width=dp(10)))
    label_bl.add_widget(Widget(size_hint_x=None, width=dp(10)))
    main_panel.add_widget(Widget(size_hint_y=None, height=dp(10)))
    main_panel.add_widget(label_bl)
    main_panel.add_widget(Widget(size_hint_y=None, height=dp(10)))
    navigationdrawer.add_widget(main_panel)

    navigationdrawer.anim_type = 'slide_above_anim'

    button = Button(text='toggle NavigationDrawer state (animate)')
    button.bind(on_press=lambda j: navigationdrawer.toggle_state())

    main_panel.add_widget(button)


    Window.add_widget(navigationdrawer)

    runTouchApp()
