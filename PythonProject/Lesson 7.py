# Python calculator
from ctypes import HRESULT

operator = input("Enter an operator (+, -, *, /):")

if operator not in ["+", "-", "*", "-"]:
    print(f"The {operator} is not a operator")
    exit()
else:
    pass

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2st number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = "This is not good operator"

print(round(result, 2))