import time
import click as c
import pyautogui as pa
import webbrowser

#click1=5000円コース選択兼スタートクリック関数 click2=10000円コース click3=3000円コース
def start():
  url='https://sushida.net/play.html'
  webbrowser.open(url)
  time.sleep(3.25)
  c.click1() #スタートをクリックする
  time.sleep(0.85)
  c.click2() #ここでコースを選択
  time.sleep(0.15)
  pa.press("enter") #開始！
