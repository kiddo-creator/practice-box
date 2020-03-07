from tkinter import *
import tkinter.messagebox

top = Tk("")

top.geometry("500x300")

def fun():
    tkinter.messagebox.showinfo("인사","안녕하세요")

b = Button(top,text="게임시작", command=fun, activebackground="orange")

b.pack()

top.mainloop()
