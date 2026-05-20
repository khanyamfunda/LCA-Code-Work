#Question 1: iterating with index and value

dishes = ["boerewors roll", "maponya wormms", "vetkoek", "pap", "samp and beans"]
for i, dish in enumerate(dishes):
  print(f"{i}, Dish: {dish}")

#Question 2: countdown with timer
import time
countdown = 10
while countdown > 0:
  print(countdown)
  time.sleep(1)
  countdown -= 1
print("Countdown finished!")

#Question 3: printing squares and cubes in a table

print(f"{'Number':^6} {'Square':^6} {'Cube':^6}")
for num in range(1, 11):
  print(f"{num:^6} {num**2:^6} {num**3:^6}")

#Question 4: random selection with no repeats
import random
colours = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"]
selected_colours = random.sample(colours, 5)
print("Selected Colours:")
for colour in selected_colours:
  print(colour)

#Question 5: using a custom module and looping calculator
import math_advanced

def calculator():
  while True:
    operation = input("Enter operation (add, subtract, multiply, divide) or 'q' to quit: ")
    if operation == 'q':
      print("Exiting calculator.")
      break
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if operation == 'add':
      result = math_advanced.add(num1, num2)
    elif operation == 'subtract':
      result = math_advanced.subtract(num1, num2)
    elif operation == 'multiply':
      result = math_advanced.multiply(num1, num2)
    elif operation == 'divide':
      result = math_advanced.divide(num1, num2)
    else:
      print("Invalid operation. Please try again.")
      continue
    
    print(f"Result: {result}")
