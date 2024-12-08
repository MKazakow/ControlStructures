###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input("INPUT THE FiRsT NUMBER: "))
number2 = int(input("INPUT THE SECOND NUMBER: "))
operator = input("WHAT WOULD YOU LIKE TO CALCULATE? (+,-,*,/) ")
result = 0

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2
else:
    print("Invalid operator has been input")

# print result
print(f'{number1} {operator} {number2} = {result}')