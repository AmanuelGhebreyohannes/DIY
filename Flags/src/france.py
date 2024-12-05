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
  
#Draw the blue stripe
myPen.color("blue")
myPen.pensize(2)
myPen.fillcolor("blue")

myPen.penup()
myPen.goto(-180, -120)
myPen.pendown()
myPen.begin_fill()
myPen.goto(-60,-120)
myPen.goto(-60,120)
myPen.goto(-180,120)
myPen.goto(-180, -120)
myPen.end_fill()  

#Draw the red stripe
myPen.color("red")
myPen.pensize(2)
myPen.fillcolor("red")

myPen.penup()
myPen.goto(60, -120)
myPen.pendown()
myPen.begin_fill()
myPen.goto(180,-120)
myPen.goto(180,120)
myPen.goto(60,120)
myPen.goto(60, -120)
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


# #Adding Text...
# myPen.penup()
# myPen.goto(-62, -160)
# myPen.color("white")
# myPen.write("FRANCE", align="center", font=("Arial", 24, "bold"))

draw_pole()

myPen.hideturtle()

x=input("Press Enter to close")

