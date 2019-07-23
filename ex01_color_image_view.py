import cv2
import matplotlib.pyplot as plt

Lena = "./data/lena.jpg"

img = cv2.imread(Lena)      #cv2.IMREAD_COLOR
cv2.imshow('Lena color', img) #일반적인 OpenCV용 이미지 출력함수

plt.axis('off')   #가로, 세로 눈금자를 없애 줍니다.
plt.imshow(img)   #그림을 출력하는 함수
plt.show()        #plt 윈도우를 화면에 출력합니다. 
                  #재미있는 것은 plt로 출력시 이미지가 BGR형식으로 출력됩니다.
                  #따라서 BGR형식을 RGB형식으로 출력되도록 하는 함수가 필요합니다.
img_color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_color)
plt.show()

#창이 바로 사라지는 현상이 있습니다. 방지하기 위해서는 waitKey()함수를 실행해 주세요
#waitKey함수의 매개변수는 밀리초입니다. 
cv2.waitKey(5000)
cv2.destroyAllWindows()