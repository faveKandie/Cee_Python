#importing modules
import turtle
from turtle import Turtle, Screen, colormode
import time
import random
import tkinter
from random import randint
import os
import sys
import stat
turtle.colormode(255)

#making another screen
varsc = Screen()

#creating a score board
score = 0
board = Turtle()
board.ht()
        

#writing the main program function
def gamer():
    global lives
    global board
    global score
    global high_score
    sheet = []
    arrays = []
    sheet.append(score)
    score = 0
    board.clear()
    
    board.ht()
    #building essentials
    turtle.colormode(255)
    varscreen = Screen()
    varscreen.bgcolor("black")
    varscreen.title("cee_amOby-Snake-Game!")
    varscreen.setup(1200, 800)
    varscreen.tracer(0)
    varscreen.listen()
    user_bet = varscreen.textinput(title = "WELCOME TO CEE SNAKE GAME RACE!🦋", prompt = "WHAT'S YOUR NAME?: ")
    
    #creating the wall
    wall = Turtle()
    wall.shape("square")
    wall.color("pink")
    wall.ht()
    wall.penup()
    wall.goto(-590, 0)
    wall.pendown()
    wall.pencolor("pink")
    wall.pensize(11)
    wall.setheading(90)
    wall.forward(390)
    wall.setheading(0)
    wall.forward(1170)
    wall.setheading(270)
    wall.forward(770)
    wall.setheading(180)
    wall.forward(1170)
    wall.setheading(90)
    wall.forward(390)
    wall.penup()
    wall.setheading(0)
    wall.forward(100)
    wall.pendown()
    wall.setheading(90)
    wall.forward(280)
    wall.setheading(0)
    wall.forward(100)
    wall.setheading(270)
    wall.forward(100)
    wall.setheading(0)
    wall.forward(150)
    wall.penup()
    wall. forward(100)
    wall.pendown()
    wall.setheading(90)
    wall.forward(100)
    wall.setheading(180)
    wall.forward(80)
    wall.penup()
    wall.setheading(0)
    wall.forward(200)
    wall.pendown()
    wall.forward(400)
    wall.setheading(270)
    wall.forward(80)
    wall.setheading(0)
    wall.forward(70)
    wall.setheading(270)
    wall.penup()
    wall.forward(120)
    wall.setheading(180)
    wall.pendown()
    wall.forward(300)
    wall.setheading(270)
    wall.forward(150)
    wall.setheading(0)
    wall.penup()
    wall.forward(100)
    wall.pendown()
    wall.forward(200)
    wall.setheading(90)
    wall.forward(150)
    wall.penup()
    wall.setheading(270)
    wall.forward(150)
    wall.pendown()
    wall.forward(100)
    wall.setheading(180)
    wall.forward(850)
    wall.penup()
    wall.forward(100)
    wall.pendown()
    wall.forward(90)
    wall.penup()
    wall.setheading(270)
    wall.forward(110)
    wall.setheading(0)
    wall.pendown()
    wall.forward(500)
    wall.penup()
    wall.forward(100)
    wall.setheading(270)
    wall.pendown()
    wall.forward(110)
    wall.setheading(90)
    wall.penup()
    wall.forward(110)
    wall.setheading(0)
    wall.pendown()
    wall.forward(450)
    wall.penup()
    wall.goto(-100, 80)
    wall.pendown()
    wall.setheading(180)
    wall.forward(200)
    wall.setheading(270)
    wall.forward(150)
    wall.setheading(0)
    wall.forward(300)
    wall.setheading(90)
    wall.penup()
    wall.forward(250)
    wall.pendown()
    wall.forward(210)

    #creating lives functionality
    def lives():
        lives_input = varsc.textinput(title = "cee-amoby_snakeGame", prompt = "Do you want to save yourself?: ")

        with open("cee_lives3.t2t", mode = "r") as lives:
            conts = lives.read()
            lives1 = int(conts)
        print(lives1)    

        if lives_input == "yes" or user_input == "YES" and lives1 != 0:
            lives1 -= 1
            with open("cee_lives3.t2t", mode = "w") as lives2:
                lives2.write(f"{lives1}")
            with open("cee_lives3.t2t", mode = "r") as lives3:
                cont2 = lives3.read()
                free = int(cont2)
            print(free)
            segments[0].goto(0, 0)
            segments[0].forward(15)
    

    #creating the snake body
    segments = []
    snakebody = [(0, 0), (-20, 0), (-40, 0)]
    for n in snakebody:
        snakeb = Turtle()
        snakeb.color("white")
        snakeb.shape("square")
        snakeb.shapesize(0.8, 0.8)
        snakeb.penup()
        snakeb.goto(n)
        segments.append(snakeb)

    segments[0].shape("triangle")

    #extending the body of the snake
    def add():
        snakeadd = Turtle()
        snakeadd.color("white")
        snakeadd.shape("square")
        snakeadd.shapesize(0.8, 0.8)
        snakeadd.penup()
        segments.append(snakeadd)
    
    #creating the speed functionality
    speedpick = varscreen.numinput(title = "WELCOME TO CEE SNAKE GAME RACE!🦋", prompt = "Pick a speed between 5, 10 and 15: ")
    
    #creating the food
    color_list = [(95, 158, 160), (100, 149, 237), (176, 196, 222), (147, 112, 219), (255, 192, 203), (255, 218, 185), (255, 105, 180), (176, 224, 230), (135, 206, 250), (255, 20, 147), (221, 160, 221)]
    food = Turtle()
    food.shape("circle")
    food.color(random.choice(color_list))
    food.penup()
    food.shapesize(0.7, 0.7)
    food.speed("fastest")
    
    #creating the user functionality
    def forward():
        if segments[0].heading() != 180:
            segments[0].setheading(0)
    def backward():
        if segments[0].heading() != 0:
            segments[0].setheading(180)
    def sideR():
        if segments[0].heading() != 270:
            segments[0].setheading(90)
    def sideL():
        if segments[0].heading() != 90:
            segments[0].setheading(270)

    #always include the onkey functions before the while loop program so that the turtle listener can pick user functionality
    varscreen.onkey(key = "Right", fun = forward)
    varscreen.onkey(key = "Left", fun = backward)
    varscreen.onkey(key = "Up", fun = sideR)
    varscreen.onkey(key = "Down", fun = sideL)

    #creating the main program
    game = True
    while game:
        varscreen.update()
        time.sleep(speedpick * 0.01)
        #random things
        new_x = randint(-500, 500)
        new_y = randint(-300, 300)
        #creating collision with body function
        for seggy in segments:
            if seggy == segments[0]:
                pass
            elif segments[0].distance(seggy) < 10:
                game = False
                lives()                
        #snake movement 
        for m in range(len(segments) - 1, 0, -1):
            x = segments[m - 1].xcor() 
            y = segments[m - 1].ycor()
            segments[m].goto(x, y)
        #collision with food function
        if segments[0].distance(food) < 20:
            add()
            food.color(random.choice(color_list))
            food.goto(new_x, new_y)
            score += 1
            board.penup()
            board.goto(450, 300)
            board.color("white")
            board.clear()
            board.write(f"{score}", align = "center", font = ("Comic Sans MS", 22, "bold"))
        #creating collision with walls function, the code below acts as the boundaries.
        if segments[0].xcor() > 570 or segments[0].xcor() < -570 or segments[0].ycor() > 370 or segments[0].ycor() < -370:
            game = False
        if segments[0].xcor() <= -470 and segments[0].xcor() >= -480 and segments[0].ycor() >= 10 and segments[0].ycor() <= 280:
            game = False
        if segments[0].xcor() >= -470 and segments[0].xcor() <= -370 and segments[0].ycor() >= 280 and segments[0].ycor() <= 290:
            game = False
        if segments[0].xcor() <= -370 and segments[0].xcor() >= -380 and segments[0].ycor() >= 180 and segments[0].ycor() <= 280:
            game = False
        if segments[0].xcor() >= -370 and segments[0].xcor() <= -220 and segments[0].ycor() >= 170 and segments[0].ycor() <= 180:
            game = False
        if segments[0].xcor() <= -130 and segments[0].xcor() >= -140 and segments[0].ycor() >= 180 and segments[0].ycor() <= 280:
            game = False
        if segments[0].xcor() >= -210 and segments[0].xcor() <= -110 and segments[0].ycor() >= 280 and segments[0].ycor() <= 290:
            game = False
        if segments[0].xcor() <= 0 and segments[0].xcor() >= -10 and segments[0].ycor() >= 180 and segments[0].ycor() <= 390:
            game = False
        if segments[0].xcor() >= 0 and segments[0].xcor() <= 400 and segments[0].ycor() >= 280 and segments[0].ycor() <= 290:
            game = False
        if segments[0].xcor() <= 380 and segments[0].xcor() >= 370 and segments[0].ycor() >= 210 and segments[0].ycor() <= 290:
            game = False
        if segments[0].xcor() >= 400 and segments[0].xcor() <= 460 and segments[0].ycor() >= 200 and segments[0].ycor() <= 210:
            game = False
        if segments[0].xcor() <= 460 and segments[0].xcor() >= 170 and segments[0].ycor() >= 80 and segments[0].ycor() <= 90:
            game = False
        if segments[0].xcor() >= 150 and segments[0].xcor() <= 160 and segments[0].ycor() >= -70 and segments[0].ycor() <= 80:
            game = False
        if segments[0].xcor() <= 460 and segments[0].xcor() >= 270 and segments[0].ycor() >= -70 and segments[0].ycor() <= -60:
            game = False
        if segments[0].xcor() >= 450 and segments[0].xcor() <= 460 and segments[0].ycor() >= -170 and segments[0].ycor() <= 80:
            game = False
        if segments[0].xcor() <= 460 and segments[0].xcor() >= -380 and segments[0].ycor() >= -170 and segments[0].ycor() <= -150:
            game = False
        if segments[0].xcor() >= -590 and segments[0].xcor() <= -480 and segments[0].ycor() >= -170 and segments[0].ycor() <= -150:
            game = False
        if segments[0].xcor() <= -70 and segments[0].xcor() >= -590 and segments[0].ycor() >= -280 and segments[0].ycor() <= -270:
            game = False
        if segments[0].xcor() >= 20 and segments[0].xcor() <= 460 and segments[0].ycor() >= -280 and segments[0].ycor() <= -270:
            game = False
        if segments[0].xcor() <= 20 and segments[0].xcor() >= 10 and segments[0].ycor() >= -390 and segments[0].ycor() <= -280:
            game = False
        if segments[0].xcor() >= -300 and segments[0].xcor() <= 0 and segments[0].ycor() >= -70 and segments[0].ycor() <= -60:
            game = False
        if segments[0].xcor() <= -100 and segments[0].xcor() >= -300 and segments[0].ycor() >= 70 and segments[0].ycor() <= 80:
            game = False
        if segments[0].xcor() >= -300 and segments[0].xcor() <= -290 and segments[0].ycor() >= -70 and segments[0].ycor() <= 80:
            game = False
        new_score = score
        segments[0].forward(15)    
    varscreen.clear()
    varscreen.bgcolor("black")
    board.penup()
    board.goto(-10, 0)
    board.color("pink")
    board.write(f"Game Over {user_bet} ...\n Your Score is {score}", align = "center", font = ("Comic Sans MS", 35, "bold"))

    #saving each new score to  cee_amoby_snakegame_scoresheet .txt file(t2t file) separated by a comma
    with open("cee_amoby_snakegame_scoresheet.t2t", mode = "a") as file1:
        file1.write(f", {new_score}")
    
    #reading the content of the saved file in the .t2t file
    with open("cee_amoby_snakegame_scoresheet.t2t", mode = "r") as file1:
        contents = file1.read()
    #adding the read contents to an empty array so it will look like an inputed array separated by a comma
    arrays.append(contents)    
    
    #applying the split function to separate the contents of the read .txt file which i set to be separated by a comma
    split_score = contents.split(", ")
    
    #looping through the split contents and saving them each as a separate number in the array  
    for n in range(0, (len(split_score))):
        split_score[n] = int(split_score[n])
    
    #looping through contents of the array holding every updated score being played to get high score
    highest = 0
    for r in split_score:
        if r > highest:
            highest = r  #at this point, highest is no longer 0, everytime
            board.goto(-90, -100)
    
    board.write(f"Highest score is {highest}", align = "center", font = ("Comic Sans MS", 20, "bold"))
    #to tell the user if they've made a new high score
    if score >= highest:
        board.goto(-50, -170)
        board.write("New High score!", align = "center", font = ("Comic Sans MS", 30, "bold"))
               

#calling the function
gamer()
            
#runs whenever the main program function has completed
result = True
while result:
    user_input = varsc.textinput(title = "WELCOME TO CEE SNAKE GAME RACE!🦋", prompt = "Do you want to retry? YES or No: ")
    if user_input == "yes" or user_input == "YES":
        gamer()
    elif user_input == "no" or user_input == "NO":
        result = False
        break

#to keep the turtle screen open until it is touched
varscreen.exitonclick()
varsc.exitonclick()