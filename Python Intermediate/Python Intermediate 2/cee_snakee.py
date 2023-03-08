from turtle import Turtle, Screen, colormode
import time

var = Screen()
var.title("cee Snake")
var.bgcolor("black")
var.setup(width = 600, height = 600)

#creating the snake parts
snake_part = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for n in snake_part:
    new_part = Turtle("square")
    new_part.color("white")
    new_part.goto(n)
    segments.append(new_part)
    

#creating the user's operation of the snake
root = segments[0]

def forward():
    root.forward(100)
    
#creating the onscreen partition
var.onkey(forward, "space")

var.exitonclick()