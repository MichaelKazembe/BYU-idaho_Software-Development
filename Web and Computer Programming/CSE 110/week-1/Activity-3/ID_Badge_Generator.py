"""
AUTHOR:  MICHAEL KAZEMBE
DATE:  23/04/2024
COURSE:  CSE 110: Introduction to Programming
INSTRUCTOR:  CHAD OWENS
ASSIGNMENT:  Activity 3 - ID Badge Generator
PURPOSE:  To write a program that asks a user for their favorite color, then allow them to type in their color. Finally, have the program respond to them by displaying the text "Your favorite color is" followed by the color they typed.

** Overview **
An ID badge, such as a drivers license or student ID, contains personal details that are formatted in a very specific way.

For this activity you will write a program that will create a properly formatted ID badge.

** Assignment **
Write a program to prompt the user for the following:

- First name, Last name, Email Address, Phone Number, Job Title, ID Number


Then you should display the information back in this format:

Note that the square brackets [] indicate a value coming from the user and should not be displayed.


----------------------------------------
[LAST NAME], [first name]
[Job title]
ID: [id number]

[email address]
[phone number]
----------------------------------------
In addition to the spacing and punctuation shown above, you must implement the following requirements:

The last name should be converted from whatever the user types to be displayed in ALL CAPS.

The job title should be displayed so that the first letter is capitalized.

The email address should be displayed in all lowercase.

An example of the program running is shown:


Please enter the following information:

First name: Jane
Last name: Doe
Email address: JaneDoe@email.com
Phone number: (208) 555-1234
Job title: chief software architect
ID Number: 83-23821

The ID Card is:
----------------------------------------
DOE, Jane
Chief Software Architect
ID: 83-23821

janedoe@email.com
(208) 555-1234
----------------------------------------

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
print("ID:" + ID_number)
print("\n")
print(email.lower())
print(phone)
print("------------------------------------------")