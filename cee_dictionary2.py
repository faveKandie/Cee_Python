student_scores = {
"ben": 89, 
"ola": 95, 
"manny": 60, 
"Harry": 81, 
"cee": 100,}

student_grades = {}

for key in student_scores:
  score = student_scores[key]
  if score > 90:
    student_grades[key] = "outsanding"
  elif score > 80:
    student_grades[key] = "exceeds expectations"
  elif score > 70:
    student_grades[key] = "Try better"
  else:
    student_grades[key] = "fail"
    
print(student_grades)
