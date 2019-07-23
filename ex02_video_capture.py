import cv2

video = cv2.VideoCapture(0) #0번 카메라
#video = cv2.VideoCapture('/data/vtest.avi')    #저장된 동영상 실행

video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 
#              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) #실제화면의 크기로 

#print('frame_size : ', frame_size)  #실제화면 크기로 할때 화면 사이즈 보여주기

while True:
    retVal, frame = video.read() #프레임 캡쳐
    if not retVal:
        break
    
    cv2.imshow('frame', frame)

    key = cv2.waitKey(50) #50밀리세컨드
    if key == 27: #esc
        break

if video.isOpened():  #혹시 영상이 오픈되어있다면 해제한다.
    video.release()
cv2.destroyAllWindows()  #모든 열려있는 윈도우를 닫는다.




