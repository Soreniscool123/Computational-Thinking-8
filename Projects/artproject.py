# Setup
import turtle
turtle.Screen().bgcolor("black")
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


# Setup 7
    t7 = turtle.Turtle()
t7.color("purple")
t7.speed(40)
t7.penup()
t7.goto(-350, -76)
t7.pendown()

# Row 7
for i in range(13):
    for i in range(4):
        t7.forward(40)
        t7.left(90)
    t7.penup()
    t7.forward(55)
    t7.pendown()

# Setup 8
    t8 = turtle.Turtle()
t8.color("maroon")
t8.speed(40)
t8.penup()
t8.goto(-350, -127)
t8.pendown()

# Row 8
for i in range(13):
    for i in range(4):
        t8.forward(40)
        t8.left(90)
    t8.penup()
    t8.forward(55)
    t8.pendown()

    # Setup 9
    t9 = turtle.Turtle()
t9.color("brown")
t9.speed(40)
t9.penup()
t9.goto(-350, -178)
t9.pendown()

# Row 9
for i in range(13):
    for i in range(4):
        t9.forward(40)
        t9.left(90)
    t9.penup()
    t9.forward(55)
    t9.pendown()

    # Setup 10
    t10 = turtle.Turtle()
t10.color("red")
t10.speed(40)
t10.penup()
t10.goto(-350, -229)
t10.pendown()

# Row 10
for i in range(13):
    for i in range(4):
        t10.forward(40)
        t10.left(90)
    t10.penup()
    t10.forward(55)
    t10.pendown()

# Setup 11
    t11 = turtle.Turtle()
t11.color("orange")
t11.speed(40)
t11.penup()
t11.goto(-350, -280)
t11.pendown()

# Row 11
for i in range(13):
    for i in range(4):
        t11.forward(40)
        t11.left(90)
    t11.penup()
    t11.forward(55)
    t11.pendown()

    # Setup 12 white
    t12 = turtle.Turtle()
t12.color("white")
t12.speed(40)
t12.penup()
t12.goto(-340, 250)
t12.pendown()

# Row 12 white
for i in range (11):
    t12.pendown()
    for i in range(13):
        for i in range(4):
            t12.forward(10)
            t12.left(90)
        t12.penup()
        t12.forward(55)
        t12.pendown()
    t12.penup()
    t12.setheading(270)
    t12.forward(102)
    t12.setheading(180)
    t12.forward(713)
    t12.setheading(0)
    t12.penup()
    

# End
turtle.exitonclick()