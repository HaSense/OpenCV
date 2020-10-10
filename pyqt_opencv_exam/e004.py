import cv2
import threading
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

   
def filter_gray(): #흑백영상
    src = cv2.imread('../data/lena.jpg')
    src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) 
    h,w = src.shape
    print(h,w)
    qImg = QtGui.QImage(src.data, w, h, w*1, QtGui.QImage.Format_Grayscale8) #w*1 생략가능
    pixmap = QtGui.QPixmap.fromImage(qImg)
    label.setPixmap(pixmap)
    label.resize(pixmap.width(), pixmap.height())
    label.show()
    print("필터01 동작중")

def filter_blur(): #블러영상
    src = cv2.imread('../data/lena.jpg')
    src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) 
    h,w = src.shape
    blur= cv2.GaussianBlur(src, ksize=(7, 7), sigmaX=0.0)
    print(h,w)
    #byte per lines w*c
    qImg = QtGui.QImage(blur.data, w, h, w*1, QtGui.QImage.Format_Grayscale8)
    pixmap = QtGui.QPixmap.fromImage(qImg)
    label.setPixmap(pixmap)
    label.resize(pixmap.width(), pixmap.height())
    label.show()
    print("필터01 동작중")

def original_load():
    
    img = cv2.imread('../data/lena.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    h,w,c = img.shape
    print(h, w, c)
    qImg = QtGui.QImage(img.data, w, h, w*c, QtGui.QImage.Format_RGB888)
    pixmap = QtGui.QPixmap.fromImage(qImg)
    label.setPixmap(pixmap)
    label.resize(pixmap.width(), pixmap.height())
    label.show()
    print("원본 영상 출력")

def onExit():
    print("exit")
    stop()

app = QtWidgets.QApplication([])
win = QtWidgets.QWidget()
vbox = QtWidgets.QVBoxLayout()
label = QtWidgets.QLabel()
btn_origin = QtWidgets.QPushButton("원본 이미지 출력")
btn_gray = QtWidgets.QPushButton("흑백 이미지 출력")
btn_blur = QtWidgets.QPushButton("Blur 효과 출력")
vbox.addWidget(label)
vbox.addWidget(btn_origin)
vbox.addWidget(btn_gray)
vbox.addWidget(btn_blur)
win.setLayout(vbox)
win.resize(600,480)
win.show()


#버튼에 원본 이미지 출력 이벤트 등록 및 실행
btn_origin.clicked.connect(original_load)
#버튼에 필터1 효과
btn_gray.clicked.connect(filter_gray)
btn_blur.clicked.connect(filter_blur)
app.aboutToQuit.connect(onExit)

sys.exit(app.exec_())