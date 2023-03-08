import random

row1 = ["[]", "[]", "[]"]
row2 = ["[]", "[]", "[]"]
row3 = ["[]", "[]", "[]"]

print(f"{row1}\n{row2}\n{row3}")
print("where row1 = 1, 2, 3.\n\t  row2 = 4, 5, 6.\n  And row3 = 7, 8, 9.")

print("\nWhich Box do you think the computer placed his 'Y' treasure in?.")
spot = int(input("Where do you want to put the treasure?: Box "))

varname = random.randint(1, 9)

if varname == 1:
  row1[0] = "y"
elif varname == 2:
  row1[1] = "y"
elif varname == 3:
  row1[2] = "y"
elif varname == 4:
  row2[0] = "y"
elif varname == 5:
  row2[1] = "y"
elif varname == 6:
  row2[2] = "y"
elif varname == 7:
  row3[0] = "y"
elif varname == 8:
  row3[1] = "y"
else:
  row3[2] = "y"

if spot == 1:
  row1[0] = "x"
elif spot == 2:
  row1[1] = "x"
elif spot == 3:
  row1[2] = "x"
elif spot == 4:
  row2[0] = "x"
elif spot == 5:
  row2[1] = "x"
elif spot == 6:
  row2[2] = "x"
elif spot == 7:
  row3[0] = "x"
elif spot == 8:
  row3[1] = "x"
else:
  row3[2] = "x"
  
print(f"{row1}\n{row2}\n{row3}")

if spot == varname:
  print("\nYou win!")
  print(f"The compuer placed in {varname} too!")
else:
  print("\nYou lose.")
  print(f"The compuer placed {varname}")