import turtle

from turtle import Turtle, Screen
timmy = Turtle()
my_screen = Screen()

timmy.shape("turtle")
timmy.color("black", "DeepPink")
timmy.forward(100)
print(timmy)

print("heyyyy")
print(my_screen.canvheight)#here, the object is accessing the attribute 
my_screen.exitonclick()

import prettytable

from prettytable import PrettyTable
x = PrettyTable()
print(x)