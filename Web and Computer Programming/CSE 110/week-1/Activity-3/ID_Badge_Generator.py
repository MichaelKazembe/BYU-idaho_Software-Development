"""
ID_Badge_Generator.py

Program that prompts the user to enter their first name, last name, 
email, phone number, job title, and ID number. The program then prints
the ID card with the user's information.

"""

# Prompt User To Enter Their Information

print("Please enter the following information: \n")
# Prompt User For Their First Name
first_name = input("Enter Your First Name: ")
# Prompt User For Their Last Name
last_name = input("Enter Your Last Name: ")
# Prompt User For Their Email
email = input("Enter Your email: ")
# Prompt User For Their Phone Number
phone = input("Enter Your phone number: ")
# Prompt User For Their Job Title
job_title = input("Enter Your job title: ")
# Prompt User For Their ID Number
ID_number = input("Enter Your ID number: ")


# Print Personal Information
print("\n")
print("The ID Card is:")
print("------------------------------------------")
print(last_name.upper() + ", " + first_name.capitalize())
print(job_title.title())
print("ID: " + ID_number)
print("\n")
print(email.lower())
print(phone)
print("------------------------------------------")