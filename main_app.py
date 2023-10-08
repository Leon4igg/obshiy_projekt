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
        self.b1 = Button(text='Старт',size_hint=(.4,.4), pos_hint={'x':.3, 'y':.3}, background_color=(0,1,1,1))
        self.add_widget(self.b1)
        self.b1.on_press = self.navtoru

    def navtoru(self):
        self.manager.current='ekran2' 

class ekran2(Screen):
    def __init__(self, name = 'ekran2'):
        super().__init__(name=name)
        self.b2 = Button(text='',size_hint=(.4,.4), pos_hint={'x':.3, 'y':.3}, background_color=(0,1,1,1))
        self.add_widget(self.b2)
        self.anime()
    def anime(self):
            an1 = Animation(duration = 1,size_hint=(.2,.2),pos_hint={'x':.6,'y':.8}, background_color=(10,10,0,1))#скорость - duration
            an1 += Animation(pos_hint={'x':0,'y':0}, background_color=(0,10,0,1)) #перемещение и цвет
            an1 += Animation(pos_hint={'x':.4,'y':.6}, background_color=(10,0,0,1))
            an1 += Animation(pos_hint={'x':0,'y':.5}, background_color=(5,0,0,1))
            an1 += Animation(pos_hint={'x':.9,'y':.1}, background_color=(1,10,0,1))
            an1 += Animation(pos_hint={'x':.8,'y':.5}, background_color=(3,10,0,1))
            an1 += Animation(pos_hint={'x':.2,'y':.3}, background_color=(5,10,0,1))
            an1.repeat = True
            an1.start(self.b2)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ekran1(name='ekran1'))
        sm.add_widget(ekran2(name='ekran2'))
        return sm





MyApp().run() # программа отслеживает нажатие на кнопку и печатает соотв. текст