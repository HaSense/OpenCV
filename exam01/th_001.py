#스레드 종료 테스트

import cv2
import threading
import sys
import time

global cnt

running = False
def run():
    global running
    while running:
        cnt += 1
        print(f'Thread-1 : {cnt}')
        time.sleep(1)
    
    print("Thread end.")

def runGray():
    global running
    while running:
        cnt += 1
        print(f'Thread-2 : {cnt}')
        time.sleep(1)
    
    print("Thread end.")

def stop():
    global running
    running = False
    print("stoped..")
