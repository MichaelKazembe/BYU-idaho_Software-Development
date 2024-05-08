"""
AUTHOR: MICHAEL KAZEMBE
DATE: 07/05/2024

complex_conditions.py

This program demonstrates the use of complex conditions in Python.
A simplistic system to determine if a user can qualify for a loan.

"""

# Prompt the user to enter their rating between 1-10

print("\nPlease enter your rating between 1-10 for the following: \n")

loan_size = int(input("How large is the loan? " ))

credit_history = int(input("How good is your credit history? "))

income = int(input("How high is your income? "))

down_payment = int(input("How large is your down payment? "))

print("You entered the following information: ")


to_loan = False

# First, check if the loan size is at least 5
if loan_size >= 5:

    # If the credit history and income are both at least 7, then the decision is "yes"
    if credit_history >= 7 and income >= 7 :
        to_loan = True
    elif credit_history >= 7 or income >= 7 :
        if down_payment >= 5 :
            to_loan = True
        else: 
            to_loan = False
    else:
        to_loan = False

else:
    if credit_history < 4:
        to_loan = False
    else:
        if income >= 7 or down_payment >= 7 :
            to_loan = True
        elif income >= 4 and down_payment >= 4 :
            to_loan = True
        else:
            to_loan = False

if to_loan:
    print(f"Loan size: {loan_size}, Credit: {credit_history}, Income: {income}, Down Payment: {down_payment}")
    print("YES: This Loan is approved\n")
else:
    print(f"Loan size: {loan_size}, Credit: {credit_history}, Income: {income}, Down Payment: {down_payment}")
    print("NO: This Loan is not approved\n")

# End of Program
