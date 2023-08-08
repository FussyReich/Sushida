import sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as f
import webbrowser
webbrowser.open('https://sushida.net/play.html')

def close():
    root.destroy()

def sushi():
    import main

root = tk.Tk()
root.title("寿司打をぶっ壊す")
root.geometry("350x150")

#メインフレームの作成
frame=tk.Frame(root)
frame.pack(fill=tk.BOTH, pady=10)
SushiButton=ttk.Button(frame, text="実行する", command=sushi)

#ウィジェットの作成
Title=tk.Label(frame, text="自動で寿司打をやってもらおう()", font=("MSゴシック", "20", "bold"))

#ウィジェットの配置
Title.pack()
SushiButton.pack(pady=10)

root.mainloop()
