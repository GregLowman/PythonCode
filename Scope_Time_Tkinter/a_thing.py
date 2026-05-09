"""Tkinter Hangman game: canvas scaffold, difficulty selection, letter guessing, and win/lose logic."""
from tkinter import *

import random as r

import time as tm


class menu:

    def __init__(self):

        self.game = Tk()

        self.game.geometry('600x600+50+50')

        self.game.title("Hang Man")

        self.canvas = Canvas(self.game,height=400,width=800,bg='light goldenrod yellow')

        self.canvas.delete(ALL)

        self.canvas.create_line(100,50,100,500,tags="Line")

        self.canvas.create_line(20,500,80,500,tags="Line")

        self.canvas.create_line(100,50,150,50,tags="Line")

        self.canvas.pack()

        self.play = Button(self.game,text="Play",command=self.playbt)

        self.play.pack(side=BOTTOM)

        self.game.mainloop()

    def playagain(self):

        self.game.destroy()

        self.__init__()

    def playbt(self):

        self.difs()



    def difs(self):

        self.play.destroy()

        self.easy = Button(self.game,text="Easy",command=self.easy)

        self.medium = Button(self.game,text="Medium",command=self.medium)

        self.hard = Button(self.game,text="Hard",command=self.hard)



        self.easy.pack(side=BOTTOM)

        self.medium.pack(side=BOTTOM)

        self.hard.pack(side=BOTTOM)



    def easy(self):

        ewords = r.choice(["TABLE","CHAIR","DESK","PHONE","LIGHT","MAN"])

        self.playP(ewords.lower())

    def medium(self):

        mwords = r.choice(["PYTHON","LAPTOP","JACKET","VIDEO","MODULE","LIBRARY"])

        self.playP(mwords.lower())

    def hard(self):

        hwords = r.choice(["PROGRAM","TOLEDO","UNIVERSITY","ENGINEER","FOOTBALL","LANGUAGE"])

        self.playP(hwords.lower())



    def playP(self,words):

        self.lwords = words

        for i in range(0, len(self.lwords)):

            self.canvas.create_text(300+20*i,310,text="_",font="Times 16",tags="text")

        self.hm = 0

        self.easy.destroy()

        self.medium.destroy()

        self.hard.destroy()

        self.myscore = int(0)



        self.te = StringVar()

        self.teb = Entry(self.game, textvariable = self.te)

        self.tebt = Button(self.game,text="Submit", command = self.checkAnswer)

        self.teb.pack(side=BOTTOM)

        self.tebt.pack(side=BOTTOM)




    def checkAnswer(self):

        temp= self.te.get()

        score=0

        score1=0

        x1=300


        for i in range(0,len(self.lwords)):



            if temp==self.lwords[i]:

                self.canvas.create_text(x1+20*i,300,text=self.lwords[i],font="Times 16",tags="text")

                score1+=1

                self.myscore += 1


            if self.myscore == len(self.lwords):

                self.win()


        if not (score1 > score):

            self.draw()

            score=0

            score1



    def win(self):

        self.canvas.delete(ALL)

        self.canvas.after(100)

        self.teb.destroy()

        self.tebt.destroy()

        self.canvas.create_text(400,200,text = 'YOU WIN!!',font='Times 36')

        self.pa = Button(self.game,text="Play Again?",command=self.playagain)

        self.pa.pack(side=BOTTOM)



    def draw(self):

        self.hm += 1

        if self.hm == 1:

            self.canvas.create_oval(125,50,175,100, tags = "Line")

        elif self.hm == 2:

            self.canvas.create_line(150,100,150,150, tags = "Line")

        elif self.hm == 3:

            self.canvas.create_line(150,125,125,100, tags = "Line")

        elif self.hm == 4:

            self.canvas.create_line(150, 125, 175, 100, tags = "Line")

        elif self.hm == 5:

            self.canvas.create_line(150,150,125,175, tags = "Line")

        elif self.hm == 6:

            self.canvas.create_line(150,150,175,175, tags = "Line")

            self.canvas.update()

            self.canvas.after(100)

            self.canvas.delete(ALL)

            self.canvas.create_text(200,200,text="HANG MAN!!",font="Times 36")

            self.tebt.destroy()

            self.teb.destroy()

            self.pa = Button(self.game,text="Play Again?",command=self.playagain)

            self.pa.pack(side=BOTTOM)


menu()
