from turtle import *

#def მიდგომა
def draw_square(x_coordinate, y_coordinate):
    penup()
    goto(x_coordinate, y_coordinate)
    pendown()

    for i in range(4):
        forward(100)
        right(90)

    draw_square(100,100)
    draw_square(-300,200)
    draw_square(100,-300)
    draw_square(-300,-300)

