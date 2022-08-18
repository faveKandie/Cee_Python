print("Welcome to Cee_score calculator.")
score = input("Please enter the score of the student separated by a comma: ")

split_score = score.split(", ")
for n in range(0, (len(split_score))):
  split_score[n] = int(split_score[n])

number = 0
for m in split_score:
  number += 1

varname = 0
for p in split_score:
  varname += p

print(f"The total number of courses he took is: {number}")
print(f"The total number of his scores is: {varname}")

av_score = round(varname / number)
print(f"The average score is {av_score}")

highest = 0
for r in split_score:
  if r > highest:
    highest = r

print(f"The highest score is: {highest}")