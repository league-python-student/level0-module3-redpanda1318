import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    t = turtle.Turtle()
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(80)

    #      3) Set the pen width to 10
    t.width(10)

    #      4) Ask the user what color pen they would like to draw with
    for i in range(20):

        color = simpledialog.askstring(title = 'colors',prompt = "What color would you like to draw with?")



    #      5) Use an if/else statement to set the pen color that the user
    #         requested
        if color == "red":
            turtle.pencolor('red')


        elif color == "orange":
            turtle.pencolor('orange')

        elif color == "yellow":
            turtle.pencolor('yellow')

        elif color == "green":
            turtle.pencolor('green')

        elif color == "blue":
            turtle.pencolor('blue')

        elif color == "purple":
            turtle.pencolor('purple')

        elif color == "pink":
            turtle.pencolor('pink')

    #      6) If the user doesn't enter anything, choose a random color
        else:
            turtle.pencolor(get_random_color())

        turtle.forward(150)
        turtle.right(90)
        turtle.forward(80)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(80)

    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them


    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
