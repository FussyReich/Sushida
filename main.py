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
import sub

s.start()
nowtime=time.time()
while True:
    if time.time()-nowtime>1.5:
        break
sub.f() #10000円コース以外はコメント化
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
    #画像ファイルを定期的に削除する
    shutil.rmtree(path)  
    os.mkdir(path)