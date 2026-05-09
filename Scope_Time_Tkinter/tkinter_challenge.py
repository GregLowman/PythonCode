"""Tkinter calculator with grid layout: resizable title bar, result entry, and button grid."""
import tkinter

main_window = tkinter.Tk()

large_font = ('arial', 20)
medium_font = ('arial', 10)
small_font = ('arial', 5)

main_window.title("Calculator")
main_window.geometry('640x480-8-200')
main_window.configure(bg='grey80')
main_window['padx'] = 8

main_window.rowconfigure(0, weight=8)
main_window.rowconfigure(1, weight=10)

for i in range(2, 7):
    main_window.rowconfigure(i, weight=50)
for i in range(0, 4):
    main_window.columnconfigure(i, weight=50)

label_frame = tkinter.LabelFrame(main_window)
label_frame.grid(row=0, column=0, columnspan=4, sticky='news')
label_frame.configure(bg='grey15')

label = tkinter.Label(label_frame, text='Calculator', font=large_font, width=20, fg='white', bg='grey15')
label.grid(row=0, column=4, sticky='e')

cancel_button = tkinter.Button(label_frame, text="X", font=large_font, width=1, bg='orangered3', command=main_window.destroy)
cancel_button.grid(row=0, column=0, sticky='ew')

minimize_button = tkinter.Button(label_frame, text="-", font=large_font, width=1, bg='grey25')
minimize_button.grid(row=0, column=1, sticky='ew')

maximize_button = tkinter.Button(label_frame, text="[]", font=large_font, width=1, bg='grey25')
maximize_button.grid(row=0, column=2, sticky='ew')

result_frame = tkinter.Entry(main_window)
result_frame.grid(row=1, column=0, columnspan=4, sticky='news')
result_frame.configure(border=4, relief='sunken')

buttons = ["C", "CE", "Del", "%",
           "7", "8", "9", "+",
           "4", "5", "6", "-",
           "1", "2", "3", "*",
           "0", "=", "/"]

columns = 0
rows = 2
stick = 'ewns'

for i in range(0, len(buttons)):
    if buttons[i] == '=':
        tkinter.Button(main_window, text=buttons[i], font=medium_font).grid(row=rows, column=columns, sticky=stick, padx=1, columnspan=2)
        columns += 2

    else:
        tkinter.Button(main_window, text=buttons[i], font=medium_font).grid(row=rows, column=columns, sticky=stick, padx=1, columnspan=1)
        columns += 1

    if columns == 4:
        rows += 1
        columns = 0

main_window.mainloop()
