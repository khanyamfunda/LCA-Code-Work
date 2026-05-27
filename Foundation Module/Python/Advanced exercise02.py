# Advanced Exercise 2: Operators, Conditionals, and Input Handling
import math

#Question 1: Multi-Step Arithmetic Operations
a = 5
b = 10
c = 7
a += 3
b *= 2
c %= 4
result = math.sqrt(a**2 + b**2 + c**2)
print(round (result, 2))


#Question 2: Complex Conditional Evaluation
x = int(input("enter first number: "))
y = int(input("enter second number: "))
z = int(input("enter third number: "))
is_even = x % 2 == 0
is_positive = y > 0
is_in_range = 10 <= z <= 50
final_condition = x % 2 == 0 and y > 0 and 10 <= z <= 50
print(final_condition)


#Question 3: Grading with Adjustments 
base_score = int(input("enter your base score: "))
bonus_points = 5
adjusted_score = base_score + bonus_points
late_penalty = 10
final_score = adjusted_score - late_penalty
print(final_score)
max_score = min(final_score, 100) 
final_score = max(max_score, 0)
print(final_score)  
if final_score >= 90:
  grade = "A"
elif final_score >= 80:
  grade = "B"
elif final_score >= 70:
  grade = "C"
elif final_score >= 60:
  grade = "D"
else:
  grade = "F"
print(grade)

#Question 4: Simple Calculator 
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
operation = input("enter the operation (+,-,*,/,**,%): ")
if operation == "-":
  result = num1 - num2
elif operation == "+":
  result = num1 + num2
elif operation == "*":
  result = num1 * num2
elif operation == "**":
  result = num1 ** num2
elif operation == "%":
  result = num1 % num2
elif operation == "/":
  result = num1 / num2
if operation == "/" and num2 == 0:
  result = "division by 0 is not allowed"
print(result)

