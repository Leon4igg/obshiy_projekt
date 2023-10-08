
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
class MyApp(App):
    def onyame(self):
        an1 = Animation(duration = 1,pos_hint={'x':.6,'y':.8}, background_color=(10,10,0,1))#скорость - duration
        an1 += Animation(pos_hint={'x':0,'y':0}, background_color=(0,10,0,1)) #перемещение и цвет
        an1 += Animation(pos_hint={'x':.4,'y':.6}, background_color=(10,0,0,1))
        an1 += Animation(pos_hint={'x':0,'y':.5}, background_color=(5,0,0,1))
        an1 += Animation(pos_hint={'x':.9,'y':.1}, background_color=(1,10,0,1))
        an1 += Animation(pos_hint={'x':.8,'y':.5}, background_color=(3,10,0,1))
        an1 += Animation(pos_hint={'x':.2,'y':.3}, background_color=(5,10,0,1))
        an1.repeat = True
        an1.start(self.btn)






    def build(self):
      txt = Label(text='Это надпись',size_hint=(.2,.2),pos_hint={'x':.2,'y':.4}) 
      self.btn = Button(text='Это кнопка',size_hint=(.1,.2),pos_hint={'x':.5,'y':.4})
      layout = FloatLayout()

      layout.add_widget(txt)
      layout.add_widget(self.btn)
      self.btn.on_press = self.onyame
      return layout 

MyApp().run() # программа отслеживает нажатие на кнопку и печатает соотв. текст.
