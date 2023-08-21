import pyautogui as pa
import time
from PIL import Image
import sys
import pyocr
import pyocr.builders
import start as s
from PIL import ImageGrab as ig
import os
import shutil
import screenshot_pyocr as sp

s.start()
nowtime=time.time()
while True:
    if time.time()-nowtime>1.5:
        break
t=0
while t<8:
    if t==8:
        break
    img_name=(f'./screenshots/{t}.png')
    ig.grab(bbox=(598,468,822,493)).save(img_name)
    Str=sp.scpy(img_name)
    pa.typewrite(Str, interval = 0.0)
    t+=1
    path='./screenshots'
    #shutil.rmtree(path)  
    #os.mkdir(path)
p=ord('a')
while True:
    if time.time() - nowtime > 300:
        break
    screenshot_name=(f'./screenshots/{chr(p)}.png')
    print(f'{screenshot_name}を保存しました')
    ig.grab(bbox=(535,468,885,493)).save(screenshot_name) #10000円コース用
    #ig.grab(bbox=(598,468,822,493)).save(screenshot_name) #5000円コース用
    #ig.grab(bbox=(640,468,788,492)).save(screenshot_name) #3000円コース用
    string=sp.scpy(screenshot_name)
    pa.typewrite(string, interval = 0.0)
    nowtime1 = time.time()
    while True:
        if time.time() - nowtime1 > 0.25: 
            break
    p+=1
    path='./screenshots'
    #shutil.rmtree(path)  
    #os.mkdir(path)