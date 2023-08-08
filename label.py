import sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as f

def close():
    root.destroy()

root = tk.Tk()
root.title("寿司打をぶっ壊す")
root.geometry("350x150")

#メインフレームの作成
frame=tk.Frame(root)
frame.pack(fill=tk.BOTH, pady=10)

#ウィジェットの作成
Title=tk.Label(frame, text="自動で寿司打をやってもらおう()", font=("MSゴシック", "20", "bold"))

#ウィジェットの配置
Title.pack()

root.mainloop()
