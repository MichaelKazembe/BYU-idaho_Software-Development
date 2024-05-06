"""
AUTHOR: MICHAEL KAZEMBE

if_statements.py

This program demonstrates the use of if statements in Python.

"""

# COMPARE TWO NUMBERS

# Prompt the user to enter two numbers

first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))

# Compare the two numbers and display the result

if first_num > second_num:
    print(" The first number is greater\n")
else:
    print("The first number is not greater\n")

if first_num == second_num:
    print("The Numbers are equal\n")
else:
    print("The Numbers are not equal\n")

if second_num > first_num:
    print("The second number is greater\n")

# COMPARING STRINGS

# Prompt the user to enter their favorite animal
animal = input("Enter your favorite animal: ")

if animal.lower() == 'dog':
    print("That's my favorite animal too\n")
else:
    print("That's not my favorite animal\n")


