"""
AUTHOR: MICHAEL KAZEMBE
DATE: 21/05/2024

lists.py

A program that creates lists, adds to them, and iterates through them.

"""

friends_names = [] # initialize list
name = "" # empty string

while (name != "end"):
    name = input("Enter name of your friend(type 'end' to finish): ").lower()
    
    if name != "end": # Prevents 'end' from being added to the list
        friends_names.append(name) # adds name to the list

print("\n")
print("Your friends are: ")
for name in friends_names: # iterates through the name list
    print(name)