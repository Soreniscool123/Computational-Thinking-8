# Setup
import turtle
t = turtle.Turtle()
t.color("red")
t.speed(40)
t.penup()
t.goto(-350, 230)
t.pendown()

# Row 1
for i in range(13):
    for i in range(4):
        t.forward(40)
        t.left(90)
    t.penup()
    t.forward(55)
    t.pendown()

# Setup 2
    t2 = turtle.Turtle()
t2.color("orange")
t2.speed(40)
t2.penup()
t2.goto(-350, 179)
t2.pendown()

# Row 2
for i in range(13):
    for i in range(4):
        t2.forward(40)
        t2.left(90)
    t2.penup()
    t2.forward(55)
    t2.pendown()


# Setup 3
    t3 = turtle.Turtle()
t3.color("yellow")
t3.speed(40)
t3.penup()
t3.goto(-350, 128)
t3.pendown()

# Row 3
for i in range(13):
    for i in range(4):
        t3.forward(40)
        t3.left(90)
    t3.penup()
    t3.forward(55)
    t3.pendown()


# Setup 4
    t4 = turtle.Turtle()
t4.color("lime")
t4.speed(40)
t4.penup()
t4.goto(-350, 77)
t4.pendown()

# Row 4
for i in range(13):
    for i in range(4):
        t4.forward(40)
        t4.left(90)
    t4.penup()
    t4.forward(55)
    t4.pendown()


# Setup 5
    t5 = turtle.Turtle()
t5.color("green")
t5.speed(40)
t5.penup()
t5.goto(-350, 26)
t5.pendown()

# Row 5
for i in range(13):
    for i in range(4):
        t5.forward(40)
        t5.left(90)
    t5.penup()
    t5.forward(55)
    t5.pendown()


# Setup 6
    t6 = turtle.Turtle()
t6.color("blue")
t6.speed(40)
t6.penup()
t6.goto(-350, -25)
t6.pendown()

# Row 6
for i in range(13):
    for i in range(4):
        t6.forward(40)
        t6.left(90)
    t6.penup()
    t6.forward(55)
    t6.pendown()

# End
turtle.exitonclick()