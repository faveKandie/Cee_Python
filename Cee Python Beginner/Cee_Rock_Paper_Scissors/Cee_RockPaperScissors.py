import random

name = input("Enter your name: ")
print("\nWhat do you chose:\n1 for rock\t2 for paper\t3 for scissors.\n")
pick = int(input(name + " " + "drew: "))

varname = random.randint(1, 3)

rock = '''
    _________
___|    (____)
     )  (_____)
  rock!  (____)
_____    (___)
     '___(_)
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
    ________
   |  (_____)__
---'     ______)
scissors ______)
_____ (_____)
     '_(___)
'''

if pick == 1:
  print(rock)
  varname = random.randint(1, 3)
  print(f" The compueter drew: {varname}")
  if varname == 1:
    print (rock)
    print("It's a draw")
  elif varname == 2:
    print (paper)
    print("You lose!")
  else:
    print(scissors)
    print("You win!")
elif pick == 2:
  print(paper)
  varname = random.randint(1, 3)
  print(f" The computer drew: {varname}")
  if varname == 2:
    print(paper)
    print("It's a draw!")
  elif varname == 1:
    print(rock)
    print("You win!")
  else:
    print(scissors)
    print("You lose!")
else:
  print(scissors)
  varname = random.randint(1, 3)
  print(f"The computer drew: {varname}")
  if varname == 3:
    print(scissors)
    print("It's a draw!")
  elif varname == 2:
    print(paper)
    print("You win!")
  else:
    print(rock)
    print("You lose!")
    
  


