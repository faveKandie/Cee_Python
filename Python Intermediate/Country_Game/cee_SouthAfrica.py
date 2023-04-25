#This is the main program for south african country game
import pandas
import random
import turtle
import time

rate = turtle.Screen()
rate.title("south_africa_")
rate.setup(800, 710)


 #add shape to the variable defined screen
#turtle.shape(southafrica_img) should be found in the folder
southafrica_img = "southafrica.gif"
rate.addshape(southafrica_img)
turtle.shape(southafrica_img)

rate.tracer(100)
#to get the co-ordinates of points we click
def get_mouseOn_click(x, y):
    print(x, y)


#accessing pandas file
doc = pandas.read_csv("SA9_states.csv")
#converting the states column in the csv file to a list
states = doc["states"] .to_list()
 
#Empty list to store names of states we have already guessed
guessed_state = []

#creating some necessary turtle- score, time, and state writing
scoree = turtle.Turtle()
scoree.ht()
locate = turtle.Turtle()
locate.ht()
timer = turtle.Turtle()
timer.ht()

#a function of predefined process required for those turtle writing
def location(fund, x, y):
    fund.ht()
    fund.penup()
    fund.goto(x, y)
    fund.pendown()

#creating the time variable
timee = 30
location(timer, 330, -330)
timer.clear()
timer.write(f"00:{timee}", align = "center", font = ("ComicSans MS", 20, "bold"))

#aesthetic turtles
border = turtle.Turtle()
border.ht()
location(border, 330, -270)
scorer = turtle.Turtle()
scorer.ht()
location(scorer, -300, 320)
def brorder(funder, x, y):
    funder.pensize(6)
    funder.pencolor("black")
    funder.setheading(0)
    funder.forward(100)
    funder.setheading(270)
    funder.forward(40)
    funder.setheading(180)
    funder.forward(100)
    funder.setheading(90)
    funder.forward(40)
    funder.penup()
    funder.goto(x, y)
    funder.pendown()

location(border, 280, -290)
brorder(border, 330, -290)
border.write("TIME", align = "center", font  = ("ComicSans MS", 20, "bold"))
location(scorer, -390, 320)
brorder(scorer, -340, 320)
scorer.write("SCORE", align = "center", font  = ("ComicSans MS", 15, "bold"))
location(scoree, -340, 280)

#asking the question
state_text = rate.textinput(title = "Name: ", prompt = "What's your name: ").title()        

#declaring the score variable
score = 0  

#this function is basically for the timer function
#here, i used the ontimer function to make the time in seconds actually work  
#1. first requirement for the ontimer function  
repeat = True 
#2. the function we will run inside the turtle ontimer
def run(): 
    #3. Declare the global variables to be used inside here
    global timee
    global score
    global state_text
    #4. since it's basically for the time running, here goes it
    if timee > 0 and state_text != "Exit":
        timee -= 1
        moder = timee % 60
        timer.clear()
        if moder >= 10:
            timer.write(f"00:{moder}", align = "center", font = ("ComicSans MS", 20, "bold"))
        elif moder < 10:
            timer.write(f"00:0{moder}", align = "center", font = ("ComicSans MS", 20, "bold"))
        #5. so below, as long as the time is not at 0seconds, every 1800 miliseconds, approximately 1 second, the time is reduced by  1. Because it runs this main function inside the turtle timer
        rate.ontimer(fun= run, t = 1000)
    #6. When the time hits at 0 seconds
    elif timee == 0:
        #7. declaring an empty list to to hold names of states not guessed before the time runs out if there's any
        rare = []
        for m in range(0, 9):
            if states[m] not in guessed_state:
                rare.append(states[m]) #at this point, rare holds unguessed state
        for m in rare: #accessing the unguessed state
            time.sleep(1) #every 1 second, it write them on their position in the map
            randname = doc[doc.states == m]  #to access the cordinates of those unguessed state from the main csv file
            locate.ht()
            locate.penup()
            locate.goto(int(randname["x"]), int(randname["y"]))
            locate.pendown()
            locate.color("white")
            locate.write(f"{m}", align = "center", font = ("Comic Sans MS", 10, "bold"))
        time.sleep(2)
        rate.clear()
        rate.bgcolor("black")
        locate.penup()
        locate.goto(0,0)
        locate.pendown()
        locate.write(f"Game Over\nYour score is {score}", align = "center", font = ("Comic Sans MS", 20, "bold"))
    elif state_text == "Exit" or score == 9:
        pass
        #the line of code above ignores all those conditions if the user inputs exit or has finished before the time runs out

#running the time function above        
run()
#remember that we declared repeat = True, now we declare repeat = False as it is the last requirement for the turtle ontimer function
repeat = False

#the main game program for the states
while len(guessed_state) != 10:
    #to stop producing the question bar
    if timee < 2:
        break
    #the question bar
    state_text = rate.textinput(title = "SA_State", prompt = "Mention another state: ").title()
    #if the user opts out of the game
    if state_text == "Exit":
        rare = []  #holding names of states not gotten/guessed
        for m in range(9):
            if states[m] not in guessed_state:
                rare.append(states[m])
        for m in rare:
            time.sleep(1)  #every 1 second, the computer autofills it
            randname = doc[doc.states == m]  #the states x and y
            locate.ht()
            locate.penup()
            locate.goto(int(randame["x"], int(randname["y"])))
            locate.pendown()
            locate.color("white")
            locate.write(f"{m}", align = "center", font = ("Comic Sans MS", 10, "bold"))
        rate.clear()
        rate.bgcolor("black")
        locate.penup()
        locate.goto(0,0)
        locate.pendown()
        locate.write(f"Game Over\nYour score is {score}", align = "center", font = ("Comic Sans MS", 20, "bold"))
        break  #to leave the loop
    #the lines of code below is for when the user keeps guessing 
    if state_text in states and state_text not in guessed_state:
        guessed_state.append(state_text)
        statesy = doc[doc.states == state_text]
        locate.penup()
        locate.goto(int(statesy["x"]), int(statesy["y"]))
        locate.pendown()
        locate.write(f"{state_text}", align = "center", font = ("ComicSans Ms", 10, "bold")) 
        score += 1
        scoree.clear()
        scoree.write(f"{score}/9", align = "center", font = ("ComicSans MS", 20, "bold"))
    #the lines of code below is for when the user has guessed all before the time is over
    if score == 9:
        rate.clear()
        rate.bgcolor("black")
        locate.penup()
        locate.goto(0,0)
        locate.pendown()
        locate.color("white")
        locate.write(f"Game Over\nYou WIN!\nYour score is {score}", align = "center", font = ("Comic Sans MS", 20, "bold"))
        break  #to leave the while loop since we were not using a true and false condition here

#the lines of code below is to prevent the turtle screen from closing when the user is still in the game        
rate.onscreenclick(get_mouseOn_click)
rate.mainloop()