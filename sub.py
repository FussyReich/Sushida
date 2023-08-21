import pyautogui as pa
import screenshot_pyocr as sp
from PIL import ImageGrab as ig
import os
import shutil

def f():
    t=0
    while t<8: #最初の方はタイピング量が少ないのでスクショ範囲を5000円コースにする
        if t==8:
            break
        img_name=(f'./screenshots/{t}.png')
        ig.grab(bbox=(598,468,822,493)).save(img_name)
        Str=sp.scpy(img_name)
        pa.typewrite(Str, interval = 0.0)
        path='./screenshots'
        #画像ファイルを定期的に削除する
        shutil.rmtree(path)  
        os.mkdir(path)
        t+=1
