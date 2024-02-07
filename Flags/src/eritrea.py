import turtle

#turtle.speed(10)
turtle.fd(0)
x=input("Press Enter to start")
yellow_pos=(110,55)

def draw_blue():
	turtle.color("blue")
	turtle.begin_fill()
	turtle.fd(500)
	turtle.left(90)
	turtle.fd(125)
	turtle.setpos(0,0)
	turtle.end_fill()

def draw_red():
	turtle.color("red")
	turtle.begin_fill()
	turtle.fd(250)
	turtle.setpos(500,125)
	turtle.setpos(0,0)
	turtle.end_fill()

def draw_green():
	turtle.setpos(0,250)
	turtle.color("green")
	turtle.begin_fill()
	turtle.right(90)
	turtle.fd(500)
	turtle.right(90)
	turtle.fd(125)
	turtle.setpos(0,250)
	turtle.end_fill()


def draw_yellow_down():
	turtle.color("red")
	turtle.setpos(110,55)
	yellow_pos=turtle.pos()
	turtle.color("yellow")
	turtle.begin_fill()
	turtle.setheading(0)
	turtle.right(15)
	turtle.fd(45)
	turtle.setheading(180)
	turtle.fd(80)
	turtle.setpos(yellow_pos)
	turtle.end_fill()



def draw_yellow_right():
	list2=turtle.pos()
	angle=0
	i=20
	j=0
	turtle.setheading(0)
	while(j<8):
		
		list=list2
		turtle.setheading(angle)
		turtle.setpos(list)
		turtle.begin_fill()
		turtle.circle(98,30)
		turtle.setheading(190+angle)
		turtle.fd(i)
		i+=3
		list2=turtle.pos()
		turtle.setpos(list)
		angle+=17
		turtle.end_fill()
		j+=1
		

def draw_yellow_left():
	angle=0
	turtle.color("red")
	turtle.setpos(yellow_pos)
	turtle.color("yellow")
	list2=turtle.pos()
	i=20
	j=0
	while(j<8):
		list=list2
		turtle.setheading(180-angle)
		turtle.setpos(list)
		turtle.begin_fill()
		turtle.circle(-98,30)
		turtle.setheading(-10-angle)
		turtle.fd(i)
		i+=3
		list2=turtle.pos()
		turtle.setpos(list)
		angle+=17
		turtle.end_fill()
		j+=1


def draw_yellow_middle():
	turtle.color("red")
	turtle.setpos(yellow_pos)
	turtle.color("yellow")
	turtle.setheading(90)
	j=0
	turtle.pensize(3)
	while(j<6):
		turtle.setheading(90)
		turtle.fd(15)
		list=turtle.pos()
		turtle.begin_fill()
		if(j%2==0):
			turtle.setheading(0)
			turtle.circle(35,90)
			turtle.setheading(190)
			turtle.fd(15)
			turtle.setpos(list)
		else:
			turtle.setheading(180)
			turtle.circle(-35,90)
			turtle.setheading(-10)
			turtle.fd(15)
			turtle.setpos(list)
		turtle.end_fill()
		j+=1

def draw_pole():
	turtle.penup()
	turtle.home()
	turtle.pendown()
	turtle.pensize(10)
	turtle.pencolor("black")
	turtle.setheading(90)
	turtle.fd(300)
	turtle.setheading(-90)
	turtle.fd(600)
	turtle.ht()

draw_blue()
draw_red()
draw_green()
draw_yellow_down()	
draw_yellow_right()
draw_yellow_left()
draw_yellow_middle()
draw_pole()


x=input("Press Enter to close")