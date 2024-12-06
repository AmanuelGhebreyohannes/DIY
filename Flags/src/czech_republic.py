#Drawing flags usiong Python Turtle - www.101computing.net/drawing-flags-using-python-turtle
import turtle

x=input("Press Enter to start")
myPen = turtle.Turtle()
myPen.shape("arrow")
# myPen.speed(10)

window = turtle.Screen()
window.bgcolor("#DDDDDD")

#Draw the frame for the flag
myPen.color("white")
myPen.pensize(2)
myPen.fillcolor("white")
myPen.begin_fill()
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
  
#Draw the red horizontal stripe
myPen.color("#CC2222")
myPen.pensize(2)
myPen.fillcolor("#CC2222")

myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()
myPen.begin_fill()
myPen.goto(180, -120)
myPen.goto(180, 0)
myPen.goto(-180, 0)
myPen.goto(-180, -120)
myPen.end_fill()  

#Draw the blue triangle
myPen.color("#2222BB")
myPen.pensize(2)
myPen.fillcolor("#2222BB")

myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()
myPen.begin_fill()
myPen.goto(0,0)
myPen.goto(-180,120)
myPen.goto(-180,-120)
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
