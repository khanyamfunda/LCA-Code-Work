#QUESTION 1
x = 14
x += 3
y = 25
y *= 2
result = x/y
print(result)
#QUESTION 2
a = 24
b = 17
c = 5
print(a>b)
print(17%2==0)
print(c<=a)
final_condition = (a>b or 17%2==0 and c<=a)
print(final_condition)
#QUESTION 3
score = int(input("enter your test score(0-100): "))
if score >=90 and score <=100:
  grade = "A"
elif score >=80:
  grade = "B"
elif score >=70:
  grade = "C"
elif score >=60:
  grade = "D"
else:
  grade = "F"
print(f"Your grade is: {grade}")
#QUESTION 4
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
operation = input("enter the operation (+,-,*,/): ")
if operation == "-":
  result = num1 - num2
elif operation == "+":
  result = num1 + num2
elif operation == "*":
  result = num1 * num2
elif operation == "/":
  result = num1 / num2
else:
  result = "division by 0 is not allowed"
print(f"the result is:{result}")




      

