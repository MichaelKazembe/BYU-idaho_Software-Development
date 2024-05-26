"""
AUTHOR: MICHAEL KAZEMBE
DATE: 23/05/2024

shopping_cart.py

A program that stores a list of products in a shopping cart 
along with their prices

"""

# STRETCH CHALLENGE
# Added price, quantity and subtotal of individual items
# Added formatting when viewing the cart
# Added a message when the cart is empty
# Added a message when the item number is invalid
# Added a message when the cart is empty
# Added a message when the action is invalid

# START PROGRAM

def shopping_cart():
    print("=" * 40)
    print(" " * 5 + "🛒  WELCOME TO SHOPPING CART 🛒")
    print("=" * 40)

    items = []
    prices = []
    quantities = []
    sub_total = []

    while True:
        # Welcome Screen
        print("-" * 40)
        print("Please select one of the following:")
        print(" " * 5 + "1. Add item")
        print(" " * 5 + "2. View cart")
        print(" " * 5 + "3. Remove item")
        print(" " * 5 + "4. Compute total")
        print(" " * 5 + "5. Quit")
        print("-" * 40)

        # PROMPT user to enter an action
        action = int(input("Please enter an action: "))

        # ADD item to cart
        if action == 1:
            # PROMPT user to enter item and price
            name = input("What item would you like to add? ").capitalize()
            number_of_items = int(input(f"How many '{name}' are there? "))
            cost = float(input(f"What is the price of '{name}'? "))

            items.append(name) # Add the item to the list
            quantities.append(number_of_items) # Add the quantity to the list
            prices.append(cost) # Add the price to the list

            sub_price = number_of_items * cost # Calculate the subtotal of the item
            sub_total.append(sub_price) # Add the subtotal to the list

            print(f"'{name}' has been added to the cart.\n")

        # VIEW cart contents
        elif action == 2:
            if len(items) > 0:
                # Display the contents of the shopping cart
                print("The contents of the shopping cart are:")
                print("-" * 46)
                print(f"{'No.':<4} {'Item':<15} {'Qty':<5} {'Price':<10} {'Subtotal':<10}")
                print("-" * 46)
                
                # Display the items in the shopping cart
                for i in range(len(items)):
                    print(f"{i + 1:<4} {items[i]:<15} {quantities[i]:<5} ${prices[i]:<10.2f} ${sub_total[i]:<10.2f}")
                print("-" * 48)
            else:
                print("\nYour shopping cart is empty! Please add some items first.")

        # REMOVE items
        elif action == 3:
            index_to_remove = int(input("Which item would you like to remove? (Enter the item number) "))
            if 1 <= index_to_remove <= len(items): # Check if the item number is valid
                index_to_remove -= 1  # Convert to zero-based index
                removed_item = items.pop(index_to_remove) # Remove the item from the list
                removed_quantity = quantities.pop(index_to_remove) # Remove the quantity from the list
                removed_price = prices.pop(index_to_remove) # Remove the price from the list
                removed_sub_total = sub_total.pop(index_to_remove) # Remove the sub_total from the list
                print(f"You removed item'{removed_item}' of quantity {removed_quantity} costing ${removed_sub_total:.2f} from the cart.")
            else:
                print(f"\nInvalid item number. You have {len(items)} items in the cart!")

        # COMPUTE total
        elif action == 4:
            if len(prices) > 0:
                total = sum(sub_total) # Calculate the total price of the items in the shopping cart
                print(f"The total price of the items in the shopping cart is ${total:.2f}")
            else:
                print("\nYour shopping cart is empty! Please add some items first.")

        # QUIT
        elif action == 5:
            print("Thank you. Goodbye!")
            break

        # INVALID option
        else:
            print("Invalid action. Please enter a number between 1 and 5.")

shopping_cart()

# END OF PROGRAM