from PyQt5.QtWidgets import*

app = QApplication([])
okno = QWidget()

okno.setWindowTitle('Калькулятор')
okno.resize(600,600)

#1
a = QLineEdit(okno)
a.move(50,200)
b = QLineEdit(okno)
b.move(250,200)
tex = QLabel(okno)
tex.setText('+')
tex.move(210,202)
tex1 = QPushButton(okno)
tex1.setText('=')
tex1.move(400,202)

#2
c = QLineEdit(okno)
c.move(50,300)
v = QLineEdit(okno)
v.move(250,300)
tex2 = QLabel(okno)
tex2.setText('-')
tex2.move(210,302)
tex3 = QPushButton(okno)
tex3.setText('=')
tex3.move(400,302)

#3
g = QLineEdit(okno)
g.move(50,400)
j = QLineEdit(okno)
j.move(250,400)
tex4 = QLabel(okno)
tex4.setText('*')
tex4.move(210,405)
tex5 = QPushButton(okno)
tex5.setText('=')
tex5.move(400,402)

#4
l = QLineEdit(okno)
l.move(50,500)
o = QLineEdit(okno)
o.move(250,500)
tex7 = QLabel(okno)
tex7.setText('/')
tex7.move(210,505)
tex8 = QPushButton(okno)
tex8.setText('=')
tex8.move(400,502)

def slozh():
    ch1=int(a.text())
    ch2=int(b.text())
    res1=ch1+ch2
    tex1.setText(str(res1))

def vichit():
    ch3=int(c.text())
    ch4=int(v.text())
    res2=ch3-ch4
    tex3.setText(str(res2))

def umn():
    ch5=int(g.text())
    ch6=int(j.text())
    res3=ch5*ch6
    tex5.setText(str(res3))

def delen():
    ch7=int(l.text())
    ch8=int(o.text())
    res4=ch7/ch8
    tex8.setText(str(res4))

tex1.clicked.connect(slozh)
tex3.clicked.connect(vichit)
tex5.clicked.connect(umn)
tex8.clicked.connect(delen)

a.setStyleSheet('''QLineEdit{font-size:10px;
background: yellow;}''')
b.setStyleSheet('''QLineEdit{font-size:10px;
background: yellow;}''')
c.setStyleSheet('''QLineEdit{font-size:10px;
background: yellow;}''')
v.setStyleSheet('''QLineEdit{font-size:10px;
background: yellow;}''')
g.setStyleSheet('''QLineEdit{font-size:10px;
background: yellow;}''')
j.setStyleSheet('''QLineEdit{font-size:10px;
background: yellow;}''')
l.setStyleSheet('''QLineEdit{font-size:10px;
background: yellow;}''')
o.setStyleSheet('''QLineEdit{font-size:10px;
background: yellow;}''')

okno.setStyleSheet('''QWidget{background-image: url('aaaa.jpg');
}''')

#b1 = QPushButton(okno)
#b1.setText('1')
#b1.move(100,250)
okno.show()
app.exec_()
