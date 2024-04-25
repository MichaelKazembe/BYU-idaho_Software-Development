""" 
Input_output.py

This program prompts the user for their first and
last name and then displays the text back all on one
line saying, "Your name is last-name, first-name, last-name"

"""

# Prompt the user for their first name
first_name = input("What is your first name? ")
# Prompt the user for their last name
last_name = input("What is your last name? ")

# Display the text back all on one line saying, "Your name is last-name, first-name, last-name"
print("Your name is", last_name + ",", first_name, last_name + ".")


# Adjust the Capitalization
# Display the words using the .title() function 

print("Your name is", last_name.title() + ",", first_name.title(), last_name.title() + ".")
