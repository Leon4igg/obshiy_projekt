from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
class ekran1(Screen):
    def __init__(self, name = 'ekran1'):
        super().__init__(name=name)
        self.b1 = Button(text='старт',size_hint=(.2,.2))
        self.add_widget(self.b1)
        self.b1.on_press = self.navtoru
    def navtoru(self):
        self.manager.current='ekran2' 
        self.manager.children[0].b2.background_color=(10,0,0,1)
class ekran2(Screen):
    def __init__(self, name = 'ekran2'):
        super().__init__(name=name)
        self.b2 = Button(text='второй')
        self.add_widget(self.b2)
        self.b2.on_press = self.naperv
    def naperv(self):
        self.manager.current='ekran1' 
        self.manager.children[0].b1.background_color=(0,0,0,1)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ekran1(name='ekran1'))
        sm.add_widget(ekran2(name='ekran2'))
        return sm





MyApp().run() # программа отслеживает нажатие на кнопку и печатает соотв. текст
