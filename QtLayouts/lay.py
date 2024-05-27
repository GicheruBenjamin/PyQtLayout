import sys
from PyQt6.QtWidgets import (QWidget, 
QApplication,
QVBoxLayout,
QHBoxLayout,
QGridLayout,
QLabel,)

app = QApplication([])

window = QWidget()

wag = QWidget()
l_sty = f"font-size: 20px; font-weight: bold; color: blue; padding: 5px; height: 12px; width: 25px"
l1,l2,l3,l4,l5,l6 = QLabel("1"), QLabel("2"), QLabel("3"), QLabel("4"), QLabel("5"), QLabel("6")
l1.setStyleSheet(l_sty)
l2.setStyleSheet(l_sty)
l3.setStyleSheet(l_sty)
l4.setStyleSheet(l_sty)
l5.setStyleSheet(l_sty)
l6.setStyleSheet(l_sty)
lay1 = QVBoxLayout()
lay1.addWidget(l1)
lay1.addWidget(l2)
lay1.addWidget(l3)
lay1.addWidget(l4)
lay1.addWidget(l5)
lay1.addWidget(l6)
wag.setLayout(lay1)

weg = QWidget()
lk_sty = f"font-size: 20px; font-weight: bold; color: red; padding: 5px; height: 12px; width: 30px;"
la,le,li,lo,lu = QLabel("A"), QLabel("E"), QLabel("I"), QLabel("O"), QLabel("U")
la.setStyleSheet(lk_sty)
le.setStyleSheet(lk_sty)
li.setStyleSheet(lk_sty)
lo.setStyleSheet(lk_sty)
lu.setStyleSheet(lk_sty)
lay2 = QHBoxLayout()
lay2.addWidget(la)
lay2.addWidget(le)
lay2.addWidget(li)
lay2.addWidget(lo)
lay2.addWidget(lu)
weg.setLayout(lay2)

lay3 = QGridLayout()
lay3.addWidget(wag,0,0)
lay3.addWidget(weg,0,1)
window.setLayout(lay3)

window.show()

sys.exit(app.exec())