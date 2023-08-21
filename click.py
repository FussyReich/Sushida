import pyautogui as pa

def click1(): #5000円コース兼スタートクリック関数 
  pa.mouseDown(x=720,y=493, button='left')
  pa.mouseUp()
def click2(): #10000円コース選択用関数
  pa.mouseDown(x=715,y=560, button='left')
  pa.mouseUp()
def click3(): #3000円コース選択用関数
  pa.mouseDown(x=720,y=420, button='left')
  pa.mouseUp()
