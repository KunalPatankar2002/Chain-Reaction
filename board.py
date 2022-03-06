import tkinter as t
import tkinter.font


# noinspection PyUnresolvedReferences
def resetBoard():
    turn.set(0)

    for x in range(rowSize):
        for y in range(colSize):
            value = 0
            val[x][y] = t.StringVar()
            btn[x][y] = t.Button(frame, textvariable=val[x][y], command=lambda x=x, y=y: add(x, y))
            btn[x][y]["width"] = 6
            btn[x][y]["height"] = 3
            btn[x][y]["bg"] = "black"
            btn[x][y]["fg"] = "white"
            btn[x][y]["activebackground"] = "white"
            btn[x][y]["activeforeground"] = "white"
            btn[x][y]["font"] = fontForGame
            val[x][y].set(value)
            btn[x][y].grid(row=x, column=y)


def add(x, y):
    # TO DO: add player check (red can play red, etc)
    addAtom(x, y)
    passTurn()


def addAtom(x, y):
    value = 1 + int(val[x][y].get())
    if value > maxSize(x, y):
        return

    btn[x][y]["bg"] = color[turn.get() % playersCount]

    if value == maxSize(x, y):
        btn[x][y]["bg"] = "black"
        val[x][y].set(0)
        expand(x, y)
    else:
        val[x][y].set(value)


def expand(x, y):
    if x - 1 >= 0:
        # left
        addAtom(x - 1, y)
    if x + 1 <= rowSize - 1:
        # right
        addAtom(x + 1, y)
    if y - 1 >= 0:
        # down
        addAtom(x, y - 1)
    if y + 1 <= colSize - 1:
        # up
        addAtom(x, y + 1)
    return


def maxSize(x, y):
    """
    :param x: column no
    :param y: row no
    :return: maximum value a cell can hold depending on position (corner, edge, middle)
    """
    size = 4
    if x == rowSize - 1 or x == 0:
        size = size - 1
    if y == colSize - 1 or y == 0:
        size = size - 1
    return size


def passTurn():
    # increment move if a valid one is made to give chance to next player
    turn.set(turn.get() + 1)



window = t.Tk()

# required font style
fontForGame = tkinter.font.Font(family='Times', size=12, weight='bold')

# it's just an integer with more options/functions
turn = t.IntVar()

frame = t.Frame(window)
frame.pack()

# set the dimensions of the board
rowSize = 7
colSize = 7

playersCount = 2
color = ["blue", "violet"]

btn = [[0 for y in range(colSize)] for x in range(rowSize)]
val = [[0 for y in range(colSize)] for x in range(rowSize)]

resetBoard()

window.mainloop()
