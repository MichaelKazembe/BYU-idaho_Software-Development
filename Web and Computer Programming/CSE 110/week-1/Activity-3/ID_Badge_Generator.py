"""
ID_Badge_Generator.py

Program that prompts the user to enter their first name, last name, 
email, phone number, job title, and ID number. The program then prints
the ID card with the user's information.

"""

# Prompt User To Enter Their Information

print("Please enter the following information: \n")
# Prompt User For Their First Name
first_name = input("Enter Your First Name: ").upper()
# Prompt User For Their Last Name
last_name = input("Enter Your Last Name: ").capitalize()
# Prompt User For Their Email
email = input("Enter Your email: ").lower()
# Prompt User For Their Phone Number
phone = input("Enter Your phone number: ")
# Prompt User For Their Job Title
job_title = input("Enter Your job title: ").title()
# Prompt User For Their ID Number
ID_number = input("Enter Your ID number: ")

# Prompt User For Their Hair Color
hair = input("Enter Your Hair Color: ")
# Prompt User For Their Eye Color
eye = input("Enter Your Eye Color: ").capitalize()
# Prompt User For Month They Started Working
month = input("Enter The Month You Started Working: ")
# Prompt User Whether They Completed Advanced Training
training = input("Did You Complete Advanced Training? (Yes/No): ")

# Print Personal Information With Stretch Challenge
print("\nThe ID Card is:")
print("-" * 42)
print(f"{last_name}, {first_name}")
print(job_title)
print(f"ID: {ID_number}")
print("\n")
print(email)
print(phone)
print("\n")
# Stretch Challenge: formatting the string to the right to align the text
print(f"Hair: {hair:<15} Eyes: {eye.capitalize()}") # string Formatting 15 spaces to the right
print(f"Month: {month:<14} Training: {training.capitalize()}") # string Formatting 14 spaces to the right
print("-" * 42)

# End Of Program

