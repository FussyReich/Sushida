import pyautogui as pa
import webbrowser
import time
from PIL import Image
import sys

import pyocr
import pyocr.builders
import click as c
from PIL import ImageGrab as ig
import os
import shutil

url='https://sushida.net/play.html'
webbrowser.open(url)
time.sleep(3.25)
c.click1()
time.sleep(0.75)
c.click3() #click1=5000円コース click2=10000円コース click3=3000円コース
time.sleep(0.25)
pa.press("enter")
p=ord('a')
nowtime=time.time()
while True:
    if time.time()-nowtime>1.5:
        break
while True:
    if time.time() - nowtime > 300:
        break
    #ig.grab(bbox=(550,468,875,493)).save(f'./screenshots/{chr(p)}.png') #10000円コース用
    #ig.grab(bbox=(600,468,820,493)).save(f'./screenshots/{chr(p)}.png') #5000円コース用
    ig.grab(bbox=(640,468,788,492)).save(f'./screenshots/{chr(p)}.png') #3000円コース用
    screenshot_name=(f'./screenshots/{chr(p)}.png')
    def test(screenshot_name):
        tools = pyocr.get_available_tools()
        tool = tools[0]

        langs = tool.get_available_languages()
        lang = langs[0]
        #txtに変換した文字列を代入する
        txt = tool.image_to_string(
            Image.open(screenshot_name),
            lang="eng",
            builder=pyocr.builders.TextBuilder(tesseract_layout=6)
        )
        Text = list(txt)   #文字列を配列に変換
        count = len(Text)
        txt = str(''.join(Text))   #文字列に戻す
        print(txt)
        return txt
    string=test(screenshot_name)
    pa.typewrite(string, interval = 0.0)
    nowtime1 = time.time()
    while True:
        if time.time() - nowtime1 > 0.25: 
            break
    p+=1
    path='./screenshots'
    #shutil.rmtree(path)  
    #os.mkdir(path)