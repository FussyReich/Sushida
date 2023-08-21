## 使い方
### 起動したいとき
#### 以下のコマンドを実行
##### 2回目以降は```python main.py```だけでOK
```
mkdir screenshots
pip install pillow
pip install pyautogui
pip install pyocr
brew install tesseract
wget https://github.com/tesseract-ocr/tessdata/raw/4.00/jpn.traineddata
mv jpn.traineddata /usr/local/Cellar/tesseract/4.1.0/share/tessdata/
python main.py
```
### コースを変更したいとき
初期設定では10000円コースになっていますが
変更したい場合には以下の部分を変更します
##### main.pyに移動
###### Before
```python
s.start()
nowtime=time.time()
while True:
    if time.time()-nowtime>1.5:
        break
sub.f() #10000円コース以外はコメント化 <<<ここを変更
p=ord('a')
```

###### After
```python
s.start()
nowtime=time.time()
while True:
    if time.time()-nowtime>1.5:
        break
#sub.f() #10000円コース以外はコメント化
p=ord('a')
```
###### Before
```python
while True:
    if time.time() - nowtime > 300:
        break
    screenshot_name=(f'./screenshots/{chr(p)}.png')
    print(f'{screenshot_name}を保存しました')
    ig.grab(bbox=(535,468,885,493)).save(screenshot_name) #10000円コース用 <<< ここを変更
    #ig.grab(bbox=(598,468,822,493)).save(screenshot_name) #5000円コース用 <<< ここを変更
    #ig.grab(bbox=(640,468,788,492)).save(screenshot_name) #3000円コース用 <<< ここを変更
    string=sp.scpy(screenshot_name)
    pa.typewrite(string, interval = 0.0)
```
###### After(3000円コース)
```python
while True:
    if time.time() - nowtime > 300:
        break
    screenshot_name=(f'./screenshots/{chr(p)}.png')
    print(f'{screenshot_name}を保存しました')
    #ig.grab(bbox=(535,468,885,493)).save(screenshot_name) #10000円コース用
    #ig.grab(bbox=(598,468,822,493)).save(screenshot_name) #5000円コース用
    ig.grab(bbox=(640,468,788,492)).save(screenshot_name) #3000円コース用
    string=sp.scpy(screenshot_name)
    pa.typewrite(string, interval = 0.0)
```
###### After(5000円コース)
```python
while True:
    if time.time() - nowtime > 300:
        break
    screenshot_name=(f'./screenshots/{chr(p)}.png')
    print(f'{screenshot_name}を保存しました')
    #ig.grab(bbox=(535,468,885,493)).save(screenshot_name) #10000円コース用
    #ig.grab(bbox=(598,468,822,493)).save(screenshot_name) #5000円コース用
    ig.grab(bbox=(640,468,788,492)).save(screenshot_name) #3000円コース用
    string=sp.scpy(screenshot_name)
    pa.typewrite(string, interval = 0.0)
```
**start.pyに移動**
##### 3000円コースにしたい場合は**click3** 5000円コースにしたい場合は**click1**に変更してください
###### Before
```python
def start():
  url='https://sushida.net/play.html'
  webbrowser.open(url)
  time.sleep(3.25)
  c.click1() #スタートをクリックする
  time.sleep(0.85)
  c.click2() #ここでコースを選択 <<<ここを変更
  time.sleep(0.25)
  pa.press("enter")
```
###### After(3000円コース)
```python
def start():
  url='https://sushida.net/play.html'
  webbrowser.open(url)
  time.sleep(3.25)
  c.click1() #スタートをクリックする
  time.sleep(0.85)
  c.click3() #ここでコースを選択 <<<ここを変更
  time.sleep(0.25)
  pa.press("enter")
```
###### After(5000円コース)
```python
def start():
  url='https://sushida.net/play.html'
  webbrowser.open(url)
  time.sleep(3.25)
  c.click1() #スタートをクリックする
  time.sleep(0.85)
  c.click1() #ここでコースを選択 <<<ここを変更
  time.sleep(0.25)
  pa.press("enter")
```