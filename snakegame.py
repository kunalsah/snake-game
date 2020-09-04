
import turtle
import time
import random

delay = 0.1

#Score
Score = 0
High_Score = 0

#set up the screen
wn=turtle.Screen()
wn.title("snake game")
wn.bgcolor("green")
wn.setup(width=700,height=700)
wn.tracer(0)

#creating the border
b=turtle.Turtle()
b.penup()
b.goto(-310,310)
b.pendown()
b.pensize(3)
b.pencolor("white")
for i in range (4):
	b.fd(620)
	b.rt(90)

b.penup()
b.goto(-240,255)
b.pendown()
b.fd(470)
b.hideturtle()


# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("red")
food.penup()
food.goto(0,100)

segments =[]

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier",24,"bold"))

#Functions
def go_up():
	if head.direction != "down":
		head.direction ="up"

def go_down():

	if head.direction != "up":
		head.direction ="down"

def go_left():

	if head.direction != "right":
		head.direction ="left"

def go_right():

	if head.direction != "left":
		head.direction ="right"

def move():
	if head.direction =="up":
		y = head.ycor()
		head.sety(y+20)

	if head.direction =="down":
		y = head.ycor()
		head.sety(y-20)

	if head.direction =="left":
		x = head.xcor()
		head.setx(x-20)

	if head.direction =="right":
		x = head.xcor()
		head.setx(x+20)
# keyboard bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left ")
wn.onkeypress(go_right,"Right")

#Main game loop
while True:
	wn.update()

	# check for a collision with the border
	if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 235 or head.ycor()< - 290:
		time.sleep(1)
		head.goto(0,0)
		head.direction = "stop"

		# hide the segments
		for segment in segments:
			segment.goto(1000,1000)

		# clear the segments list
		segments.clear()

		#reset the Score
		Score = 0

		#reset the delay
		delay = 0.1
		
		#update the Score display

		pen.clear()
		pen.write("Score: {} High Score: {}".format(Score, High_Score), align="center", font=("Courier",24,"bold"))

	# check for a collision with the food
	if head.distance(food) < 20:
		# move the food to the random position
		x = random.randint(-290,290)
		y = random.randint(-290,235)
		food.goto(x,y)

		# add a segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape('square')
		new_segment.color('grey')
		new_segment.penup()
		segments.append(new_segment)

		#shorten the delay
		delay -= 0.001

		#increase the Score
		Score += 10

		if Score > High_Score:
			High_Score = Score
		pen.clear()
		pen.write("Score: {} High Score: {}".format(Score, High_Score), align="center", font=("Courier",24,"bold"))

	# move the end segements first in reverse order
	for index in range(len(segments)-1,0,-1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x,y)

	#move segment 0 to where the head is
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x,y)

	move()
	# check for head collision with the body
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0,0)
			head.direction = "stop"

			# hide the segments
			for segment in segments:
				segment.goto(1000,1000)

			# clear the segments list
			segments.clear()

			#reset the Score
			Score = 0

			#reset the delay
			delay = 0.1	

			#update the Score display
			
			pen.clear()
			pen.write("Score: {} High Score: {}".format(Score, High_Score), align="center", font=("Courier",24,"bold"))
		
	time.sleep(delay)

wn.mainloop()