a = float(input("Please enter a number: "))

b = float(input("Please enter another number: "))
user = input("Do you want to '+', '/' '*' '-' : ")
if user == "+":
    result = round((a + b), 3)
    print(f"The answer is {result}")
elif user == "/":
    result = round((a / b), 3)
    print(f"The answer is {result}")
elif user == "*":
    result = round((a * b), 3)
    print(f"The answer is {result}")
elif user == "-":
    result = round((a - b), 3)
    print(f"The answer is {result}")
else:
    print("You entered an invalid operation")



quest = False
while not quest:
    ask = input("Do you want to perform anther operation: ")
    if ask == "yes":
        print("\n")
        b = float(input("Please enter another number: "))
        user = input("Do you want to '+', '/' '*' '-': ")
        if user == "+":
            result += b
            print(f"The new answer is {result}")
        elif user == "/":
            result /= b
            print(f"The new answer is {result}")
        elif user == "*":
            result *= b
            print(f"The new answer is {result}")
        elif user == "-":
            result -= b
            print(f"The new answer is {result}")
        else:
            print("You entered an invalid operation")
    if ask == "no":
        quest = True
        print(f"The final answer is {round(result, 3)}")
        break
