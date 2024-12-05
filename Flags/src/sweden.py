#Drawing flags usiong Python Turtle - www.101computing.net/drawing-flags-using-python-turtle
import turtle
x=input("Press Enter to start")
myPen = turtle.Turtle()
myPen.shape("arrow")
# myPen.speed(10)

window = turtle.Screen()
window.bgcolor("#DDDDDD")

#Position the pen in the bottom left corner
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()

#Draw the frame for the flag
myPen.color("#307DC1")
myPen.pensize(2)
myPen.fillcolor("#307DC1")
#Position the pen in the bottom left corner
myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()
myPen.begin_fill()
myPen.goto(180,-120)
myPen.goto(180,120)
myPen.goto(-180,120)
myPen.goto(-180, -120)
myPen.end_fill()  

#Draw the yellow horizontal stripe
myPen.color("#FFD900")
myPen.pensize(2)
myPen.fillcolor("#FFD900")

myPen.penup()
myPen.goto(-180, -20)
myPen.pendown()
myPen.begin_fill()
myPen.goto(180, -20)
myPen.goto(180, 20)
myPen.goto(-180, 20)
myPen.goto(-180, -20)
myPen.end_fill()  

#Draw the yellow vertical stripe
myPen.penup()
myPen.goto(-80, -120)
myPen.pendown()
myPen.begin_fill()
myPen.goto(-40, -120)
myPen.goto(-40, 120)
myPen.goto(-80, 120)
myPen.goto(-80, -120)
myPen.end_fill()  


myPen.color("white")
myPen.goto(-180, -120)

def draw_pole():
    myPen.pendown()
    myPen.pensize(10)
    myPen.pencolor("black")
    myPen.setheading(90)
    myPen.fd(300)
    myPen.setheading(-90)
    myPen.fd(600)
    myPen.ht()

draw_pole()
myPen.hideturtle()

x=input("Press Enter to close")