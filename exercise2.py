# Question 1: Arithmetic and Assignment Operators
x = 10
y = 2
x += 3
y *= 2
result = x / y
print(result)

# Question 2: Comparison and Logical Operators
a = 10
b = 4
c = 8
condition1 = a > b
condition2 = b % 2 == 0
condition3 = c <= a
final_condition = condition1 or (condition2 and condition3)
print(final_condition)

# Question 3: Conditional Statements
score = 100
if 90 <= score <= 100:
  grade = "A"
elif 80 <= score < 90:
  grade = "B"
elif 70 <= score < 80:
  grade = "C"
elif 60 <= score < 70:
  grade = "D"
elif 0 <= score < 60:
  grade = "F"
else:
  grade = "Invalid score"
print("Your grade is:", grade)

# Question 4: Combining Operators and Conditionals 
num1 = 10
num2 = 5
operation = input("Enter an operation (+, -, *, /): ")
if operation == "+":
  result = num1 + num2
elif operation == "-":
  result = num1 - num2
elif operation == "*":
  result = num1 * num2
elif operation == "/":
  if num2 != 0:
    result = num1 / num2
  else:
    result = "Cannot divide by zero"
else: 
  result = "Invalid operation"

print("Result:", result)