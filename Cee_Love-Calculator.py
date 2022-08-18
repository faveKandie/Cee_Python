#love calculator written in python
print("Welcome to Cee_Love Calculator.\n")
name1 = input("What is your name: ")
name2 = input("What is your crush's name: ")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

t = lower_name1.count("t")
r = lower_name1.count("r")
u = lower_name1.count("u")
e = lower_name1.count("e")
T = lower_name2.count("t")
R = lower_name2.count("r")
U = lower_name2.count("u")
E = lower_name2.count("e")
l = lower_name1.count("l")
o = lower_name1.count("o")
v = lower_name1.count("v")
e = lower_name1.count("e")
L = lower_name2.count("l")
O = lower_name2.count("o")
V = lower_name2.count("v")
e = lower_name2.count("e")

score1 = (t + r + u + e + T + R + U + E) * 10
score2 = (l + o + v + e + L + O + V + E)

score = score1 + score2

print(f"Your love score is {score}%")

if score >= 85 and score <= 100:
  print("You guys are a perfect match!")
elif score >= 63 and score <= 84:
  print("You guys are a good match")
elif score >= 50 and score <= 62:
  print("You guys are just okay with each other")
elif score >= 30 and score <= 49:
  print("You guys are not so good with each other. You guys are better of as friends.")
elif score >= 0 and score <= 29:
  print("You guys are a poor match")
else:
  print("You guys don't just match for no bad reason")