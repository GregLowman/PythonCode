"""Tkinter Hangman UI scaffold: letter grid, hangman canvas, used-letters panel, and word slots."""
import tkinter

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

letters_font = ('Bodoni MT Black', 15, 'bold')
title_font = ('Arial', 15, 'bold')
available_font = ('Rockwell Condensed', 17, 'bold', 'italic')
used_font = ('Arial', 12, 'bold', 'italic', 'underline')


used_letters = {}

for i in range(0, len(letters)):
    used_letters.setdefault(f"{i}", letters[i])

main_window = tkinter.Tk()
main_window.geometry('950x550+350+150')
main_window['pady'] = 5
main_window['padx'] = 5
main_window.configure(bg='grey69')

for i in range(0, 4):
    main_window.rowconfigure(i, weight=1)
    if i != 3:
        main_window.columnconfigure(i, weight=1)

top_title = tkinter.LabelFrame(main_window, bd=0, bg='grey69')
top_title.grid(row=0, column=0, columnspan=3, sticky='new')

for i in range(0, 3):
    top_title.columnconfigure(i, weight=1)

game_title = tkinter.Label(top_title, text="Hangman", font=title_font, bg='grey69')
game_title.grid(row=0, column=1)

hangman_graphic = tkinter.LabelFrame(main_window, width=150, bd=15, bg='dark turquoise')
hangman_graphic.grid(row=1, column=0, rowspan=2, sticky='nwse')
hangman_graphic.grid_propagate(0)

used_letters_box = tkinter.LabelFrame(main_window, text="Used Letters", font=used_font, bd=0, bg='grey69')
used_letters_box.grid(row=1, column=2, rowspan=2, sticky='n')
columns = 0
rows = 0

for i in range(0, len(letters)):
    tkinter.Menubutton(used_letters_box, bg='grey69').grid(column=columns, row=rows)
    rows += 1
    if rows == 13:
        rows = 0
        columns += 1

correct_letters_slot = tkinter.Frame(main_window)
correct_letters_slot.grid(row=2, column=1)
rows = 0
columns = 0
for i in range(0, 8):
    tkinter.Menubutton(correct_letters_slot, text='___', font='bold', bg='grey69').grid(row=rows, column=columns)
    columns += 1

letter_box = tkinter.LabelFrame(main_window, bg='snow2')
letter_box.grid(row=4, column=0, columnspan=3, sticky='sew')
letter_box['pady'] = 5

letter_label = tkinter.Label(main_window, text='Available Letters', font=available_font, bg='grey69')
letter_label.grid(row=3, column=0, columnspan=3, sticky='swe')

for i in range(0, 13):
    letter_box.columnconfigure(i, weight=1)
for i in range(0, 3):
    letter_box.rowconfigure(i, weight=1)

rows = 1
columns = 0
stick = 'ew'

for i in range(0, len(letters)):
    if letters[i] == 'A' or letters[i] == 'N':
        tkinter.Button(letter_box, text=letters[i], font=letters_font, bg='snow2')\
            .grid(row=rows, column=columns, sticky=stick, padx=(5, 0))
    elif letters[i] == 'M' or letters[i] == 'Z':
        tkinter.Button(letter_box, text=letters[i], font=letters_font, bg='snow2')\
            .grid(row=rows, column=columns, sticky=stick, padx=(0, 5))
    else:
        tkinter.Button(letter_box, text=letters[i], font=letters_font, bg='snow2')\
            .grid(row=rows, column=columns, sticky=stick)

    columns += 1

    if columns == 13:
        columns = 0
        rows += 1


main_window.mainloop()
