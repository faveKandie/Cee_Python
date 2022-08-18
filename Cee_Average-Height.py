height = input("Please enter the height of the students in the class seperated by a comma: ")

re_height = height.split(", ")

varname = len(re_height)

print(" ")

for n in range(0, varname):
  re_height[n] = int(re_height[n])

total_height = 0

for m in re_height:
  total_height += m

number = 0

for p in re_height:
  number += 1
  

print(f"The total height of students in this class is {total_height} cm")
print(f"\nThe number of students in this class is: {number}")
print(f"The average height of students in this class will be total height / number of students\nWhich is {total_height} / {number} = ")

average_height = round(total_height / number)

print(f"{average_height} cm")