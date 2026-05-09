"""Tkinter intro: pack layout with a label, canvas, and three buttons in left/right frames."""
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

main_window = tkinter.Tk()

main_window.title("Hello World")
main_window.geometry('640x480+600+200')

label = tkinter.Label(main_window, text="Hello World")
label.pack(side='top')

leftFrame = tkinter.Frame(main_window)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(main_window)
rightFrame.pack(side='right', anchor='n', expand=True)


button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')
main_window.mainloop()

