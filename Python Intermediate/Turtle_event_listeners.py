import turtle
from turtle import Turtle, Screen, colormode
turtle.colormode(255)

import random
var = Turtle()#accessingthe Turtle class
screen = Screen()#accessing the Screen class
var.shape("turtle")
var.color("deep pink")
var.speed("fastest")

screen.listen()#accessing the screen methods

color_list = [(95, 158, 160), (100, 149, 237), (176, 196, 222), (147, 112, 219), (255, 192, 203), (255, 218, 185), (255, 105, 180), (176, 224, 230), (135, 206, 250), (255, 20, 147), (221, 160, 221)]
def penu():
	var.penup()
def pend():
	var.pendown()
def forward():
	var.forward(70)
def backward():
	var.backward(70)
def right():
	var.right(30)
def left():
	var.left(30)
def undoo():
	var.undo()
def clear():
	var.reset()
	var.color(random.choice(color_list))

screen.onkey(key = "space", fun = forward)
screen.onkey(key = "Up", fun = backward)
screen.onkey(key = "Right", fun = right)
screen.onkey(key = "Left", fun = left)
screen.onkey(key = "Down", fun = penu)
screen.onkey(key = "a", fun = pend)
screen.onkey(key = "b", fun = undoo)
screen.onkey(key = "c", fun = clear)

screen.exitonclick()