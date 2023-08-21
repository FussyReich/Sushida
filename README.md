## 使い方
### 起動したいとき
#### 以下のコマンドを実行
###### 2回目以降は```python main.py```だけでOK
```
mkdir screenshots
python main.py
```
### コースを変更したいとき
初期設定では10000円コースになっていますが
変更したい場合には以下の部分を変更します
**main.pyに移動**
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

**start.pyに移動**
##### 3000円コースにしたい場合はclick3 5000円コースにしたい場合はclick1に変更してください
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