import math

height = int(input("What is the height of the wall?: m "))
width = int(input("What is the width of the wall?: m "))
coverage = 5
cans = 0

def func_name(height, width, coverage, cans):
  cans += math.ceil((height * width) / coverage)
  print(f"Given a wall of {height}m height and {width}m width.")
  print(f"Remember, 1 can of paint can cover {coverage} square meters")
  if cans == 1:
    print(f"You'll need just a can of paint")
  else:
    print(f"You'll need {cans} cans of paint")
  
func_name(height, width, coverage, cans)