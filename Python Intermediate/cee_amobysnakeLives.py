from turtle import Turtle, Screen
import cee_amobySnakeGame

lives = 3
varss = Screen()

user_input = varss.textinput(title = "cee-amoby_snakeGame", prompt = "Do you want to save yourself?: ")

pro = True
while pro:
    if user_input == "yes" or user_input == "YES":
        lives -= 1
        if lives == 0:
            pro = False
            