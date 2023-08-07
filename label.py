import sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as f

def close():
    root.destroy()

root = tk.Tk()
root.title("寿司打をぶっ壊す")
root.geometry("350x150")

Header=tk.Label(text=u'寿司打を自動でやってもらおう！()')
Header.pack()

root.mainloop()
