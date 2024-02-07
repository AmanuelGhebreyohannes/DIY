import turtle

# Set up the turtle
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")
screen.title("Monaco Flag Drawing")

# Create a turtle object
t = turtle.Turtle()
# t.speed(0)  # Set maximum speed
x=input("Press Enter to start")

# Define function to draw rectangle with border
def draw_rectangle_with_border(fill_color, border_color, width, height):
    t.color(border_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Draw the pole
pole_height = 750  # Adjusted height for the pole
t.penup()
t.goto(-310, 200)  # Adjusted position for the pole
t.pendown()
draw_rectangle_with_border("#666666", "black", 10, pole_height)  # Gray color for the pole

# Draw the red rectangle (flag)
t.penup()
t.goto(-300, 200)
t.pendown()
draw_rectangle_with_border("#FF0000", "black", 600, 200)

# Draw the white rectangle (flag)
t.penup()
t.goto(-300, 0)
t.pendown()
draw_rectangle_with_border("white", "black", 600, 200)

# Hide turtle and display the flag
t.hideturtle()
turtle.done()
