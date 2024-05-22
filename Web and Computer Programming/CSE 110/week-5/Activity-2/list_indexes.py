"""
AUTHOR: MICHAEL KAZEMBE
DATE: 21/05/2024

list_indexes.py

A program that 

"""

shopping_items = [] # initialize shopping list
item = "" # empty string

while (item != "quit"):
    item = input("Please enter the items of the shopping list (type: quit to finish): ").lower()
    
    if item != "quit": # Prevents 'quit' from being added to the list
        shopping_items.append(item) # adds item to the list

print("\n")
print("The shopping list is: ")
for item in shopping_items: # iterates through the item list
    print(item)

print("\n")
print("The shopping list with indexes is: ")
for i in range(len(shopping_items)):
    item = shopping_items[i]
    print(f"{i}. {item}")

print("\n")
index =int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

shopping_items[index] = new_item

print("\n")
print("The shopping list with indexes is: ")
for i in range(len(shopping_items)):
    item = shopping_items[i]
    print(f"{i}. {item}")

