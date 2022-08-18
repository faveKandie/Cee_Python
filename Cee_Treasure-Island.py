#Cee Treasure Island written in python.
print("Welcome to Treasure Island\nYour mission is to find the treasure.")
print("All inputs should be in small letter")
road = input("\nYou are at a crossroad, do you want to go left or right?: ")

if road == "left":
  deci = input('\nYou came to a lake, there is an island in the middle of the lake.\nType "wait" to wait for a boat or "swim" to swim across: ')
  if deci == "wait":
    colour = input("\nYou arrive at the island unharmed.\nThere is a room with three doors. Pick a colour: Red, Blue, yellow: ")
    if colour == "blue":
      action = input("\nIf you take any other step, you could fall. Do you step or go BACK: ")
      if action == "step":
        dig = input("\nOh! You're just covered in dust. It's not that deep anywhere.\n The room is now full of water: Do you follow the open TOP or dig BELOW: ")
        if dig == "top":
          round = input("\nYou're on a thin cliff. Do you walk over or run over: ")
          if round == "walk":
            door = input("\nYou arrive at two balcony doors. Pick a door: door1 or door2: ")
            if door == "door2":
              lady = input("\nYou find an old lady. Do you take her lead. Yes or no.: ")
              if lady == "yes":
                love = input("\nYou both found the treasure. But only one person can make it, and she's injured. Do you save her or leave her or kill her. save, leave, kill: ")
                if love == "kill":
                  last = ("\nBecause you've got a map\nHint: left is a dead end. You have the treasure and you're at a crossroad. left, right or centre: !")
                  if last == "centre":
                    print("\nYou made it out. You win!")
                  else:
                    print("\nYou came so far but still lost. Game over!")
                elif love == "leave":
                  last = input("\nYou've got no map. But you're out. Which way do you go: left, right or centre: ")
                  if last == "right":
                    print("\nYou came so far but still lost. Game over!")
                  elif last == "centre":
                    print("\nMonster scorpion stung you. Game over!")
                  else:
                    print("\nYou made it out. You win!")
                else:
                  print("You both died. Game over!")
              else:
                print("She casts a spell on you. Game over!")
            else:
              print("The guards kick you down the cliff. Game Over.")
          else:
            print("You fall down the cliff. Game Over!")
        else:
          print("You drown before you succeeded Game Over!")
      else:
        print("You're eaten by zombies. Game Over!")
    elif colour == "red":
      action = input("\nAll that glitters is not gold, But atleast you found yourself in a secret room. There are two boxes. Box1 or Box2: ")
      if action == "box1":
        print("A can of worms. Game over!")
      else:
        leave = input("You've found the treasure. Now go out! Do you go throgh same door or take a small door: same or small?: ")
        if leave == "same":
          print("Same road doesn't lead to same destination. Game over.")
        else:
          print("\nYou meet a door of questions. Pass all three and a jet awaits you!")
          simple = input("From RBG, R means: ")
          if simple == "red":
            another = input("Check 1 is correct\nB means: ")
            if another == "blue":
              let = input("Check 2 is also correct. One to go. G means: ")
              if let == "green":
                print("Check 3 correct. You win!")
              else:
                print("Game over. Loser.")
            else:
              ("You came so far but game over\n")
          else:
            print("Game over!")
    elif colour == "yellow":
      print("\nYou're a meat to these hungry lions. Game Over!")
  else:
    print("The waves carried you to your death. Game over!")
else:
  print("A snake just bit you! Game over!")
  
