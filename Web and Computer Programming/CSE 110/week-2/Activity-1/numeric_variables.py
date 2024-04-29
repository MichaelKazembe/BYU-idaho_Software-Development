"""
AUTHOR: MICHAEL KAZEMBE

numeric_variables.py

This program demonstrates the use of numeric variables in Python.


"""
# Problem 1
# Prompt the user for their age. Convert the age to an integer and store it in a variable called age.
# Add one to it, and tell them how old they will be next year.

age = int(input("\nHow old are you? "))
age_next_year = age + 1
print(f"You will be {age_next_year} on your next birthday.")

# Problem 2
# Prompt the user for the number of egg cartons they have. 
# Assume each carton holds 12 eggs, multiply their number by 12, 
# and display the total number of eggs.

egg_cartons = int(input("How many egg cartons do you have? "))
total_eggs = egg_cartons * 12
print(f"You have {total_eggs} eggs in total.")

# Problem 3
# Prompt the user for a number of cookies and a number of people. 
# Then, divide the number of cookies by the number of people 
# to determine how many cookies each person gets.

num_cookies = int(input("\nHow many cookies do you have? "))
num_people = int(input("How many people are there? "))
cookies_per_person = num_cookies / num_people
print(f"Each person gets {cookies_per_person} cookies.")

# end of program
