score = 0
#the self argument in all functions of a class enables the circular use of models. In this way, object are recognizable and interused
class QuizBrain:
	def __init__(self, q_list): #this function automatically access the data module and so does the class
		self.question_number = 0 #from the data module, it is the positional array of the element of the list initialized at 0
		self.question_list = q_list #from the data module, self.question_list is the list named question_data
	
	def still_has_question(self):#this function enables the continues loop to access the various elements in the list from th data module
		if self.question_number < 10:
			return True
		else:
			print(f"You've completed the Quiz and your final score is {score}/{self.question_number}")
			return False
	
	def next_question(self): #this enables the elements of the list to be changing in a corresponding manner as the positional array changes
		current_question = self.question_list[self.question_number] #this accesses/represents the elements of the list
		self.question_number += 1 #this is the increment value of the positional array
		#as the positon changes/increases, the corresponding question element in that position of the list changes/comes up
		
		user_input = input(f"Q.{self.question_number}: {current_question.text}. (True/False): ").lower() #collects the users answer
		self.check_answer(user_input, current_question.answer) #calls the function check_anser here using self. to make the outcome accessible in this function.
		#the current_question.answer accesses the self.answer from the question_model module
	
	def check_answer(self, user_answer, correct_answer): #argument in this function
		#nb: each argument in each function performs a major role in the outcome of the main project.
		global score #to take rack of the users score, i initialized it as 0 and globally called it so i can use it locally
		rate = False #to avoid an infinite loop
		while not rate:
			if user_answer.lower() == correct_answer.lower():
				print("You got it right!")
				score += 1 #the increment value for each correct answer
				print(f"And your current score is {score}/{self.question_number}")
				print("\n")
				rate = True  #breaks the loop
			else:
				print("You failed it!")
				score += 0 #the maintained initial score for each wrong answer
				print(f"And your current score is {score}/{self.question_number}")
				print("\n")
				rate = True #breaks the loop
	