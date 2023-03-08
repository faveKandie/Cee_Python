#A program that checks if an inputed year is a leap year or not
year = int(input("What year do you want to check: "))

if year % 4 == 0:
   if year % 100 == 0:
     if year % 400 == 0:
       print("Check 3: \nLeap: Satisfied. It is a leap year.")
     else:
       print("Check 3: \nNot Leap: Not satisfied. It is not a leap year.")
   else:
     print("check 2: \nLeap: Satisfied. It is a leap year.")
else:
  print("Check 1: \nLeap: Not satisfied. It is not a leap year.")