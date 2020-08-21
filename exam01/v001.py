# OpenCV + PyQT
# 컬러 카메라, 흑백 카메라 동작 테스트

import cv2
import threading
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

#간단한 코드라 실행 상태를 전역변수로 만들어 확입합니다.
#코드가 길어지면 전역변수의 사용은 좋지 않습니다.
running = False
def run():
    global running
    #카메라에서 영상을 가져옵니다.
    cap = cv2.VideoCapture(0) #0 카메라
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    label.resize(width, height)
    while running:
        ret, img = cap.read()
        if ret:
            #openCV 함수를 이용해 가져온 이미지를 pyQT pixmap에 대입합니다.
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
            h,w,c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w*c, QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            label.setPixmap(pixmap)
        else:
            QtWidgets.QMessageBox.about(win, "Error", "Cannot read frame.")
            print("cannot read frame.")
            break
    cap.release() #리소스를 반환합니다.
    print("Thread end.")

def runGray():
    global running
    #카메라에서 영상을 가져옵니다.
    cap = cv2.VideoCapture(0) #0 카메라
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    label.resize(width, height)
    while running:
        ret, img = cap.read()
        if ret:
            #openCV 함수를 이용해 가져온 이미지를 pyQT pixmap에 대입합니다.
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
            h,w = img.shape
            qImg = QtGui.QImage(img.data, w, h, QtGui.QImage.Format_Grayscale8)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            label.setPixmap(pixmap)
        else:
            QtWidgets.QMessageBox.about(win, "Error", "Cannot read frame.")
            print("cannot read frame.")
            break
    cap.release() #리소스를 반환합니다.
    print("Thread end.")

def stop():
    global running
    running = False
    print("stoped..")

def start():
    global running
    running = True
    th = threading.Thread(target=run)
    th.start()
    print("started..")

def start_gray():
    global running
    running = True
    th = threading.Thread(target=runGray)
    th.start()
    print("gray started..")

def onExit():
    print("exit")
    stop()

app = QtWidgets.QApplication([])
win = QtWidgets.QWidget()
vbox = QtWidgets.QVBoxLayout()
label = QtWidgets.QLabel()
btn_start = QtWidgets.QPushButton("Camera On")
btn_gray = QtWidgets.QPushButton("Camera On - Gray")
btn_stop = QtWidgets.QPushButton("Camera Off")
vbox.addWidget(label)
vbox.addWidget(btn_start)
vbox.addWidget(btn_gray)
vbox.addWidget(btn_stop)
win.setLayout(vbox)
win.resize(600,480)
win.show()

#클릭시 새로운 스레드를 실행하고
btn_start.clicked.connect(start)
#stop 시 스레드 상태를 강제로 멈추게 합니다. 
#스레드 상태의 flag 변환의 경우 운영체제에서 거부될 수 있습니다. 차후 변경합니다.
btn_gray.clicked.connect(start_gray)
btn_stop.clicked.connect(stop)
app.aboutToQuit.connect(onExit)

sys.exit(app.exec_())