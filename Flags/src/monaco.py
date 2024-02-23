import turtle

width=600
height=600
# Setup the screen
screen = turtle.Screen()
screen.setup(width, height)
screen.title("Kuwait Flag Drawing")

# Create a turtle object
t = turtle.Turtle()
# t.speed(0)  # Set maximum speed
x=input("Press Enter to start")

# Function to draw a pole with given color
def draw_pole(color):
    t.color(color)
    t.penup()
    x1,y1 = (-width/2+50),(height/2-50)
    x2,y2 = (-width/2+30),(height/2-50)
    x3,y3 = (-width/2+30),(-height+50)
    x4,y4 = (-width/2+50),(-height+50)
    t.goto(x1,y1)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.goto(x4,y4)
    t.end_fill()
    t.penup()

def draw_green(color):
    t.color(color)
    t.penup()
    x1,y1 = (-width/2+50),(height/2-50)
    x2,y2 =(-width/2+450),(height/2-50)
    x3,y3 = (-width/2+450),(height/2-200)
    x4,y4 = (-width/2+150),(height/2-200)
    x5,y5 = (-width/2+50),(height/2-50)
    t.goto(x1,y1)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.goto(x4,y4)
    t.goto(x5,y5)
    t.goto(x4,y4)
    t.end_fill()
    t.penup()

def draw_white(color):
    t.color(color)
    t.penup()
    x1,y1 = (-width/2+150),(height/2-200)
    x2,y2 =(-width/2+450),(height/2-200)
    x3,y3 = (-width/2+450),(height/2-300)
    x4,y4 = (-width/2+150),(height/2-300)
    t.goto(x1,y1)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.goto(x4,y4)
    t.goto(x1,y1)
    t.end_fill()
    t.penup()

def draw_black(color):
    t.color(color)
    t.penup()
    x1,y1 = (-width/2+50),(height/2-50)
    x2,y2 = (-width/2+150),(height/2-200)
    x3,y3 = (-width/2+150),(height/2-300)
    x4,y4 = (-width/2+50),(height/2-450)
    t.goto(x1,y1)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.goto(x4,y4)
    t.goto(x1,y1)
    t.end_fill()
    t.penup()

def draw_red(color):
    t.color(color)
    t.penup()
    x1,y1 = (-width/2+150),(height/2-300)
    x2,y2 = (-width/2+450),(height/2-300)
    x3,y3 = (-width/2+450),(height/2-450)
    x4,y4 = (-width/2+50),(height/2-450)
    t.goto(x1,y1)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.goto(x4,y4)
    t.goto(x1,y1)
    t.end_fill()
    t.penup()

draw_pole("brown")  # pole
draw_green("green")
draw_white("white")
draw_black("black")
draw_red("red")


# Hide turtle and display the flag
t.hideturtle()
turtle.done()
