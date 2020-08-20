import cv2
from PyQt5 import QtWidgets
from PyQt5 import QtGui

app = QtWidgets.QApplication([])
label = QtWidgets.QLabel()

#opencv 함수를 이용하여 사진을 읽어 옵니다.
img = cv2.imread('../data/lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

h,w,c = img.shape

#array 데이터를 QtGui.QImage 포맷으로 변환합니다.
qImg = QtGui.QImage(img.data, w, h, w*c, QtGui.QImage.Format_RGB888)
#변환된 이미지를 pixmap에 대입합니다.
pixmap = QtGui.QPixmap.fromImage(qImg)
label.setPixmap(pixmap)
label.resize(pixmap.width(), pixmap.height())
label.show()

app.exec_()
