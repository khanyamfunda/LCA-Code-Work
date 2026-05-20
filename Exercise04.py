#Question 1: Using a for loop with a list
list = ("apple", "banana", "grapes", "pear")
for x in list:
  print(x)

#Question 2: Using a while loop for countdown
i = 5
while i>=0:
  print("this is a countdown" + str(i))
  i=i-1

#Question 3: Using a for loop with range()
for i in range(1, 11):
  print(i ** 2)

#Question 4: Using the random module 
import random

colours = ("red", "purple", "blue", "black", "white", "green")
for i in range(3):
  print(random.choice(colours))

#QUESTION 5: Creating and using a custom module
import math_operations


while True:
  operation = input("Enter operation (add, subtract, multiply, divide) or 'exit' to quit: ")
  if operation == "exit":
    break
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  
  if operation == "add":
    print(math_operations.add(num1, num2))
  elif operation == "subtract":
    print(math_operations.subtract(num1, num2))
  elif operation == "multiply":
    print(math_operations.multiply(num1, num2))
  elif operation == "divide":
    print(math_operations.divide(num1, num2))
  else:
    print("Invalid operation. Please try again.")

