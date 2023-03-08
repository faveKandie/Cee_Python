import random

logo = '''
   _____   _ _ _   _____
  /  _  \ |  ___| |  ___|
 |  / |_| | |___  | |___
 | |   _  |  ___| |  ___|
 |  \_| | | |___  | |___
  \__ __/ |_____| |_____|
 _   _   _ _ _   __    _     _____ _       __    __   _ _ _   __    _
| | | | |  _  | |  \  | |   /       \     |  \  /  | |  _  | |  \  | |
| |_| | | |_| | |   \ | |  /  ____   \    |   \/   | | |_| | |   \ | |
|  _  | |  _  | | |\ \| | |  /       |    | |\ _/| | |  _  | | |\ \| |
| | | | | | | | | | \   | | |_ _________  |_|    |_| |_| |_| |_| \___|
|_| |_| |_| |_| |_|  \ _| |   |   ___   |  ______   ____     ____ ______
                          |   |__|   \  | |___   | |    \___/    |  ..  \
                     
                           \         /  | /  ... | |  | |  |  |  | |_____
                            \_______/ __| \___ __/ |__| |__|  |__|______/
                            '''

stages = ['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  0   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  0   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  0   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  0   |
      |
      |
      |
========
''', '''
  +---+
  |   |
      |
      |
      |
      |
========
''']

word = ["enabled", "hangman", "praised", "repeats", "ability", 
"hooked", "enable", "better", "random", "survive", "conquer", 
"apple", "breathe", "ceeamoby", "determined", "hired", "alien", 
"stars", "always", "programmer", "love", "start", "please", "sorry", 
"brought", "normal", "greatness", "study", "nicely", "friendship", 
"tough", "again", "london", "mathematics", "zealous", "patient", "content", 
"last", "best", "graduating", "student", "university", "opportunity"]

varname = len(word)
lives = 6

rand_word = ""
for p in range(0, varname):
  rand_word = random.choice(word)

lenrand_word = len(rand_word)
blank = []

for n in rand_word:
  blank += '_'

print(f"Welcome to {logo}")
print(f"{' '.join(blank)}")

end_game = False
print(f"Hint: The Word begins with {rand_word[0]} and ends in {rand_word[-1]}")

while not end_game:
    guess = input(f"\nGuess a letter from the {lenrand_word} lettered word: ").lower()
    for position in range(0, lenrand_word):
      letters = rand_word[position]
      if letters == guess:
        blank[position] = letters
    
    if guess not in rand_word:
      lives -= 1
      live = 6 - lives
      if lives == 0:
        end_game = True
        print(f"You lose!\nThe word given was: {rand_word}")
        if live == 1:
          print(f"You used {live} live")
        else:
          print(f"You used {live} lives")
    print(f"{' '.join(blank)}")
    if "_" not in blank:
      end_game = True
      print("You win!")
      live = 6 - lives
      if live == 1:
        print(f"You used {live} live")
      else:
        print(f"You used {live} lives")
      
    print(stages[lives])
