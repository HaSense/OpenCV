import cv2
import threading
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout

capture = cv2.VideoCapture('../data/vtest.avi')

def origin(): #원본
    global capture
    while True:
        if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
            capture.open('../data/vtest.avi')

        ret, frame = capture.read()
        cv2.imshow("VideoFrame", frame)

        if cv2.waitKey(33) > 0:
            break
def gray(): #흑백
    global capture
    #capture = cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY)
    while True:
        if (capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
            capture.open('../data/vtest.avi')

        ret, frame = capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("VideoFrame", frame)

        if cv2.waitKey(33) > 0:
            break
def blur(): #블러
    global capture
    #capture = cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY) #스칼라값으로 받으면 pyqt에서 에러발생
    while True:
        if (capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
            capture.open('../data/vtest.avi')

        ret, frame = capture.read()
        cv2.imshow("VideoFrame", frame)

        if cv2.waitKey(33) > 0:
            break
def onExit():
    print("exit")


app = QtWidgets.QApplication([])
win = QtWidgets.QWidget()
grid = QGridLayout()
hbox = QHBoxLayout()
vbox = QVBoxLayout()
label = QtWidgets.QLabel()
btn_origin = QtWidgets.QPushButton("원본 영상 출력")
btn_gray = QtWidgets.QPushButton("흑백 영상 출력")
btn_blur = QtWidgets.QPushButton("Blur 효과 출력")

grid.addWidget((btn_origin), 0,10)
grid.addWidget((btn_gray),1,10)
grid.addWidget((btn_blur),2,10)


win.setLayout(grid)
win.resize(600, 480)
win.show()

# 버튼에 원본 이미지 출력 이벤트 등록 및 실행
btn_origin.clicked.connect(origin)
# 버튼에 필터1 효과
btn_gray.clicked.connect(gray)
btn_blur.clicked.connect(blur)
app.aboutToQuit.connect(onExit)

sys.exit(app.exec_())
capture.release()
cv2.destroyAllWindows()