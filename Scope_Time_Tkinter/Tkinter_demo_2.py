"""Tkinter grid layout demo: label, canvas, and resizable button panel in a two-frame window."""
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

main_window = tkinter.Tk()

main_window.title("Hello World")
main_window.geometry('640x480+600+200')

label = tkinter.Label(main_window, text="Hello World")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(main_window)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(main_window)
rightFrame.grid(row=1, column=2, sticky='n')


button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button1.grid(sticky='ew')
button2.grid(sticky='ew')
button3.grid(sticky='ew')
main_window.mainloop()


