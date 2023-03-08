import random


chose = input("What do you draw?\nrock, paper, scissors: ")
print(f"\you drew: {chose}")

listed = ["rock", "paper", "scissors"]
re_listed = len(listed)

for n in range(1, re_listed + 1):
  varname = random.choice(listed)

rock = '''
    ________
___|   (____)
     ) (_____)
  rock! (____)
_____   (___)
     '__(_)
'''

paper = '''
    __________
___|    ______)
        _______)
 paper!  ______)
_____    _____)
     '______)
'''

scissors = '''
    _______
___|  (____)___
         ______)
scissors ______)
_____ (____)
     '____)
'''

if chose == "rock":
  print(rock)
  print(f"The computer drew: {varname}")
  if varname == "rock":
    print(rock)
    print("It's a draw!")
  elif varname == "paper":
    print(paper)
    print("You lose!")
  else:
    print(scissors)
    print("You win!")
elif chose == "paper":
  print(paper)
  print(f"The computer drew: {varname}")
  if varname == "rock":
    print(rock)
    print("You win!")
  elif varname == "paper":
    print(paper)
    print("It's a draw!")
  else:
    print(scissors)
    print("You lose!")
else:
  print(scissors)
  print(f"The computer chose: {varname}")
  if varname == "rock":
    print(rock)
    print("You lose!")
  elif varname == "paper":
    print(paper)
    print("You win!")
  else:
    print(scissors)
    print("It's a draw!")