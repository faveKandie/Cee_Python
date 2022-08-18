import random
print("Welcome to Cee Restruant!")

print("\nMenu:\nSmall size = $15 \t Medium size = $20 \t Large size = $25\nPepperoni for small = $2 \t Pepperoni for other sizes = $3\nCheese for all sizes = $1")

size = input("\nWhat size of pizza do you want?:\n1. small 2. medium 3. large: ")
if size == "small":
  bill = 15
elif size == "medium":
  bill = 20
else:
  bill = 25

pep = input("\nPepperoni for what size do you want?:\n1. small 2. others 3. non : ")
if pep == "small":
  bill += 2
elif pep == "others":
  bill += 3
else:
  bill += 0

cheese = input("\nDo you want cheese?\n1. yes 2. no: ")
if cheese == "yes":
  bill += 1
else:
  bill += 0
  
orders = int(input("\nHow many orders are you making?: "))
bill *= orders

tip = int(input("\nWhat percentage of tip are you giving.\n1. 5 2. 10 3. 15: %"))
new_tip = round((tip / 100) * bill)

bill += new_tip

print(f"\nYou are tipping ${new_tip}")
print(f"Total cost of your order is ${bill}")
print("Your order has been made. Enjoy your pizza!")

banker = input("\nAre you splitting the bill? Yes or no?: ")

if banker == "no":
  number = int(input("\nHow many people are sitting at the table: "))
  name = input("Please input the names of the people at the table separated by a comma: ")

  re_name = name.split(", ")

  x = len(re_name)

  rand_choice = random.randint(0, x - 1)
  person = re_name[rand_choice]
  #as a random number of the list elements.

  print("\nThe persom that will pay for everyone's meal will be: " + person)
  print(f"{person}, you will pay ${bill}")
else:
  number = int(input("\nHow many people are sitting at the table: "))
  shared_bill = round(bill / number) 
  print(f"Each person will pay ${shared_bill}")
