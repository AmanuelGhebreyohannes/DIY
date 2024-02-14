import turtle

# Setup the screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.title("Kuwait Flag Drawing")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set maximum speed

# Function to draw a rectangle with given color
def draw_rectangle(color, width, height):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
        t.forward(width)
    t.end_fill()

# Function to draw the flagpole
def draw_flagpole(height):
    t.color("black")
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(20)
    t.end_fill()

# Draw the flag
flag_width = 300
flag_height = 200
draw_rectangle("green", flag_width, flag_height/3)  # Green stripe
t.right(180)
# t.forward(flag_width)
draw_rectangle("white", flag_width, flag_height/3)  # White stripe
t.right(180)
# t.forward(flag_width)
draw_rectangle("red", flag_width, flag_height/3)  # Red stripe

# Position the turtle for drawing the flagpole
t.penup()
t.goto(-10, -200)  # Adjusted position for the flagpole
t.pendown()

# Draw the flagpole
flagpole_height = 300
draw_flagpole(flagpole_height)

# Hide turtle and display the flag
t.hideturtle()
turtle.done()
