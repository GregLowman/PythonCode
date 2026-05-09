"""Tkinter calculator UI prototype: title bar, result entry, and dynamically-laid button grid."""
import tkinter

main_window = tkinter.Tk()

large_font = ('arial', 20)
medium_font = ('arial', 10)
small_font = ('arial', 5)

main_window.title("Calculator")
main_window.geometry('640x480-8-200')
main_window.configure(bg='grey80')
main_window['padx'] = 8

label_frame = tkinter.LabelFrame(main_window)
label_frame.grid(row=0, column=0, sticky='news')
label_frame.configure(bg='grey15')

label = tkinter.Label(label_frame, text='Calculator', font=medium_font, width=20, fg='white', bg='grey15')
label.grid(row=0, column=3, sticky='e')

cancel_button = tkinter.Button(label_frame, text="X", font=medium_font, width=1, bg='orangered3', command=main_window.destroy)
cancel_button.grid(row=0, column=0, sticky='ew')

minimize_button = tkinter.Button(label_frame, text="-", font=medium_font, width=1, bg='grey25')
minimize_button.grid(row=0, column=1, sticky='ew')

maximize_button = tkinter.Button(label_frame, text="[]", font=medium_font, width=1, bg='grey25')
maximize_button.grid(row=0, column=2, sticky='ew')

result_frame = tkinter.Entry(main_window)
result_frame.grid(row=1, column=0, sticky='news')
result_frame.configure(border=4, relief='sunken')

buttons = ["C", "CE", "Del", "%",
           "7", "8", "9", "+",
           "4", "5", "6", "-",
           "1", "2", "3", "*",
           "0", "=", "/"]

columns = 0
rows = 0
stick = 'ew'
key_pad = tkinter.Frame(main_window)
key_pad.grid(row=2, column=0, sticky='nswe')
for i in range(0, len(buttons)):
    if buttons[i] == '=':
        tkinter.Button(key_pad, text=buttons[i], font=medium_font).grid(row=rows, column=columns, sticky=stick, padx=1, columnspan=2)
        columns += 2

    else:
        tkinter.Button(key_pad, text=buttons[i], font=medium_font).grid(row=rows, column=columns, sticky=stick, padx=1, columnspan=1)
        columns += 1

    if columns == 4:
        rows += 1
        columns = 0

main_window.update()
main_window.minsize(key_pad.winfo_width() + 8,
                    result_frame.winfo_height() +
                    key_pad.winfo_height() +
                    label_frame.winfo_height())
main_window.maxsize(key_pad.winfo_width() + 8,
                    result_frame.winfo_height() +
                    key_pad.winfo_height() +
                    label_frame.winfo_height())
main_window.mainloop()
