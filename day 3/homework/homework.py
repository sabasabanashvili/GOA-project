from turtle import *
from turtle import*

speed(0)
bgcolor("skyblue")

#Grass
penup()
goto(-400, -100)
pendown()
color("limegreen")
begin_fill()
for i in range(2):
    forward(800)
    right(90)
    forward(400)
    right(90)
end_fill()

#Left Mountain
penup()
goto(-400, -100)
pendown()
color("dimgray")
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

#Right Mountain
penup()
goto(100, -100)
pendown()
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

#Middle Mountain
penup()
goto(-160, -100)
pendown()
color("gray")
begin_fill()
for i in range(3):
    forward(400)
    left(120)
end_fill()

#Middle Mountain Ice Cap
penup()
goto(-35, 120)
pendown()
color("white")
begin_fill()
left(35)
forward(60)
right(90)
forward(30)
left(100)
forward(45)
right(85)
forward(65)
left(160)
forward(150)
end_fill()

#Left Mountain Ice Cap
penup()
goto(-215, 100)
pendown()
color("snow")
begin_fill()
forward(70)
left(120)
forward(75)
left(150)
forward(45)
right(90)
forward(45)
left(120)
end_fill()

#Right Mountain Ice Cap
penup()
goto(203, 80)
pendown()
begin_fill()
forward(95)
right(120)
forward(80)
right(150)
forward(50)
left(70)
end_fill()

left(50)

#Sun
penup()
goto(-500, 350)
pendown()
color("yellow")
begin_fill()
circle(125)
end_fill()

#Tree
def tree():

    color("saddlebrown")
    begin_fill()
    for i in range(2):
        forward(40)
        left(90)
        forward(10)
        left(90)
    end_fill()


    forward(10)
    left(90)
    forward(5)


    color("forestgreen")
    begin_fill()
    circle(25)
    end_fill()

    right(90)



penup()
goto(-250,-110)
pendown()
fillcolor("gray20")
begin_fill()
width(3)
pencolor("black")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()
fillcolor("red")
begin_fill()
right(135)
forward(143)
right(90)
forward(140)
end_fill()
penup()
goto(-250,-110)
pendown()
right(45)
forward(200)
left(90)
forward(65)
left(90)
fillcolor("gray30")
begin_fill()
forward(90)
right(90)
forward(80)
right(90)
forward(90)
end_fill()
penup()
goto(-250,-110)
pendown()
fillcolor("white")
begin_fill()
left(90)
forward(30)
right(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()
fillcolor("white")
begin_fill()
right(90)
forward(40)
right(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()
penup()
goto(-250,-160)
pendown()
left(90)
width(1)
pencolor("black")
fillcolor("blue")
begin_fill()
forward(300)
left(90)
forward(100)
left(90)
forward(300)
end_fill()
penup()
goto(-50,-160)
pendown()
fillcolor("blue")
begin_fill()
forward(600)
right(90)
forward(100)
right(90)
forward(600)
end_fill()

#Plant the first tree
penup()
goto(-25,-80)
pendown()
left(90)
tree()
#Plant the first tree
penup()
goto(-350,-100)
pendown()
tree()
#Plant the first tree
penup()
goto(150,-100)
pendown()
tree()
#Plant the first tree
penup()
goto(-290,-250)
pendown()
tree()
#Plant the first tree
penup()
goto(290,-250)
pendown()
tree()
#Plant the first tree
penup()
goto(120,-270)
pendown()
tree()










exitonclick()