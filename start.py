import time
import click as c
import pyautogui as pa
import webbrowser
#click1=5000円コース click2=10000円コース click3=3000円コース
def start():
  url='https://sushida.net/play.html'
  webbrowser.open(url)
  time.sleep(3.25)
  c.click1()
  time.sleep(0.85)
  c.click2() 
  time.sleep(0.25)
  pa.press("enter")
