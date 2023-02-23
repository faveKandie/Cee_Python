import turtle
from turtle import Turtle, Screen, colormode
turtle.colormode(255)
import random
var = Turtle()
screen = Screen()
screen.setup(width = 700, height = 700)

race_on = True
user_bet = screen.textinput(title = "MAKE YOUR BET!🦋", prompt = "Which turtle will win the race? Pick a colour: ")
all_turtle = []
speed = [1, 2, 3, 4, 5]
num = [0, 1, 2, 3, 4]

def start(get):
	color_list = ["pink", "red", "blue", "green", "orange"]
	get.color("white")
	for n in range(5):
		get = Turtle()
		get.shape("turtle")
		get.penup()
		get.color(color_list[n])
		get.setheading(270)
		get.forward(n * 70)
		get.setheading(0)
		get.backward(300)
		all_turtle.append(get)

	if user_bet:
		race_on = False

	while not race_on:
		for turt in all_turtle:
			if turt.xcor() > 330:
				race_on = True
				winning_color = turt.pencolor()
				if winning_color == user_bet:
					print(f"You've won. The {winning_color} turtle is the winner")
				else:
					print(f"You've lost. The {winning_color} turtle is the winner")
			road = 1 * (random.choice(speed))
			all_turtle[random.choice(num)].forward(road)
start(var)
