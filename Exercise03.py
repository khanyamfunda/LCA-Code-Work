#Question 1: Basic Function Definition and Calling
def greeting():
  print("Hello World!")

greeting()

#QUESTION 3: FUNCTION WITH PARAMETERS
def personalized_greeting(firstname, lastname):
  print("Hello " + firstname + " " + lastname + "!")
        
personalized_greeting("Khanya", "Mfunda")

#QUESTION 3: FUNCTION WITH RETURN VALUE
def square(number):
  return number ** 2
result = square(5)
print(result)

#QUESTION 4: Function with Multiple Parameters and Return Value
def rectangle_area(length, width):
  area = length*width
  print(area)

rectangle_area(3,4)

#QUESTION 5: Using a Function as an Argurment
def apply_operation(function, number):
  return function(number)

def double(number):
  return number * 2

print(apply_operation(double, 7))

def square(number):
  return number ** 2

print(apply_operation(square, 3))


