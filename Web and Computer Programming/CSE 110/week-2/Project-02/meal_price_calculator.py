"""
AUTHOR: MICHAEL KAZEMBE

meal_price_calculator.py

This program calculates the total cost of a meal at a restaurant.
"""

# For Creativity, I will add a welcome message to the program
# I will ask for extra items such as drinks and desserts
# I will ask for the tip percentage
# I will display the summary of the transaction
# I will display a goodbye message



# Welcome message
print("\n*** Welcome to the Meal Price Calculator! ***\n")

# Prompt the user for details about the meal
print("Please enter the following information: \n")

# Get the cost of the meal
child_meal = float(input("Cost of child's meal: "))
adult_meal = float(input("Cost of adult's meal: "))

# Get Number of children and adults
children_num = int(input("Number of children: "))
adults_num = int(input("Number of adults: "))

# Meals total
meals_total = (child_meal * children_num) + (adult_meal * adults_num)

# Display the total cost of the meals
print(f"\nTotal cost of meals: ${meals_total:.2f} \n")

print(" *** Extra Items *** \n")

# Prompt the user for extra items
drink = float(input("Cost of drinks: "))
drink_num = int(input("Number of drinks: "))
dessert = float(input("Cost of desserts: "))
dessert_num = int(input("Number of desserts: "))


# Extra items total
extra_items_total = (drink * drink_num) + (dessert * dessert_num)

# Calculate the subtotal
meals_subtotal = meals_total + extra_items_total

# display the subtotal
print(f"\nSubtotal: ${meals_subtotal:.2f} \n")

# Prompt the user for the sales tax rate
sales_tax_rate = float(input("Sales tax rate (e.g., 5% or 6.5%): "))   

# Calculate the sales tax
sales_tax = meals_subtotal * (sales_tax_rate / 100)

# Calculate the total price of the meal
total_price = meals_subtotal + sales_tax

# Display the total price of the meal
print(f"Total Price: ${total_price:.2f}")

# Prompt the user for the payment amount
payment = float(input("Payment amount: "))

# Prompt the user for tip percentage
tip_percentage = float(input("Tip percentage (e.g., 5% or 10%): "))

# Calculate tip
tip = total_price * (tip_percentage / 100)

# Display the tip
print(f"Tip: ${tip:.2f}")

# Calculate the change
change = payment - (total_price + tip)

# Display the change
print(f"Change: ${change:.2f}")

# Display summary of the transaction

print("\n *** Summary *** \n")
print(f"Total cost of meals: ${meals_total:.2f}")
print(f"Total cost of extra items: ${extra_items_total:.2f}")
print(f"Subtotal: ${meals_subtotal:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Total price: ${total_price:.2f}")
print(f"Payment: ${payment:.2f}")
print(f"Change: ${change:.2f} \n")

# Display a goodbye message
print("*** Thank you for using the Meal Price Calculator! ***")

# End of Program