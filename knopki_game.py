from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
import random
x1y1 = random.randint(0,8)/10
y1x1 = random.randint(0,8)/10                       
x1y2 = random.randint(0,8)/10
y1x2 = random.randint(0,8)/10                    
x1y3 = random.randint(0,8)/10
y1x3 = random.randint(0,8)/10                      
x1y4 = random.randint(0,8)/10
y1x4 = random.randint(0,8)/10                     
x1y5 = random.randint(0,8)/10
y1x5 = random.randint(0,8)/10                    
x1y6 = random.randint(0,8)/10
y1x6 = random.randint(0,8)/10                   
x1y7 = random.randint(0,8)/10
y1x7 = random.randint(0,8)/10                  
x1y8 = random.randint(0,8)/10
y1x8 = random.randint(0,8)/10                 
x1y9 = random.randint(0,8)/10
y1x9 = random.randint(0,8)/10                
x1y10 = random.randint(0,8)/10
y1x10 = random.randint(0,8)/10
x2y1 = random.randint(0,8)/10
y2x1 = random.randint(0,8)/10                       
x2y2 = random.randint(0,8)/10
y2x2 = random.randint(0,8)/10                        
x2y3 = random.randint(0,8)/10
y2x3 = random.randint(0,8)/10                        
x2y4 = random.randint(0,8)/10
y2x4 = random.randint(0,8)/10                       
x2y5 = random.randint(0,8)/10
y2x5 = random.randint(0,8)/10                       
x2y6 = random.randint(0,8)/10
y2x6 = random.randint(0,8)/10                       
x2y7 = random.randint(0,8)/10
y2x7 = random.randint(0,8)/10                       
x2y8 = random.randint(0,8)/10
y2x8 = random.randint(0,8)/10                       
x2y9 = random.randint(0,8)/10
y2x9 = random.randint(0,8)/10                      
x2y10 = random.randint(0,8)/10
y2x10 = random.randint(0,8)/10    
x3y1 = random.randint(0,8)/10
y3x1 = random.randint(0,8)/10                       
x3y2 = random.randint(0,8)/10
y3x2 = random.randint(0,8)/10                        
x3y3 = random.randint(0,8)/10
y3x3 = random.randint(0,8)/10                        
x3y4 = random.randint(0,8)/10
y3x4 = random.randint(0,8)/10                       
x3y5 = random.randint(0,8)/10
y3x5 = random.randint(0,8)/10                      
x3y6 = random.randint(0,8)/10
y3x6 = random.randint(0,8)/10                       
x3y7 = random.randint(0,8)/10
y3x7 = random.randint(0,8)/10                       
x3y8 = random.randint(0,8)/10
y3x8 = random.randint(0,8)/10                       
x3y9 = random.randint(0,8)/10
y3x9 = random.randint(0,8)/10                      
x3y10 = random.randint(0,8)/10
y3x10 = random.randint(0,8)/10        
x4y1 = random.randint(0,8)/10
y4x1 = random.randint(0,8)/10                       
x4y2 = random.randint(0,8)/10
y4x2 = random.randint(0,8)/10                        
x4y3 = random.randint(0,8)/10
y4x3 = random.randint(0,8)/10                        
x4y4 = random.randint(0,8)/10
y4x4 = random.randint(0,8)/10                       
x4y5 = random.randint(0,8)/10
y4x5 = random.randint(0,8)/10                       
x4y6 = random.randint(0,8)/10
y4x6 = random.randint(0,8)/10                       
x4y7 = random.randint(0,8)/10
y4x7 = random.randint(0,8)/10                       
x4y8 = random.randint(0,8)/10
y4x8 = random.randint(0,8)/10                       
x4y9 = random.randint(0,8)/10
y4x9 = random.randint(0,8)/10                      
x4y10 = random.randint(0,8)/10
y4x10 = random.randint(0,8)/10
x5y1 = random.randint(0,8)/10
y5x1 = random.randint(0,8)/10                       
x5y2 = random.randint(0,8)/10
y5x2 = random.randint(0,8)/10                       
x5y3 = random.randint(0,8)/10
y5x3 = random.randint(0,8)/10                        
x5y4 = random.randint(0,8)/10
y5x4 = random.randint(0,8)/10                       
x5y5 = random.randint(0,8)/10
y5x5 = random.randint(0,8)/10                       
x5y6 = random.randint(0,8)/10
y5x6 = random.randint(0,8)/10                       
x5y7 = random.randint(0,8)/10
y5x7 = random.randint(0,8)/10                       
x5y8 = random.randint(0,8)/10
y5x8 = random.randint(0,8)/10                       
x5y9 = random.randint(0,8)/10
y5x9 = random.randint(0,8)/10                      
x5y10 = random.randint(0,8)/10
y5x10 = random.randint(0,8)/10
x6y1 = random.randint(0,8)/10
y6x1 = random.randint(0,8)/10                       
x6y2 = random.randint(0,8)/10
y6x2 = random.randint(0,8)/10                       
x6y3 = random.randint(0,8)/10
y6x3 = random.randint(0,8)/10                        
x6y4 = random.randint(0,8)/10
y6x4 = random.randint(0,8)/10                       
x6y5 = random.randint(0,8)/10
y6x5 = random.randint(0,8)/10                       
x6y6 = random.randint(0,8)/10
y6x6 = random.randint(0,8)/10                       
x6y7 = random.randint(0,8)/10
y6x7 = random.randint(0,8)/10                       
x6y8 = random.randint(0,8)/10
y6x8 = random.randint(0,8)/10                       
x6y9 = random.randint(0,8)/10
y6x9 = random.randint(0,8)/10                      
x6y10 = random.randint(0,8)/10
y6x10 = random.randint(0,8)/10
class ekran1(Screen):
    def __init__(self, name = 'ekran1'):
        super().__init__(name=name)
        self.b1 = Button(text='Старт',size_hint=(.4,.4), pos_hint={'x':.3, 'y':.3}, background_color=(1,2,2,1))
        self.add_widget(self.b1)
        self.b1.on_press = self.navtoru
    def navtoru(self):
        self.manager.current='ekran2' 
class ekran2(Screen):
    def __init__(self, name = 'ekran2'):
        super().__init__(name=name)
        self.b3 = Button(text='',size_hint=(.1,.1), pos_hint={'x':.4, 'y':.8}, background_color=(1,1,1,1))
        self.b4 = Button(text='',size_hint=(.1,.1), pos_hint={'x':.4, 'y':.8}, background_color=(1,1,1,1))
        self.b2 = Button(text='',size_hint=(.1,.1), pos_hint={'x':.3, 'y':.3}, background_color=(1,2,2,1))
        self.b5 = Button(text='',size_hint=(.1,.1), pos_hint={'x':.4, 'y':.8}, background_color=(1,1,1,1))
        self.b6 = Button(text='',size_hint=(.1,.1), pos_hint={'x':.3, 'y':.3}, background_color=(1,1,1,1))
        self.b7 = Button(text='',size_hint=(.1,.1), pos_hint={'x':.4, 'y':.8}, background_color=(1,1,1,1))
        self.add_widget(self.b4)
        self.add_widget(self.b3)
        self.add_widget(self.b2)
        self.add_widget(self.b5)
        self.add_widget(self.b6)
        self.add_widget(self.b7)
        self.play()
        self.anime3()
        self.anime2()
        self.anime1()
        self.anime4()
        self.anime6()
        self.anime5()
    def play(self):
        self.b2.background_color=(1,2,2,1)
        self.b3.background_color=(1,1,1,1)
        self.b4.background_color=(1,1,1,1)
        self.b5.background_color=(1,1,1,1)
        self.b6.background_color=(1,1,1,1)
        self.b7.background_color=(1,1,1,1)
        self.b5.on_press = self.lous
        self.b7.on_press = self.lous
        self.b6.on_press = self.lous
        self.b3.on_press = self.lous
        self.b4.on_press = self.lous
        self.b2.on_press = self.click

    def click(self):
        self.b2.text=''
        
        self.b2.font_size=25
        self.b2.background_color=(1,1,1,1)
        self.b3.background_color=(1,2,2,1)
        self.b4.background_color=(1,1,1,1)
        self.b5.background_color=(1,1,1,1)
        self.b6.background_color=(1,1,1,1)
        self.b7.background_color=(1,1,1,1)
        self.b3.on_press = self.click1
        self.b4.on_press = self.lous
        self.b2.on_press = self.lous
        self.b6.on_press = self.lous
        self.b7.on_press = self.lous
        self.b5.on_press = self.lous
        
        
    
    def click1(self):
        self.b3.text=''
        self.b2.background_color=(1,1,1,1)
        self.b3.background_color=(1,1,1,1)
        self.b4.background_color=(1,2,2,1)
        self.b5.background_color=(1,1,1,1)
        self.b6.background_color=(1,1,1,1)
        self.b7.background_color=(1,1,1,1)
        
        self.b3.font_size=25
        self.b2.on_press = self.lous
        self.b3.on_press = self.lous 
        self.b4.on_press = self.click2
        self.b5.on_press = self.lous
        self.b6.on_press = self.lous 
        self.b7.on_press = self.lous
    def click2(self):
        self.b3.text=''
        self.b2.background_color=(1,1,1,1)
        self.b3.background_color=(1,1,1,1)
        self.b4.background_color=(1,1,1,1)
        self.b5.background_color=(1,2,2,1)
        self.b6.background_color=(1,1,1,1)
        self.b7.background_color=(1,1,1,1)
        self.b3.font_size=25
        self.b5.on_press = self.click3
        self.b4.on_press = self.lous
        self.b6.on_press = self.lous
        self.b7.on_press = self.lous
        self.b2.on_press = self.lous
        self.b3.on_press = self.lous
    def click3(self):
        self.b3.text=''
        self.b2.background_color=(1,1,1,1)
        self.b3.background_color=(1,1,1,1)
        self.b4.background_color=(1,1,1,1)
        self.b5.background_color=(1,1,1,1)
        self.b6.background_color=(1,2,2,1)
        self.b7.background_color=(1,1,1,1)
        self.b3.font_size=25
        self.b5.on_press = self.lous
        self.b4.on_press = self.lous
        self.b6.on_press = self.click4
        self.b7.on_press = self.lous
        self.b2.on_press = self.lous
        self.b3.on_press = self.lous
    def click4(self):
        self.b2.background_color=(1,1,1,1)
        self.b3.background_color=(1,1,1,1)
        self.b4.background_color=(1,1,1,1)
        self.b5.background_color=(1,1,1,1)
        self.b6.background_color=(1,1,1,1)
        self.b7.background_color=(1,2,2,1)
        self.b5.on_press = self.lous
        self.b4.on_press = self.lous
        self.b6.on_press = self.lous
        self.b7.on_press = self.play
        self.b2.on_press = self.lous
        self.b3.on_press = self.lous

    def anime1(self):
        an1 = Animation(duration = .8,size_hint=(.1,.1),pos_hint={'x':x1y1,'y':y1x1}, )#скорость - duration 
        an1 += Animation(duration = .8,pos_hint={'x':x1y2,'y':y1x2}, )#перемещение и цвет
        an1 += Animation(duration = .8,pos_hint={'x':x1y3,'y':y1x3}, )
        an1 += Animation(duration = .8,pos_hint={'x':x1y3,'y':y1x3}, )
        an1 += Animation(duration = .8,pos_hint={'x':x1y4,'y':y1x4}, )
        an1 += Animation(duration = .8,pos_hint={'x':x1y5,'y':y1x5}, )
        an1 += Animation(duration = .8,pos_hint={'x':x1y6,'y':y1x6}, )
        an1 += Animation(duration = .8,pos_hint={'x':x1y7,'y':y1x7}, )
        an1 += Animation(duration = .8,pos_hint={'x':x1y8,'y':y1x8}, )
        an1 += Animation(duration = .8,pos_hint={'x':x1y9,'y':y1x9}, )
        an1 += Animation(duration = .8,pos_hint={'x':x1y10,'y':y1x10}, )
        an1 += Animation(duration = .8,pos_hint={'x':x2y1,'y':y2x1}, )#скорость - duration 
        an1 += Animation(duration = .8,pos_hint={'x':x2y2,'y':y2x2}, )#перемещение и цвет
        an1 += Animation(duration = .8,pos_hint={'x':x2y3,'y':y2x3}, )
        an1 += Animation(duration = .8,pos_hint={'x':x2y3,'y':y2x3}, )
        an1 += Animation(duration = .8,pos_hint={'x':x2y4,'y':y2x4}, )
        an1 += Animation(duration = .8,pos_hint={'x':x2y5,'y':y2x5}, )
        an1 += Animation(duration = .8,pos_hint={'x':x2y6,'y':y2x6}, )
        an1 += Animation(duration = .8,pos_hint={'x':x2y7,'y':y2x7}, )
        an1 += Animation(duration = .8,pos_hint={'x':x2y8,'y':y2x8}, )
        an1 += Animation(duration = .8,pos_hint={'x':x2y9,'y':y2x9}, )
        an1 += Animation(duration = .8,pos_hint={'x':x2y10,'y':y2x10}, )
        an1 += Animation(duration = .8,pos_hint={'x':x3y1,'y':y3x1}, )#скорость - duration 
        an1 += Animation(duration = .8,pos_hint={'x':x3y2,'y':y3x2}, )#перемещение и цвет
        an1 += Animation(duration = .8,pos_hint={'x':x3y3,'y':y3x3}, )
        an1 += Animation(duration = .8,pos_hint={'x':x3y3,'y':y3x3}, )
        an1 += Animation(duration = .8,pos_hint={'x':x3y4,'y':y3x4}, )
        an1 += Animation(duration = .8,pos_hint={'x':x3y5,'y':y3x5}, )
        an1 += Animation(duration = .8,pos_hint={'x':x3y6,'y':y3x6}, )
        an1 += Animation(duration = .8,pos_hint={'x':x3y7,'y':y3x7}, )
        an1 += Animation(duration = .8,pos_hint={'x':x3y8,'y':y3x8}, )
        an1 += Animation(duration = .8,pos_hint={'x':x3y9,'y':y3x9}, )
        an1 += Animation(duration = .8,pos_hint={'x':x3y10,'y':y3x10}, )
        an1 += Animation(duration = .8,pos_hint={'x':x4y1,'y':y4x1}, )#скорость - duration 
        an1 += Animation(duration = .8,pos_hint={'x':x4y2,'y':y4x2}, )#перемещение и цвет
        an1 += Animation(duration = .8,pos_hint={'x':x4y3,'y':y4x3}, )
        an1 += Animation(duration = .8,pos_hint={'x':x4y3,'y':y4x3}, )
        an1 += Animation(duration = .8,pos_hint={'x':x4y4,'y':y4x4}, )
        an1 += Animation(duration = .8,pos_hint={'x':x4y5,'y':y4x5}, )
        an1 += Animation(duration = .8,pos_hint={'x':x4y6,'y':y4x6}, )
        an1 += Animation(duration = .8,pos_hint={'x':x4y7,'y':y4x7}, )
        an1 += Animation(duration = .8,pos_hint={'x':x4y8,'y':y4x8}, )
        an1 += Animation(duration = .8,pos_hint={'x':x4y9,'y':y4x9}, )
        an1 += Animation(duration = .8,pos_hint={'x':x4y10,'y':y4x10}, )
        an1 += Animation(duration = .8,pos_hint={'x':x5y1,'y':y5x1}, )#скорость - duration 
        an1 += Animation(duration = .8,pos_hint={'x':x5y2,'y':y5x2}, )#перемещение и цвет
        an1 += Animation(duration = .8,pos_hint={'x':x5y3,'y':y5x3}, )
        an1 += Animation(duration = .8,pos_hint={'x':x5y3,'y':y5x3}, )
        an1 += Animation(duration = .8,pos_hint={'x':x5y4,'y':y5x4}, )
        an1 += Animation(duration = .8,pos_hint={'x':x5y5,'y':y5x5}, )
        an1 += Animation(duration = .8,pos_hint={'x':x5y6,'y':y5x6}, )
        an1 += Animation(duration = .8,pos_hint={'x':x5y7,'y':y5x7}, )
        an1 += Animation(duration = .8,pos_hint={'x':x5y8,'y':y5x8}, )
        an1 += Animation(duration = .8,pos_hint={'x':x5y9,'y':y5x9}, )
        an1 += Animation(duration = .8,pos_hint={'x':x5y10,'y':y5x10}, )
        an1 += Animation(duration = .8,pos_hint={'x':x6y1,'y':y6x1}, )#скорость - duration 
        an1 += Animation(duration = .8,pos_hint={'x':x6y2,'y':y6x2}, )#перемещение и цвет
        an1 += Animation(duration = .8,pos_hint={'x':x6y3,'y':y6x3}, )
        an1 += Animation(duration = .8,pos_hint={'x':x6y3,'y':y6x3}, )
        an1 += Animation(duration = .8,pos_hint={'x':x6y4,'y':y6x4}, )
        an1 += Animation(duration = .8,pos_hint={'x':x6y5,'y':y6x5}, )
        an1 += Animation(duration = .8,pos_hint={'x':x6y6,'y':y6x6}, )
        an1 += Animation(duration = .8,pos_hint={'x':x6y7,'y':y6x7}, )
        an1 += Animation(duration = .8,pos_hint={'x':x6y8,'y':y6x8}, )
        an1 += Animation(duration = .8,pos_hint={'x':x6y9,'y':y6x9}, )
        an1 += Animation(duration = .8,pos_hint={'x':x6y10,'y':y6x10}, )
        
        an1.repeat = True
        an1.start(self.b2)
    def anime2(self):
        an2 = Animation(duration = .8,size_hint=(.1,.1),pos_hint={'x':x2y1,'y':y2x1}, )#скорость - duration 
        an2 += Animation(duration = .8,pos_hint={'x':x2y2,'y':y2x2}, )#перемещение и цвет
        an2 += Animation(duration = .8,pos_hint={'x':x2y3,'y':y2x3}, )
        an2 += Animation(duration = .8,pos_hint={'x':x2y3,'y':y2x3}, )
        an2 += Animation(duration = .8,pos_hint={'x':x2y4,'y':y2x4}, )
        an2 += Animation(duration = .8,pos_hint={'x':x2y5,'y':y2x5}, )
        an2 += Animation(duration = .8,pos_hint={'x':x2y6,'y':y2x6}, )
        an2 += Animation(duration = .8,pos_hint={'x':x2y7,'y':y2x7}, )
        an2 += Animation(duration = .8,pos_hint={'x':x2y8,'y':y2x8}, )
        an2 += Animation(duration = .8,pos_hint={'x':x2y9,'y':y2x9}, )
        an2 += Animation(duration = .8,pos_hint={'x':x2y10,'y':y2x10}, )
        an2 += Animation(duration = .8,pos_hint={'x':x3y1,'y':y3x1}, )#скорость - duration 
        an2 += Animation(duration = .8,pos_hint={'x':x3y2,'y':y3x2}, )#перемещение и цвет
        an2 += Animation(duration = .8,pos_hint={'x':x3y3,'y':y3x3}, )
        an2 += Animation(duration = .8,pos_hint={'x':x3y3,'y':y3x3}, )
        an2 += Animation(duration = .8,pos_hint={'x':x3y4,'y':y3x4}, )
        an2 += Animation(duration = .8,pos_hint={'x':x3y5,'y':y3x5}, )
        an2 += Animation(duration = .8,pos_hint={'x':x3y6,'y':y3x6}, )
        an2 += Animation(duration = .8,pos_hint={'x':x3y7,'y':y3x7}, )
        an2 += Animation(duration = .8,pos_hint={'x':x3y8,'y':y3x8}, )
        an2 += Animation(duration = .8,pos_hint={'x':x3y9,'y':y3x9}, )
        an2 += Animation(duration = .8,pos_hint={'x':x3y10,'y':y3x10}, )
        an2 += Animation(duration = .8,pos_hint={'x':x4y1,'y':y4x1}, )#скорость - duration 
        an2 += Animation(duration = .8,pos_hint={'x':x4y2,'y':y4x2}, )#перемещение и цвет
        an2 += Animation(duration = .8,pos_hint={'x':x4y3,'y':y4x3}, )
        an2 += Animation(duration = .8,pos_hint={'x':x4y3,'y':y4x3}, )
        an2 += Animation(duration = .8,pos_hint={'x':x4y4,'y':y4x4}, )
        an2 += Animation(duration = .8,pos_hint={'x':x4y5,'y':y4x5}, )
        an2 += Animation(duration = .8,pos_hint={'x':x4y6,'y':y4x6}, )
        an2 += Animation(duration = .8,pos_hint={'x':x4y7,'y':y4x7}, )
        an2 += Animation(duration = .8,pos_hint={'x':x4y8,'y':y4x8}, )
        an2 += Animation(duration = .8,pos_hint={'x':x4y9,'y':y4x9}, )
        an2 += Animation(duration = .8,pos_hint={'x':x4y10,'y':y4x10}, )
        an2 += Animation(duration = .8,pos_hint={'x':x5y1,'y':y5x1}, )#скорость - duration 
        an2 += Animation(duration = .8,pos_hint={'x':x5y2,'y':y5x2}, )#перемещение и цвет
        an2 += Animation(duration = .8,pos_hint={'x':x5y3,'y':y5x3}, )
        an2 += Animation(duration = .8,pos_hint={'x':x5y3,'y':y5x3}, )
        an2 += Animation(duration = .8,pos_hint={'x':x5y4,'y':y5x4}, )
        an2 += Animation(duration = .8,pos_hint={'x':x5y5,'y':y5x5}, )
        an2 += Animation(duration = .8,pos_hint={'x':x5y6,'y':y5x6}, )
        an2 += Animation(duration = .8,pos_hint={'x':x5y7,'y':y5x7}, )
        an2 += Animation(duration = .8,pos_hint={'x':x5y8,'y':y5x8}, )
        an2 += Animation(duration = .8,pos_hint={'x':x5y9,'y':y5x9}, )
        an2 += Animation(duration = .8,pos_hint={'x':x5y10,'y':y5x10}, )
        an2 += Animation(duration = .8,pos_hint={'x':x6y1,'y':y6x1}, )#скорость - duration 
        an2 += Animation(duration = .8,pos_hint={'x':x6y2,'y':y6x2}, )#перемещение и цвет
        an2 += Animation(duration = .8,pos_hint={'x':x6y3,'y':y6x3}, )
        an2 += Animation(duration = .8,pos_hint={'x':x6y3,'y':y6x3}, )
        an2 += Animation(duration = .8,pos_hint={'x':x6y4,'y':y6x4}, )
        an2 += Animation(duration = .8,pos_hint={'x':x6y5,'y':y6x5}, )
        an2 += Animation(duration = .8,pos_hint={'x':x6y6,'y':y6x6}, )
        an2 += Animation(duration = .8,pos_hint={'x':x6y7,'y':y6x7}, )
        an2 += Animation(duration = .8,pos_hint={'x':x6y8,'y':y6x8}, )
        an2 += Animation(duration = .8,pos_hint={'x':x6y9,'y':y6x9}, )
        an2 += Animation(duration = .8,pos_hint={'x':x6y10,'y':y6x10}, )
        an2 += Animation(duration = .8,pos_hint={'x':x1y1,'y':y1x1}, )#скорость - duration 
        an2 += Animation(duration = .8,pos_hint={'x':x1y2,'y':y1x2}, )#перемещение и цвет
        an2 += Animation(duration = .8,pos_hint={'x':x1y3,'y':y1x3}, )
        an2 += Animation(duration = .8,pos_hint={'x':x1y3,'y':y1x3}, )
        an2 += Animation(duration = .8,pos_hint={'x':x1y4,'y':y1x4}, )
        an2 += Animation(duration = .8,pos_hint={'x':x1y5,'y':y1x5}, )
        an2 += Animation(duration = .8,pos_hint={'x':x1y6,'y':y1x6}, )
        an2 += Animation(duration = .8,pos_hint={'x':x1y7,'y':y1x7}, )
        an2 += Animation(duration = .8,pos_hint={'x':x1y8,'y':y1x8}, )
        an2 += Animation(duration = .8,pos_hint={'x':x1y9,'y':y1x9}, )
        an2 += Animation(duration = .8,pos_hint={'x':x1y10,'y':y1x10}, )
        an2.repeat = True
        an2.start(self.b3)


    def anime3(self):
        an3 = Animation(duration = .8,size_hint=(.1,.1),pos_hint={'x':x3y1,'y':y3x1}, )#скорость - duration 
        an3 += Animation(duration = .8,pos_hint={'x':x3y2,'y':y3x2}, )#перемещение и цвет
        an3 += Animation(duration = .8,pos_hint={'x':x3y3,'y':y3x3}, )
        an3 += Animation(duration = .8,pos_hint={'x':x3y3,'y':y3x3}, )
        an3 += Animation(duration = .8,pos_hint={'x':x3y4,'y':y3x4}, )
        an3 += Animation(duration = .8,pos_hint={'x':x3y5,'y':y3x5}, )
        an3 += Animation(duration = .8,pos_hint={'x':x3y6,'y':y3x6}, )
        an3 += Animation(duration = .8,pos_hint={'x':x3y7,'y':y3x7}, )
        an3 += Animation(duration = .8,pos_hint={'x':x3y8,'y':y3x8}, )
        an3 += Animation(duration = .8,pos_hint={'x':x3y9,'y':y3x9}, )
        an3 += Animation(duration = .8,pos_hint={'x':x3y10,'y':y3x10}, )
        an3 += Animation(duration = .8,pos_hint={'x':x4y1,'y':y4x1}, )#скорость - duration 
        an3 += Animation(duration = .8,pos_hint={'x':x4y2,'y':y4x2}, )#перемещение и цвет
        an3 += Animation(duration = .8,pos_hint={'x':x4y3,'y':y4x3}, )
        an3 += Animation(duration = .8,pos_hint={'x':x4y3,'y':y4x3}, )
        an3 += Animation(duration = .8,pos_hint={'x':x4y4,'y':y4x4}, )
        an3 += Animation(duration = .8,pos_hint={'x':x4y5,'y':y4x5}, )
        an3 += Animation(duration = .8,pos_hint={'x':x4y6,'y':y4x6}, )
        an3 += Animation(duration = .8,pos_hint={'x':x4y7,'y':y4x7}, )
        an3 += Animation(duration = .8,pos_hint={'x':x4y8,'y':y4x8}, )
        an3 += Animation(duration = .8,pos_hint={'x':x4y9,'y':y4x9}, )
        an3 += Animation(duration = .8,pos_hint={'x':x4y10,'y':y4x10}, )
        an3 += Animation(duration = .8,pos_hint={'x':x5y1,'y':y5x1}, )#скорость - duration 
        an3 += Animation(duration = .8,pos_hint={'x':x5y2,'y':y5x2}, )#перемещение и цвет
        an3 += Animation(duration = .8,pos_hint={'x':x5y3,'y':y5x3}, )
        an3 += Animation(duration = .8,pos_hint={'x':x5y3,'y':y5x3}, )
        an3 += Animation(duration = .8,pos_hint={'x':x5y4,'y':y5x4}, )
        an3 += Animation(duration = .8,pos_hint={'x':x5y5,'y':y5x5}, )
        an3 += Animation(duration = .8,pos_hint={'x':x5y6,'y':y5x6}, )
        an3 += Animation(duration = .8,pos_hint={'x':x5y7,'y':y5x7}, )
        an3 += Animation(duration = .8,pos_hint={'x':x5y8,'y':y5x8}, )
        an3 += Animation(duration = .8,pos_hint={'x':x5y9,'y':y5x9}, )
        an3 += Animation(duration = .8,pos_hint={'x':x5y10,'y':y5x10}, )
        an3 += Animation(duration = .8,pos_hint={'x':x6y1,'y':y6x1}, )#скорость - duration 
        an3 += Animation(duration = .8,pos_hint={'x':x6y2,'y':y6x2}, )#перемещение и цвет
        an3 += Animation(duration = .8,pos_hint={'x':x6y3,'y':y6x3}, )
        an3 += Animation(duration = .8,pos_hint={'x':x6y3,'y':y6x3}, )
        an3 += Animation(duration = .8,pos_hint={'x':x6y4,'y':y6x4}, )
        an3 += Animation(duration = .8,pos_hint={'x':x6y5,'y':y6x5}, )
        an3 += Animation(duration = .8,pos_hint={'x':x6y6,'y':y6x6}, )
        an3 += Animation(duration = .8,pos_hint={'x':x6y7,'y':y6x7}, )
        an3 += Animation(duration = .8,pos_hint={'x':x6y8,'y':y6x8}, )
        an3 += Animation(duration = .8,pos_hint={'x':x6y9,'y':y6x9}, )
        an3 += Animation(duration = .8,pos_hint={'x':x6y10,'y':y6x10}, )
        an3 += Animation(duration = .8,pos_hint={'x':x1y1,'y':y1x1}, )#скорость - duration 
        an3 += Animation(duration = .8,pos_hint={'x':x1y2,'y':y1x2}, )#перемещение и цвет
        an3 += Animation(duration = .8,pos_hint={'x':x1y3,'y':y1x3}, )
        an3 += Animation(duration = .8,pos_hint={'x':x1y3,'y':y1x3}, )
        an3 += Animation(duration = .8,pos_hint={'x':x1y4,'y':y1x4}, )
        an3 += Animation(duration = .8,pos_hint={'x':x1y5,'y':y1x5}, )
        an3 += Animation(duration = .8,pos_hint={'x':x1y6,'y':y1x6}, )
        an3 += Animation(duration = .8,pos_hint={'x':x1y7,'y':y1x7}, )
        an3 += Animation(duration = .8,pos_hint={'x':x1y8,'y':y1x8}, )
        an3 += Animation(duration = .8,pos_hint={'x':x1y9,'y':y1x9}, )
        an3 += Animation(duration = .8,pos_hint={'x':x1y10,'y':y1x10}, )
        an3 += Animation(duration = .8,pos_hint={'x':x2y1,'y':y2x1}, )#скорость - duration 
        an3 += Animation(duration = .8,pos_hint={'x':x2y2,'y':y2x2}, )#перемещение и цвет
        an3 += Animation(duration = .8,pos_hint={'x':x2y3,'y':y2x3}, )
        an3 += Animation(duration = .8,pos_hint={'x':x2y3,'y':y2x3}, )
        an3 += Animation(duration = .8,pos_hint={'x':x2y4,'y':y2x4}, )
        an3 += Animation(duration = .8,pos_hint={'x':x2y5,'y':y2x5}, )
        an3 += Animation(duration = .8,pos_hint={'x':x2y6,'y':y2x6}, )
        an3 += Animation(duration = .8,pos_hint={'x':x2y7,'y':y2x7}, )
        an3 += Animation(duration = .8,pos_hint={'x':x2y8,'y':y2x8}, )
        an3 += Animation(duration = .8,pos_hint={'x':x2y9,'y':y2x9}, )
        an3 += Animation(duration = .8,pos_hint={'x':x2y10,'y':y2x10}, )
        
        
        
        an3.repeat = True
        an3.start(self.b4)
    def anime4(self):
        an4 = Animation(duration = .8,size_hint=(.1,.1),pos_hint={'x':x4y1,'y':y4x1}, )#скорость - duration 
        an4 += Animation(duration = .8,pos_hint={'x':x4y2,'y':y4x2}, )#перемещение и цвет
        an4 += Animation(duration = .8,pos_hint={'x':x4y3,'y':y4x3}, )
        an4 += Animation(duration = .8,pos_hint={'x':x4y3,'y':y4x3}, )
        an4 += Animation(duration = .8,pos_hint={'x':x4y4,'y':y4x4}, )
        an4 += Animation(duration = .8,pos_hint={'x':x4y5,'y':y4x5}, )
        an4 += Animation(duration = .8,pos_hint={'x':x4y6,'y':y4x6}, )
        an4 += Animation(duration = .8,pos_hint={'x':x4y7,'y':y4x7}, )
        an4 += Animation(duration = .8,pos_hint={'x':x4y8,'y':y4x8}, )
        an4 += Animation(duration = .8,pos_hint={'x':x4y9,'y':y4x9}, )
        an4 += Animation(duration = .8,pos_hint={'x':x4y10,'y':y4x10}, )
        an4 += Animation(duration = .8,pos_hint={'x':x5y1,'y':y5x1}, )#скорость - duration 
        an4 += Animation(duration = .8,pos_hint={'x':x5y2,'y':y5x2}, )#перемещение и цвет
        an4 += Animation(duration = .8,pos_hint={'x':x5y3,'y':y5x3}, )
        an4 += Animation(duration = .8,pos_hint={'x':x5y3,'y':y5x3}, )
        an4 += Animation(duration = .8,pos_hint={'x':x5y4,'y':y5x4}, )
        an4 += Animation(duration = .8,pos_hint={'x':x5y5,'y':y5x5}, )
        an4 += Animation(duration = .8,pos_hint={'x':x5y6,'y':y5x6}, )
        an4 += Animation(duration = .8,pos_hint={'x':x5y7,'y':y5x7}, )
        an4 += Animation(duration = .8,pos_hint={'x':x5y8,'y':y5x8}, )
        an4 += Animation(duration = .8,pos_hint={'x':x5y9,'y':y5x9}, )
        an4 += Animation(duration = .8,pos_hint={'x':x5y10,'y':y5x10}, )
        an4 += Animation(duration = .8,pos_hint={'x':x6y1,'y':y6x1}, )#скорость - duration 
        an4 += Animation(duration = .8,pos_hint={'x':x6y2,'y':y6x2}, )#перемещение и цвет
        an4 += Animation(duration = .8,pos_hint={'x':x6y3,'y':y6x3}, )
        an4 += Animation(duration = .8,pos_hint={'x':x6y3,'y':y6x3}, )
        an4 += Animation(duration = .8,pos_hint={'x':x6y4,'y':y6x4}, )
        an4 += Animation(duration = .8,pos_hint={'x':x6y5,'y':y6x5}, )
        an4 += Animation(duration = .8,pos_hint={'x':x6y6,'y':y6x6}, )
        an4 += Animation(duration = .8,pos_hint={'x':x6y7,'y':y6x7}, )
        an4 += Animation(duration = .8,pos_hint={'x':x6y8,'y':y6x8}, )
        an4 += Animation(duration = .8,pos_hint={'x':x6y9,'y':y6x9}, )
        an4 += Animation(duration = .8,pos_hint={'x':x6y10,'y':y6x10}, )
        an4 += Animation(duration = .8,pos_hint={'x':x1y1,'y':y1x1}, )#скорость - duration 
        an4 += Animation(duration = .8,pos_hint={'x':x1y2,'y':y1x2}, )#перемещение и цвет
        an4 += Animation(duration = .8,pos_hint={'x':x1y3,'y':y1x3}, )
        an4 += Animation(duration = .8,pos_hint={'x':x1y3,'y':y1x3}, )
        an4 += Animation(duration = .8,pos_hint={'x':x1y4,'y':y1x4}, )
        an4 += Animation(duration = .8,pos_hint={'x':x1y5,'y':y1x5}, )
        an4 += Animation(duration = .8,pos_hint={'x':x1y6,'y':y1x6}, )
        an4 += Animation(duration = .8,pos_hint={'x':x1y7,'y':y1x7}, )
        an4 += Animation(duration = .8,pos_hint={'x':x1y8,'y':y1x8}, )
        an4 += Animation(duration = .8,pos_hint={'x':x1y9,'y':y1x9}, )
        an4 += Animation(duration = .8,pos_hint={'x':x1y10,'y':y1x10}, )
        an4 += Animation(duration = .8,pos_hint={'x':x2y1,'y':y2x1}, )#скорость - duration 
        an4 += Animation(duration = .8,pos_hint={'x':x2y2,'y':y2x2}, )#перемещение и цвет
        an4 += Animation(duration = .8,pos_hint={'x':x2y3,'y':y2x3}, )
        an4 += Animation(duration = .8,pos_hint={'x':x2y3,'y':y2x3}, )
        an4 += Animation(duration = .8,pos_hint={'x':x2y4,'y':y2x4}, )
        an4 += Animation(duration = .8,pos_hint={'x':x2y5,'y':y2x5}, )
        an4 += Animation(duration = .8,pos_hint={'x':x2y6,'y':y2x6}, )
        an4 += Animation(duration = .8,pos_hint={'x':x2y7,'y':y2x7}, )
        an4 += Animation(duration = .8,pos_hint={'x':x2y8,'y':y2x8}, )
        an4 += Animation(duration = .8,pos_hint={'x':x2y9,'y':y2x9}, )
        an4 += Animation(duration = .8,pos_hint={'x':x2y10,'y':y2x10}, )
        an4 += Animation(duration = .8,pos_hint={'x':x3y1,'y':y3x1}, )#скорость - duration 
        an4 += Animation(duration = .8,pos_hint={'x':x3y2,'y':y3x2}, )#перемещение и цвет
        an4 += Animation(duration = .8,pos_hint={'x':x3y3,'y':y3x3}, )
        an4 += Animation(duration = .8,pos_hint={'x':x3y3,'y':y3x3}, )
        an4 += Animation(duration = .8,pos_hint={'x':x3y4,'y':y3x4}, )
        an4 += Animation(duration = .8,pos_hint={'x':x3y5,'y':y3x5}, )
        an4 += Animation(duration = .8,pos_hint={'x':x3y6,'y':y3x6}, )
        an4 += Animation(duration = .8,pos_hint={'x':x3y7,'y':y3x7}, )
        an4 += Animation(duration = .8,pos_hint={'x':x3y8,'y':y3x8}, )
        an4 += Animation(duration = .8,pos_hint={'x':x3y9,'y':y3x9}, )
        an4 += Animation(duration = .8,pos_hint={'x':x3y10,'y':y3x10}, )
        an4.repeat = True
        an4.start(self.b5)    
    def anime5(self):
        an5 = Animation(duration = .8,size_hint=(.1,.1),pos_hint={'x':x5y1,'y':y5x1}, )#скорость - duration 
        an5 += Animation(duration = .8,pos_hint={'x':x5y2,'y':y5x2}, )#перемещение и цвет
        an5 += Animation(duration = .8,pos_hint={'x':x5y3,'y':y5x3}, )
        an5 += Animation(duration = .8,pos_hint={'x':x5y3,'y':y5x3}, )
        an5 += Animation(duration = .8,pos_hint={'x':x5y4,'y':y5x4}, )
        an5 += Animation(duration = .8,pos_hint={'x':x5y5,'y':y5x5}, )
        an5 += Animation(duration = .8,pos_hint={'x':x5y6,'y':y5x6}, )
        an5 += Animation(duration = .8,pos_hint={'x':x5y7,'y':y5x7}, )
        an5 += Animation(duration = .8,pos_hint={'x':x5y8,'y':y5x8}, )
        an5 += Animation(duration = .8,pos_hint={'x':x5y9,'y':y5x9}, )
        an5 += Animation(duration = .8,pos_hint={'x':x5y10,'y':y5x10}, )
        an5 += Animation(duration = .8,pos_hint={'x':x6y1,'y':y6x1}, )#скорость - duration 
        an5 += Animation(duration = .8,pos_hint={'x':x6y2,'y':y6x2}, )#перемещение и цвет
        an5 += Animation(duration = .8,pos_hint={'x':x6y3,'y':y6x3}, )
        an5 += Animation(duration = .8,pos_hint={'x':x6y3,'y':y6x3}, )
        an5 += Animation(duration = .8,pos_hint={'x':x6y4,'y':y6x4}, )
        an5 += Animation(duration = .8,pos_hint={'x':x6y5,'y':y6x5}, )
        an5 += Animation(duration = .8,pos_hint={'x':x6y6,'y':y6x6}, )
        an5 += Animation(duration = .8,pos_hint={'x':x6y7,'y':y6x7}, )
        an5 += Animation(duration = .8,pos_hint={'x':x6y8,'y':y6x8}, )
        an5 += Animation(duration = .8,pos_hint={'x':x6y9,'y':y6x9}, )
        an5 += Animation(duration = .8,pos_hint={'x':x6y10,'y':y6x10}, )
        an5 += Animation(duration = .8,pos_hint={'x':x1y1,'y':y1x1}, )#скорость - duration 
        an5 += Animation(duration = .8,pos_hint={'x':x1y2,'y':y1x2}, )#перемещение и цвет
        an5 += Animation(duration = .8,pos_hint={'x':x1y3,'y':y1x3}, )
        an5 += Animation(duration = .8,pos_hint={'x':x1y3,'y':y1x3}, )
        an5 += Animation(duration = .8,pos_hint={'x':x1y4,'y':y1x4}, )
        an5 += Animation(duration = .8,pos_hint={'x':x1y5,'y':y1x5}, )
        an5 += Animation(duration = .8,pos_hint={'x':x1y6,'y':y1x6}, )
        an5 += Animation(duration = .8,pos_hint={'x':x1y7,'y':y1x7}, )
        an5 += Animation(duration = .8,pos_hint={'x':x1y8,'y':y1x8}, )
        an5 += Animation(duration = .8,pos_hint={'x':x1y9,'y':y1x9}, )
        an5 += Animation(duration = .8,pos_hint={'x':x1y10,'y':y1x10}, )
        an5 += Animation(duration = .8,pos_hint={'x':x2y1,'y':y2x1}, )#скорость - duration 
        an5 += Animation(duration = .8,pos_hint={'x':x2y2,'y':y2x2}, )#перемещение и цвет
        an5 += Animation(duration = .8,pos_hint={'x':x2y3,'y':y2x3}, )
        an5 += Animation(duration = .8,pos_hint={'x':x2y3,'y':y2x3}, )
        an5 += Animation(duration = .8,pos_hint={'x':x2y4,'y':y2x4}, )
        an5 += Animation(duration = .8,pos_hint={'x':x2y5,'y':y2x5}, )
        an5 += Animation(duration = .8,pos_hint={'x':x2y6,'y':y2x6}, )
        an5 += Animation(duration = .8,pos_hint={'x':x2y7,'y':y2x7}, )
        an5 += Animation(duration = .8,pos_hint={'x':x2y8,'y':y2x8}, )
        an5 += Animation(duration = .8,pos_hint={'x':x2y9,'y':y2x9}, )
        an5 += Animation(duration = .8,pos_hint={'x':x2y10,'y':y2x10}, )
        an5 += Animation(duration = .8,pos_hint={'x':x3y1,'y':y3x1}, )#скорость - duration 
        an5 += Animation(duration = .8,pos_hint={'x':x3y2,'y':y3x2}, )#перемещение и цвет
        an5 += Animation(duration = .8,pos_hint={'x':x3y3,'y':y3x3}, )
        an5 += Animation(duration = .8,pos_hint={'x':x3y3,'y':y3x3}, )
        an5 += Animation(duration = .8,pos_hint={'x':x3y4,'y':y3x4}, )
        an5 += Animation(duration = .8,pos_hint={'x':x3y5,'y':y3x5}, )
        an5 += Animation(duration = .8,pos_hint={'x':x3y6,'y':y3x6}, )
        an5 += Animation(duration = .8,pos_hint={'x':x3y7,'y':y3x7}, )
        an5 += Animation(duration = .8,pos_hint={'x':x3y8,'y':y3x8}, )
        an5 += Animation(duration = .8,pos_hint={'x':x3y9,'y':y3x9}, )
        an5 += Animation(duration = .8,pos_hint={'x':x3y10,'y':y3x10}, )
        an5 += Animation(duration = .8,pos_hint={'x':x4y1,'y':y4x1}, )#скорость - duration 
        an5 += Animation(duration = .8,pos_hint={'x':x4y2,'y':y4x2}, )#перемещение и цвет
        an5 += Animation(duration = .8,pos_hint={'x':x4y3,'y':y4x3}, )
        an5 += Animation(duration = .8,pos_hint={'x':x4y3,'y':y4x3}, )
        an5 += Animation(duration = .8,pos_hint={'x':x4y4,'y':y4x4}, )
        an5 += Animation(duration = .8,pos_hint={'x':x4y5,'y':y4x5}, )
        an5 += Animation(duration = .8,pos_hint={'x':x4y6,'y':y4x6}, )
        an5 += Animation(duration = .8,pos_hint={'x':x4y7,'y':y4x7}, )
        an5 += Animation(duration = .8,pos_hint={'x':x4y8,'y':y4x8}, )
        an5 += Animation(duration = .8,pos_hint={'x':x4y9,'y':y4x9}, )
        an5 += Animation(duration = .8,pos_hint={'x':x4y10,'y':y4x10}, )
        
        
        an5.repeat= True
        an5.start(self.b6)    
    def anime6(self):
        an6 = Animation(duration = .8,size_hint=(.1,.1),pos_hint={'x':x6y1,'y':y6x1}, )#скорость - duration 
        an6 += Animation(duration = .8,pos_hint={'x':x6y2,'y':y6x2}, )#перемещение и цвет
        an6 += Animation(duration = .8,pos_hint={'x':x6y3,'y':y6x3}, )
        an6 += Animation(duration = .8,pos_hint={'x':x6y3,'y':y6x3}, )
        an6 += Animation(duration = .8,pos_hint={'x':x6y4,'y':y6x4}, )
        an6 += Animation(duration = .8,pos_hint={'x':x6y6,'y':y6x6}, )
        an6 += Animation(duration = .8,pos_hint={'x':x6y6,'y':y6x6}, )
        an6 += Animation(duration = .8,pos_hint={'x':x6y7,'y':y6x7}, )
        an6 += Animation(duration = .8,pos_hint={'x':x6y8,'y':y6x8}, )
        an6 += Animation(duration = .8,pos_hint={'x':x6y9,'y':y6x9}, )
        an6 += Animation(duration = .8,pos_hint={'x':x6y10,'y':y6x10}, )
        an6 += Animation(duration = .8,pos_hint={'x':x1y1,'y':y1x1}, )#скорость - duration 
        an6 += Animation(duration = .8,pos_hint={'x':x1y2,'y':y1x2}, )#перемещение и цвет
        an6 += Animation(duration = .8,pos_hint={'x':x1y3,'y':y1x3}, )
        an6 += Animation(duration = .8,pos_hint={'x':x1y3,'y':y1x3}, )
        an6 += Animation(duration = .8,pos_hint={'x':x1y4,'y':y1x4}, )
        an6 += Animation(duration = .8,pos_hint={'x':x1y5,'y':y1x5}, )
        an6 += Animation(duration = .8,pos_hint={'x':x1y6,'y':y1x6}, )
        an6 += Animation(duration = .8,pos_hint={'x':x1y7,'y':y1x7}, )
        an6 += Animation(duration = .8,pos_hint={'x':x1y8,'y':y1x8}, )
        an6 += Animation(duration = .8,pos_hint={'x':x1y9,'y':y1x9}, )
        an6 += Animation(duration = .8,pos_hint={'x':x1y10,'y':y1x10}, )
        an6 += Animation(duration = .8,pos_hint={'x':x2y1,'y':y2x1}, )#скорость - duration 
        an6 += Animation(duration = .8,pos_hint={'x':x2y2,'y':y2x2}, )#перемещение и цвет
        an6 += Animation(duration = .8,pos_hint={'x':x2y3,'y':y2x3}, )
        an6 += Animation(duration = .8,pos_hint={'x':x2y3,'y':y2x3}, )
        an6 += Animation(duration = .8,pos_hint={'x':x2y4,'y':y2x4}, )
        an6 += Animation(duration = .8,pos_hint={'x':x2y5,'y':y2x5}, )
        an6 += Animation(duration = .8,pos_hint={'x':x2y6,'y':y2x6}, )
        an6 += Animation(duration = .8,pos_hint={'x':x2y7,'y':y2x7}, )
        an6 += Animation(duration = .8,pos_hint={'x':x2y8,'y':y2x8}, )
        an6 += Animation(duration = .8,pos_hint={'x':x2y9,'y':y2x9}, )
        an6 += Animation(duration = .8,pos_hint={'x':x2y10,'y':y2x10}, )
        an6 += Animation(duration = .8,pos_hint={'x':x3y1,'y':y3x1}, )#скорость - duration 
        an6 += Animation(duration = .8,pos_hint={'x':x3y2,'y':y3x2}, )#перемещение и цвет
        an6 += Animation(duration = .8,pos_hint={'x':x3y3,'y':y3x3}, )
        an6 += Animation(duration = .8,pos_hint={'x':x3y3,'y':y3x3}, )
        an6 += Animation(duration = .8,pos_hint={'x':x3y4,'y':y3x4}, )
        an6 += Animation(duration = .8,pos_hint={'x':x3y5,'y':y3x5}, )
        an6 += Animation(duration = .8,pos_hint={'x':x3y6,'y':y3x6}, )
        an6 += Animation(duration = .8,pos_hint={'x':x3y7,'y':y3x7}, )
        an6 += Animation(duration = .8,pos_hint={'x':x3y8,'y':y3x8}, )
        an6 += Animation(duration = .8,pos_hint={'x':x3y9,'y':y3x9}, )
        an6 += Animation(duration = .8,pos_hint={'x':x3y10,'y':y3x10}, )
        an6 += Animation(duration = .8,pos_hint={'x':x4y1,'y':y4x1}, )#скорость - duration 
        an6 += Animation(duration = .8,pos_hint={'x':x4y2,'y':y4x2}, )#перемещение и цвет
        an6 += Animation(duration = .8,pos_hint={'x':x4y3,'y':y4x3}, )
        an6 += Animation(duration = .8,pos_hint={'x':x4y3,'y':y4x3}, )
        an6 += Animation(duration = .8,pos_hint={'x':x4y4,'y':y4x4}, )
        an6 += Animation(duration = .8,pos_hint={'x':x4y5,'y':y4x5}, )
        an6 += Animation(duration = .8,pos_hint={'x':x4y6,'y':y4x6}, )
        an6 += Animation(duration = .8,pos_hint={'x':x4y7,'y':y4x7}, )
        an6 += Animation(duration = .8,pos_hint={'x':x4y8,'y':y4x8}, )
        an6 += Animation(duration = .8,pos_hint={'x':x4y9,'y':y4x9}, )
        an6 += Animation(duration = .8,pos_hint={'x':x4y10,'y':y4x10}, )
        an6 += Animation(duration = .8,pos_hint={'x':x5y1,'y':y5x1}, )#скорость - duration 
        an6 += Animation(duration = .8,pos_hint={'x':x5y2,'y':y5x2}, )#перемещение и цвет
        an6 += Animation(duration = .8,pos_hint={'x':x5y3,'y':y5x3}, )
        an6 += Animation(duration = .8,pos_hint={'x':x5y3,'y':y5x3}, )
        an6 += Animation(duration = .8,pos_hint={'x':x5y4,'y':y5x4}, )
        an6 += Animation(duration = .8,pos_hint={'x':x5y5,'y':y5x5}, )
        an6 += Animation(duration = .8,pos_hint={'x':x5y6,'y':y5x6}, )
        an6 += Animation(duration = .8,pos_hint={'x':x5y7,'y':y5x7}, )
        an6 += Animation(duration = .8,pos_hint={'x':x5y8,'y':y5x8}, )
        an6 += Animation(duration = .8,pos_hint={'x':x5y9,'y':y5x9}, )
        an6 += Animation(duration = .8,pos_hint={'x':x5y10,'y':y5x10}, )
        
        an6.repeat = True
        an6.start(self.b7)    



    def lous(self):
        self.manager.current='lous'
class lous(Screen):
    def __init__(self, name = 'lous'):
        super().__init__(name=name)
        self.b5 = Button(text='Поражение',size_hint=(1,1), pos_hint={'x':.0, 'y':.0}, background_color=(2,2,2,1))        
        self.add_widget(self.b5)
        self.b5.background_color=(1,0,0,1)
        self.b5.font_size=100
        self.b5.on_press = self.navtoru1
    def navtoru1(self):
        self.manager.current='ekran2' 
        
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ekran1(name='ekran1'))
        sm.add_widget(ekran2(name='ekran2'))
        sm.add_widget(lous(name='lous'))
        return sm
        return layout  



MyApp().run() # программа отслеживает нажатие на кнопку и печатает соотв. текст