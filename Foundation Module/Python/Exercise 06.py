#Task 1:
 
def check_attendence(students, absentees):
  return[student for student in students if student in absentees]

students = ["Alice", "Bob", "Charlie", "David"]
absentees = ["Bob", "David"]

check_attendence(students, absentees)
print(absentees)

#Task 2: Functions for real life data processing
def calculate_average_grade(grades_dict):
  total = sum(grades_dict.values())
  average_grade = total / len(grades_dict) 
  return average_grade

class_grades_dict = {
  "Alice": 85,
  "Bob": 92,
  "Charlie": 78,
  "David": 90,
}

result = calculate_average_grade(class_grades_dict)
print(f"The average grade is: {result}")

#Task 3: Function returning a function (higher order function)

def operation_selector(operation):
  def add(x, y):
    return x + y
  def multiply(x, y):
    return x * y
  if operation == "add":
    return add
  elif operation == "multiply":
    return multiply
  else:
    return operation_selector("Invalid operation")
  
add_function = operation_selector("add")
if add_function:
  result_add = add_function(4, 6)
  print(f"Addition Result: {result_add}")

multiply_function = operation_selector("multiply")
if multiply_function:
  result_multiply = multiply_function(3, 7)
  print(f"Multiplication Result: {result_multiply}")

  #Task 4: Function for a practical scenario

def calculate_trip_cost(distance, fuel_efficiency, fuel_price):
  fuel_needed = distance / fuel_efficiency
  total_cost = fuel_needed * fuel_price
  return total_cost
print(calculate_trip_cost(100, 10, 1.5))

#Task : Using a for loop with a dictionary (Real-life Scenario: Grocery Shopping List)
grocery_inventorydict = {
    "Beefstock": 50,
    "Polony slices": 30,
    "Cheese": 25,
    "Carrots": 15,
    "Potatoes": 10
}
for item, quantity in grocery_inventorydict.items():
  print(f"{item}: {quantity} in stock")
total_items = sum(grocery_inventorydict.values())
print(f"Total number of items in stock: {total_items}")

#Task 5: Using a while loop for banking (Real-life Scenario: ATM Pin Retry System)

pin = input("Enter your pin")
correct_pin = 1234
pin_attempts = 3
while pin_attempts>=0:
  if pin == correct_pin:
    print("Access Granted")
    break
  else:
    pin_attempts -=1
    if pin_attempts >0:
      pin = input("Pin is incorrect, Try again")
    else: 
      print("Account locked")

#Task 6:Using a for loop with range() for a school grading system

import random

score = [random.randint(0,100) for _ in range (10)]
total_score = sum(score)
average_score = total_score / len(score)
print(f"Average score for the class: {average_score}")
if average_score > 75:
  print("Congratulations! The average score is above 75.")

#Task 7: Using a for loop with a list of dictionaries (Real-life Scenario: Employee Salary Calculation)

import random

participants = ["Azola", "Khanya", "Yolanda", "Likhona", "Andy", "Phelo", "Athi", "Kleyt", "Scott", "Oyster", "Lisa", "Buhle", "Ovayo", "Nyinyi", "Mbayzo", "Lethu", "Yanga", "Thamsanqa", "Amahle", "likho"]
selected_participants = random.sample(participants, 5)
print("Selected Participants for the Team:")

for participant in selected_participants:
    print(participant)

#Task 8: Using the random module (Real-life Scenario: Random Team Selection)

import fitness_tracker
distance_walked = input("Enter the distance walked in km: ")
distance_run = input("Enter the distance run in km: ")
distance_cycled = input("Enter the distance cycled in km: ")
calories_walked = fitness_tracker.walk_calories(float(distance_walked))
calories_run = fitness_tracker.run_calories(float(distance_run))
calories_cycled = fitness_tracker.cycle_calories(float(distance_cycled))
total_calories = sum([calories_walked, calories_run, calories_cycled])
print(f"Calories burned from walking: {calories_walked}")
print(f"Calories burned from running: {calories_run}")
print(f"Calories burned from cycling: {calories_cycled}")
print(f"Total calories burned: {total_calories}")


#Task 10: Using a while loop with to stimulate loan repayment (real-life scenario: paying off a loan)
loan_amount = float(input("Enter the loan amount: "))
monthly_payment = float(input("Enter the monthly payment: "))
while loan_amount > 0:
  loan_amount -= monthly_payment
  print(f"Remaining loan amount: {loan_amount}")
if loan_amount <= 0:
  print("congratulations! Loan fully repaid!")










