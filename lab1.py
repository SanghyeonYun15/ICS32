# lab1.py

# Starter code for lab 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Sanghyeon Yun
# sanghyey@uci.edu
# 34237269

def calculate(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
        return result
    elif operator == "-":
        result = num1 - num2
        return result
    elif operator == "*":
        result = num1 * num2
        return result

def main():
    print("Welcome to ICS 32 PyCalc!\n")
    first_openand = int(input("Enter your first operand: "))
    second_openand = int(input("Enter your second operand: "))
    operator = input("Enter your desired operator (+ to add, - to subtract, or * to multiply): ")
    calc_result = calculate(first_openand, operator, second_openand)
    print(f"\nThe result of your calculation is: {calc_result}")

main()