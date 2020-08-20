from PyQt5 import QtWidgets
from PyQt5 import QtGui

app = QtWidgets.QApplication([])
label = QtWidgets.QLabel()

#QPixmap에 사진을 올립니다.
pixmap = QtGui.QPixmap('../data/lena.jpg')
#label에 입력하고 크기를 재조정합니다.
label.setPixmap(pixmap)
label.resize(pixmap.width(), pixmap.height())
label.show()

app.exec_()
