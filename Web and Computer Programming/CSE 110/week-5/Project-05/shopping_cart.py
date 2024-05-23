"""
AUTHOR: MICHAEL KAZEMBE
DATE: 23/05/2024

shopping_cart.py

A program that stores a list of products in a shopping cart 
along with their prices

"""

"""

Have menu system that repeats until the user chooses quit.

Create a list that will store the actions of the items in the shopping cart.

Complete the option to add the action of the item to the list.

Complete the option to display the actions of the items in the list.

"""

# START PROGRAM

# DEFINE a function shopping_cart():
def shopping_cart():
    # PRINT welcome screen 
    print("Welcome to the Shopping Cart Program!\n")
    # INITIALIZE empty list called items
    items = []
    # INITIALIZE empty list called prices
    princes = []

    # INITIALIZE empty variable called action
    action = ""

    # LOOP indefinitely:
    while (action != 5):
        # PRINT OPTIONS
        print("Please select one of the following:")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        # PROMPT user to enter an action
        # STORE the user input in variable action
        action = int(input("Please enter an action: "))
    
        # IF action is 1:
        if (action == 1):
            # PROMPT user to enter item
            name = input("What item would you like to add? ")
            # APPEND item to items 
            items.append(name)
            # FOR item in items
            for item in items:
            # PRINT item
                print(f"'{item.capitalize()}' has been added to the cart.\n")

        # IF action is 2:
        if (action == 2):
            if (len(items) > 0):
                print("The contents of the shopping cart are:")
                for item in items:
                    print(f"{item}")
            else:
                print("Your shopping cart is empty! Please add some items")

        # IF action is 5:
        if (action == 5):
            # PRINT goodbye message
            print("Thank you. Goodbye!")
            # BREAK the loop
            break

shopping_cart()

# END