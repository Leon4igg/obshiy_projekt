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
tex3 = QLabel(okno)
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
tex5 = QLabel(okno)
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
tex8 = QLabel(okno)
tex8.setText('=')
tex8.move(400,502)

def slozh():
    ch1=int(a.text())
    ch2=int(b.text())
    res=ch1+ch2
    tex1.setText(str(res))


tex1.clicked.connect(slozh)

#b1 = QPushButton(okno)
#b1.setText('1')
#b1.move(100,250)
okno.show()
app.exec_()