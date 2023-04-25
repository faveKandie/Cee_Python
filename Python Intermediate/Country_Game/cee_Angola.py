#This is the main program for cee Angola game
import turtle
import time
import pandas

#accessing the states csv file
rate = turtle.Screen()
rate.title("cee_Angola")

doc = pandas.read_csv("Angola.csv")
listdoc = doc["states"].to_list()

Angola_img = "Angolaa.gif"
rate.addshape(Angola_img)
rate.setup(800, 710)
turtle.shape(Angola_img)
rate.tracer(100)

Time  = 70
score = 0

#to get the co-ordinates of points we click
def get_mouseOn_click(x, y):
    print(x, y)

def repeat(fund, x, y):
    fund.ht()
    fund.penup()
    fund.goto(x, y)
    fund.pendown()

#required writing turtles
timer = turtle.Turtle()
timer.ht()
rounder = turtle.Turtle()
rounder.ht()
scorer = turtle.Turtle()
scorer.ht()
scoree = turtle.Turtle()
scoree.ht()
writer = turtle.Turtle()
writer.ht()

def border(funder, x, y):
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

repeat(scoree, -340, 280)     
repeat(rounder, 280, -290)
border(rounder, 330, -290)
rounder.write("TIME", align = "center", font  = ("ComicSans MS", 20, "bold"))
repeat(scorer, -390, 320)
border(scorer, -340, 320)
scorer.write("SCORE", align = "center", font  = ("ComicSans MS", 15, "bold"))

repeat(timer, 330, -330) 
timer.write(f"01:10", align = "center", font = ("ComicSans MS", 20, "bold"))   
name_text = rate.textinput(title = "State", prompt = "What's your name: ").title()

guessed_state = []
writer.ht()

rating = True
def func():
    global Time
    global score
    global name_text
    if  Time > 0 :
        Time -= 1
        mod = int(Time / 60)
        moder = Time % 60
        if mod < 10 and moder >= 10:
            timer.clear()
            timer.write(f"0{int(mod)}:{moder}", align = "center", font = ("ComicSans MS", 20, "bold"))
        elif mod < 10 and moder < 10:
            timer.clear()
            timer.write(f"0{int(mod)}:0{moder}", align = "center", font = ("ComicSans MS", 20, "bold"))
        else:
            timer.clear()
            timer.write(f"0{int(mod)}:{moder}", align = "center", font = ("ComicSans MS", 20, "bold"))
        turtle.ontimer(fun = func, t = 1000)
    elif Time == 0:
        rare = []
        for m in range(0, 18):
            if listdoc[m] not in guessed_state:
                rare.append(listdoc[m])
        for m in rare:
            time.sleep(1)
            statesify = doc[doc.states == m]
            writer.penup()
            writer.color("white")
            writer.goto(int(statesify["x"]), int(statesify["y"]))
            writer.pendown()
            writer.write(f"{m}", align = "center", font = ("ComicSans MS", 13, "bold"))
        time.sleep(5)
        rate.clear()
        rate.bgcolor("black")
        writer.penup()
        writer.goto(0, 0)
        writer.pendown()
        writer.write(f"Game Over {name_text}!\nYour score is {score}", align = "center", font = ("ComicSans MS", 18, "bold"))
    elif  state_text == "Exit" or score == 18:
        pass
                
                
        
func()
rating = False

while len(guessed_state) != 19:
    state_text = rate.textinput(title = "State", prompt = "Mention a state: ").title()
    if state_text == "Exit":
        rare = []
        for m in range(0, 18):
            if listdoc[m] not in guessed_state:
                rare.append(listdoc[m])
        for m in rare:
            time.sleep(1)
            statesify = doc[doc.states == m]
            writer.penup()
            writer.color("white")
            writer.goto(int(statesify["x"]), int(statesify["y"]))
            writer.pendown()
            writer.write(f"{m}", align = "center", font = ("ComicSans MS", 13, "bold"))
        time.sleep(5)
        rate.clear()
        rate.bgcolor("black")
        writer.penup()
        writer.goto(0, 0)
        writer.pendown()
        writer.write(f"Game Over {name_text}!\nYour score is {score}", align = "center", font = ("ComicSans MS", 11, "bold"))
    if state_text in listdoc and state_text not in guessed_state:
        score += 1
        guessed_state.append(state_text)
        statesy = doc[doc.states == state_text]
        writer.penup()
        writer.goto(int(statesy["x"]), int(statesy["y"]))
        writer.pendown()
        writer.write(f"{state_text}", align = "center", font = ("ComicSans MS", 13, "bold"))
        scoree.clear()
        scoree.write(f"{score}/18", align = "center", font = ("ComicSans MS", 20, "bold"))
    if  score == 18:
        time.sleep(1)
        rate.clear()
        rate.bgcolor("black")
        writer.penup()
        writer.goto(0, 0)
        writer.pendown()
        writer.write(f"Game Over!\n{name_text} is a winner!\nYour score is {score}", align = "center", font = ("ComicSans MS", 15, "bold"))
        break
    

rate.onscreenclick(get_mouseOn_click)
rate.mainloop()