import random
import tkinter as tk
import turtle
from tkinter import *
from tkinter import messagebox
from typing import List


root = tk.Tk()
root.title('Pattern Matching Game')
root.geometry("580x700")
root['background'] = '#65A062'
# icon
root.iconbitmap('C:\\Users\\Alionchik\\PycharmProjects\\pythonGuiProject\\images\\happy.png')

# canvas
frame = tk.Canvas()
screen = turtle.TurtleScreen(frame)
screen.bgcolor("black")
screen.screensize(canvwidth=200, canvheight=200)
frame.pack()

design = turtle.RawTurtle(screen)


# loadImg1 = Image.open('C:\\Users\\Alionchik\\PycharmProjects\\pythonGuiProject\\images\\watermonkey.jpg')
# img1 = ImageTk.PhotoImage(loadImg1)
# img11 = tk.Label(root, image=img1)
#
# loadImg2 = Image.open('C:\\Users\\Alionchik\\PycharmProjects\\pythonGuiProject\\images\\explosionDesign.png')
# img2 = ImageTk.PhotoImage(loadImg2)
# img22 = tk.Label(root, image=img2)
#
# loadImg3 = Image.open('C:\\Users\\Alionchik\\PycharmProjects\\pythonGuiProject\\images\\circlesDesign.png')
# img3 = ImageTk.PhotoImage(loadImg3)


def design1():
    design.pensize(2)
    design.color("purple", "yellow")
    design.speed(10)

    for j in range(3):
        for i in range(40):
            design.forward(i * 0.8)
            design.left(60)
            design.forward(20)


# create an animated drawing with turtle
def circlesFunc():
    colorList = ["#AA00FF", "#06CFDE", "#1AB789", "#FFA500", "#33FF00", "#FFFF00", "white", "#DD5018"]
    # pen size for width
    design.pensize(2)
    # speed of the animation [0] will be instant
    design.speed(0)
    # create design looping through colors
    for i in range(10):
        for colors in colorList:
            design.color(colors)
            design.circle(100)
            design.right(10)


cardMatches = ["giraffe", "giraffe", "panda", "panda", "koala", "koala", "tiger", "tiger", "panther", "panther", "owl",
               "owl"]
random.shuffle(cardMatches)

frame = tk.Frame(root)
frame.pack(pady=10)

roundCount = 0
winMatchCount = 0
answerList = []
answerDic = {}


# win screen
def win():
    label.config(text="Congratulations you won!!!", font=("Arial", 24))
    label.place()
    circlesFunc()
    allButtons = [btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11]
    for btn in allButtons:
        btn.config(bg="#2B4235")


# reset the game
def reset():
    global winMatchCount, cardMatches
    screen.clearscreen()
    winMatchCount = 0
    allButtons: List[Button] = [btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11]
    cardMatches = ["giraffe", "giraffe", "panda", "panda", "koala", "koala", "tiger", "tiger", "panther", "panther",
                   "owl", "owl"]
    random.shuffle(cardMatches)
    label.config(text='Playing Again...')
    for button in allButtons:
        button.config(text=" ", bg="SystemButtonFace", state="normal")


# key button named btn, value named num
def btnClick(btn, tile):
    global roundCount, answerDic, answerList, winMatchCount

    if btn["text"] == ' ' and roundCount < 2:
        btn["text"] = cardMatches[tile]
        answerList.append(tile)
        answerDic[btn] = cardMatches[tile]
        roundCount += 1

    # correct matches or not matched. checking against indexes of the list.
    if len(answerList) == 2:
        if cardMatches[answerList[0]] == cardMatches[answerList[1]]:
            label.config(text="MATCH", font=("Arial", 16))

            # disable matched
            for key in answerDic:
                key["bg"] = "#d5f5c9"
                key["state"] = "disabled"

                winMatchCount += 1
                if winMatchCount == 12:
                    win()

            # reset list,dic, and count
            roundCount = 0
            answerDic = {}
            answerList = []

        else:
            label.config(text="Oof, wrong!", font=("Arial", 16))
            roundCount = 0
            answerList = []
            # pop up when wrongly matched
            messagebox.showinfo("Oops, not a match!", "Oops, not a match!")
            label.config(text="Playing...", font=("Arial", 10))

            # reset the cards
            for key in answerDic:
                key["text"] = " "
            answerDic = {}


# Buttons with lambda that calls function when button clicked with two arguments
btn0 = Button(frame, text=' ', font=("Arial", 22), relief=RAISED, height=2, width=6, command=lambda: btnClick(btn0, 0))
btn1 = Button(frame, text=' ', font=("Arial", 22), relief=RAISED, height=2, width=6, command=lambda: btnClick(btn1, 1))
btn2 = Button(frame, text=' ', font=("Arial", 22), relief=RAISED, height=2, width=6, command=lambda: btnClick(btn2, 2))
btn3 = Button(frame, text=' ', font=("Arial", 22), relief=RAISED, height=2, width=6, command=lambda: btnClick(btn3, 3))
btn4 = Button(frame, text=' ', font=("Arial", 22), relief=RAISED, height=2, width=6, command=lambda: btnClick(btn4, 4))
btn5 = Button(frame, text=' ', font=("Arial", 22), relief=RAISED, height=2, width=6, command=lambda: btnClick(btn5, 5))
btn6 = Button(frame, text=' ', font=("Arial", 22), relief=RAISED, height=2, width=6, command=lambda: btnClick(btn6, 6))
btn7 = Button(frame, text=' ', font=("Arial", 22), relief=RAISED, height=2, width=6, command=lambda: btnClick(btn7, 7))
btn8 = Button(frame, text=' ', font=("Arial", 22), relief=RAISED, height=2, width=6, command=lambda: btnClick(btn8, 8))
btn9 = Button(frame, text=' ', font=("Arial", 22), relief=RAISED, height=2, width=6, command=lambda: btnClick(btn9, 9))
btn10 = Button(frame, text=' ', font=("Arial", 22), relief=RAISED, height=2, width=6,
               command=lambda: btnClick(btn10, 10))
btn11 = Button(frame, text=' ', font=("Arial", 22), relief=RAISED, height=2, width=6,
               command=lambda: btnClick(btn11, 11))

# Grid for buttons/cards
btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=0, column=3)

btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=1, column=3)

btn8.grid(row=2, column=0)
btn9.grid(row=2, column=1)
btn10.grid(row=2, column=2)
btn11.grid(row=2, column=3)

label = tk.Label(root, text='Lets Play: click on tile to find a matching pair!', font=("Arial", 10))
label.pack(pady=20)

# quit the game button
buttonQuit = Button(root, text='Quit', relief=RAISED, bg="#D85E4F", font=("Arial", 16), height=1, width=5,
                    command=root.quit)
buttonQuit.pack(side="left", padx=20)
# reset the game button
buttonReset = Button(root, text='Reset', relief=RAISED, bg="#EFCC6F", font=("Arial", 16), height=1, width=5,
                     command=reset)
buttonReset.pack(side="right", padx=20)
# end program loop
root.mainloop()
