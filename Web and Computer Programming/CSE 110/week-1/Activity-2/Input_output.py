""" 
AUTHOR:  MICHAEL KAZEMBE
DATE:  23/04/2024
COURSE:  CSE 110: Introduction to Programming
INSTRUCTOR:  CHAD OWENS
ASSIGNMENT:  Activity 2 - Input and Output
PURPOSE:  To write a program that asks a user for their favorite color, then allow them to type in their color. Finally, have the program respond to them by displaying the text "Your favorite color is" followed by the color they typed.

* Activity Instructions *
** Overview **
An iconic line from the James Bond movies is that he would introduce himself as "Bond, James Bond." For this assignment you will write a program that asks for your name and repeats it back in this way.

** Instructions **
Prompt the user for their first name. Then, prompt them for their last name. Display the text back all on one line saying, "Your name is last-name, first-name, last-name" as shown:


`What is your first name? Scott
What is your last name? Burton

Your name is Burton, Scott Burton.

What is your first name? Brigham
What is your last name? Young

Your name is Young, Brigham Young.`

Adjust the Capitalization
Now that the program is displaying the strings back with the correct spacing, improve your program by making it display the words using the .title() function on each variable so that it capitalizes only the first letter and all the other letters are lowercase.

Test that your program works by trying some words that are capitalized and some that are lower case. The output should be the same. For example:


What is your first name? Brigham
What is your last name? Young

Your name is Young, Brigham Young.

What is your first name? brigham
What is your last name? YOUNG

Your name is Young, Brigham Young.

What is your first name? brIGham
What is your last name? YOUng

Your name is Young, Brigham Young.

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
