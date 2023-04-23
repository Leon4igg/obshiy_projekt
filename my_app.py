from PyQt5.QtWidgets import*
app = QApplication([])
okno = QWidget()

line1 = QVBoxLayout()
okno.setLayout(line1)

text1 = QLabel('ура')
line1.addWidget(text1)
text1.setStyleSheet('QLabel{font-size:50px; color:red;}')

but1 = QPushButton('Я что-то написал тут, наверное')
line1.addWidget(but1)
but1.setStyleSheet('''QPushButton{font-size:50px;
background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 red, stop:1 blue);  color:brown;
}''')

okno.setStyleSheet('''QWidget{background-image: url('portrait.jpg');
}''')

okno.show()
app.exec_()
