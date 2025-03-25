import turtle


aken = turtle.Screen()
aken.bgcolor("black")
turtle.showturtle()
turtle.shape("turtle")
turtle.pensize(3)
turtle.pencolor("MediumSlateBlue")


for i in range(5):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.right(72)
    turtle.forward(-50)
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
        


turtle.done()