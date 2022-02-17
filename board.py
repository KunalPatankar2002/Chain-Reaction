# author: Cherubim anand
# PVP Chain reaction game developed using tkinter

import tkinter as t
import tkinter.font


# resets up the board for new game
def resetBoard():
    turn.set(0)

    # reset notification button
    turnNote.set("It's player " + str(turn.get() + 1) + "'s turn!")

    for x in range(rowSize):
        for y in range(colSize):
            value = 0
            val[x][y] = t.StringVar()
            btn[x][y] = t.Button(frame, textvariable=val[x][y], command=lambda x=x, y=y: add(x, y))
            btn[x][y]["width"] = 6
            btn[x][y]["height"] = 3
            btn[x][y]["bg"] = "black"
            btn[x][y]["fg"] = "blue"
            btn[x][y]["activebackground"] = "white"
            btn[x][y]["activeforeground"] = "white"

            val[x][y].set(value)
            btn[x][y].grid(row=x, column=y)


window = t.Tk()

# variable to toggle turns
turn = t.IntVar()

# Button to reset game
t.Button(window, text="RESET", command=resetBoard).pack()

# String variable to notify which player's turn
turnNote = t.StringVar()

# Label to show turnNote
t.Label(window, textvariable=turnNote).pack()

# frame to organize elements
frame = t.Frame(window)
frame.pack()

# set the dimensions of the board
rowSize = 8
colSize = 6

btn = [[0 for y in range(colSize)] for x in range(rowSize)]
val = [[0 for y in range(colSize)] for x in range(rowSize)]

resetBoard()

window.mainloop()
