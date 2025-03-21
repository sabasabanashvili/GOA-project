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

#Plant the first tree
penup()
goto(-25,-200)
pendown()
tree()

#Plant the second tree
penup()
goto(200,-150)
pendown()
tree()

#Plant the third tree
penup()
goto(300,-250)
pendown()
tree()

#Plant the fourth tree
penup()
goto(-300,-250)
pendown()
tree()

#Plant the fifth tree
penup()
goto(-200,-100)
pendown()
tree()

#Building A Castle
width(2)
penup()
goto(-300,-300)
pendown()
pencolor("black")
fillcolor("gray")
begin_fill()
left(90)
forward(600)
left(90)
forward(400)
left(90)
forward(100)
left(90)
forward(400)
right(90)
forward(500)
right(90)
forward(400)
right(90)
forward(100)
right(90)
forward(400)
right(180)
forward(300)
right(90)
forward(400)
left(90)
forward(100)
left(90)
end_fill()
fillcolor("red")
begin_fill()
forward(30)
right(90)
right(45)
forward(110)
right(90)
forward(110)
right(135)
forward(26)
left(90)
end_fill()
fillcolor("gray")
begin_fill()
forward(400)
goto(-300,-300)
pencolor("gray")
left(129)
forward(318)
right(39)
forward(251)
right(90)
forward(200)
end_fill()
penup()
goto(-200,-300)
pendown()
pencolor("black")
fillcolor("gray")
begin_fill()
right(180)
forward(400)
right(90)
forward(30)
right(90)
forward(60)
right(90)
forward(160)
right(90)
forward(60)
right(90)
forward(30)
end_fill()
pencolor("black")
forward(100)
right(90)
forward(400)
left(90)
forward(250)
left(90)
fillcolor("gray20")
begin_fill()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
end_fill()
left(90)
forward(350)
penup()
goto(-265,10)
pendown()
fillcolor("black")
begin_fill()
forward(20)
right(90)
forward(60)
right(90)
forward(20)
right(90)
forward(60)
end_fill()
penup()
goto(-265,-200)
pendown()
right(90)
fillcolor("black")
begin_fill()
forward(20)
right(90)
forward(60)
right(90)
forward(20)
right(90)
forward(60)
end_fill()
penup()
goto(-150,-120)
right(90)
fillcolor("black")
begin_fill()
forward(20)
right(90)
forward(60)
right(90)
forward(20)
right(90)
forward(60)
end_fill()
penup()
goto(120,-120)
pendown()
right(90)
fillcolor("black")
begin_fill()
forward(20)
right(90)
forward(60)
right(90)
forward(20)
right(90)
forward(60)
end_fill()
penup()
goto(240,-200)
pendown()
fillcolor("black")
begin_fill()
left(270)
forward(20)
right(90)
forward(60)
right(90)
forward(20)
right(90)
forward(60)
end_fill()
penup()
goto(240,10)
fillcolor("black")
begin_fill()
left(270)
forward(20)
right(90)
forward(60)
right(90)
forward(20)
right(90)
forward(60)
end_fill()
penup()
goto(-200,-300)
pendown()
forward(300)
right(90)
forward(40)
fillcolor("gray")
begin_fill()
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()
left(90)
forward(30)
fillcolor("gray")
begin_fill()
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()
left(90)
forward(30)
fillcolor("gray")
begin_fill()
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()
left(90)
forward(30)
fillcolor("gray")
begin_fill()
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()
left(90)
forward(30)
fillcolor("gray")
begin_fill()
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()
left(90)
forward(30)
end_fill()
fillcolor("gray")
begin_fill()
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()
left(90)
forward(30)
end_fill()
right(90)
penup()
goto(247.5,179.5)
pendown()
right(180)
fillcolor("yellow")
begin_fill()
forward(60)
right(105)
forward(60)
right(150)
forward(62)
end_fill()
penup()
goto(-200,-300)
pendown()
right(105)
forward(400)
left(90)
forward(130)
right(90)
fillcolor("gray")
begin_fill()
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()
left(90)
forward(30)
end_fill()
left(90)
forward(30)
fillcolor("gray")
begin_fill()
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()
right(180)
forward(70)
left(90)
forward(30)
fillcolor("gray")
begin_fill()
right(90)
forward(30)
right(90)
forward(30)
end_fill()
penup()
goto(-200,-300)
right(180)
pendown()
forward(400)
fillcolor("gray")
begin_fill()
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()



#Door circle
penup()
goto(50,-300)
pendown()
pencolor("gray20")
fillcolor("gray20")
begin_fill()
right(180)
forward(90)
circle(50)
end_fill()
penup()
goto(0,-300)
pendown()
pencolor("black")
forward(139)
penup()
goto(200,-300)
pendown()
forward(272.5)
pencolor("gray")
fillcolor("gray")
begin_fill()
width(24)
left(30)
forward(33)
end_fill()
width(2)
pencolor("black")
penup()
goto(200,-300)
pendown()
right(30)
forward(300)
left(90)
forward(30)
penup()
goto(-200,-300)
forward(300)



exitonclick()