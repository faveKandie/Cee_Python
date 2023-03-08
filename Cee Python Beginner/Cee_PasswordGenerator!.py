import random

print("Welcome to Cee_password Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '?']

letter = int(input("How many letters would you like in your password?: "))

symbol = int(input("How many symbols would you like?: "))

number = int(input("How many numbers would you like?: "))

password = []
#the password is declared so that in the end, we can have all random choices on a straight line
#since what we are getting from the random is a string list, we declare the variable as a string using the ""
for char in range(1, letter + 1):
  rand_char = random.choice(letters)
  password += rand_char
for dist in range(1, symbol + 1):
  rand_dist = random.choice(symbols)
  password += rand_dist
  #for a string, the += serves as a concatenation but in integers, it's addition
for numb in range(1, number + 1):
  rand_numb = random.choice(numbers)
  password += rand_numb

random.shuffle(password)
print(password)
rad = ""
for passer in password:
  rad += passer
  
print(f"Your random password is {rad}")

