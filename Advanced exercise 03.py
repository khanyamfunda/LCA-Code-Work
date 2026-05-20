#Question 1: Function with parameters and conditional logic

def greet_user(name, role):

  
  if role == "admin":
    print(f"Hello admin {name}!" )
  else:
    print(f"Hello {name}, enjoy your session" )

greet_user("Khanya", "admin")

#Question 2: Functions with default and keywords arguments:

def register_students(name, course, country):
  print(f"Hello {name}, you have registered for {course} in {country}")

register_students( "Khanya", "Busimess information systems", "South Africa")
register_students(course = "Business information systems", name = "Khanya", country = "South Africa")

#QUESTION 3: Returning multiple values

def calculate_scores(score1, score2, score3):
  total_score = int(score1) + int(score2) + int(score3)
  avarage = int(total_score)/3
  return total_score, avarage

total, average = calculate_scores(24, 30, 35)
print(f"Total score: {total}, Average score: {average}")
print(f"total score: {total}")
print(f"average score: {average}")

#Question 4: Nested functions

def student_progress(name, score1, score2, score3):
  def average_score():
    return (score1 + score2 + score3) / 3

  average = average_score()
  return f"{name}'s average score is: {average}"
progress_report = student_progress("Khanya", 43, 39, 35)
print(progress_report)

#Question 5: Function as arguments with lambdas

def apply_to_list(list, func):
  return [func(x) for x in list]
doubled = apply_to_list([1, 2, 3, 4], lambda x: x * 2)
squared = apply_to_list([1, 2, 3, 4], lambda x: x ** 2)
print(f"Doubled: {doubled}")
print(f"Squared: {squared}")


