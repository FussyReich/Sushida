import pyautogui as pa
import webbrowser
import time

url='https://sushida.net/play.html'
webbrowser.open(url)
pa.mouseDown(x=720,y=493, button='left')
pa.mouseUp()
pa.typewrite(' ', interval=0.0)
i=ord('a')
nowtime=time.time()
while True:
    if time.time()-nowtime>1.5:
        break
while True:
    if time.time() - nowtime > 300:
        break
    screen_shot=pa.screenshot(
        region=(797, 588, 275, 30)
    )
    screen_shot.save(f'./screenshot/{chr(i)}.png') 
    i+=1 