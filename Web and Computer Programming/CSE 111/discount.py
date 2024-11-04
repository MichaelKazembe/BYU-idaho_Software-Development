"""
AUTHOR: MICHAEL KAZEMBE
DATE: 4/11/2024

discount.py

A program that calculates subtotal of a product then computes the discount, sales tax and total 

"""

# START OF PROGRAM

from datetime import datetime

# Get the current day of the week from the computer's operating system
day = datetime.now().weekday()
subtotal = 0

while True:
    price = float(input("Enter the price: "))
    if price == 0:
        break
    else:
        quantity = int(input("Enter the quantity: "))
        subtotal += price * quantity

        print(f"Subtotal: ${subtotal:.2f}")

        if subtotal >= 50 and (day == 0 or day == 1):
            discount = subtotal * 0.01
            subtotal -= discount 
            sales_tax = subtotal * 0.06
            total = subtotal + sales_tax
             
            # Print the discount, sales tax and total    
            print(f"Discount ${discount:.2f}")
            print(f"Sales tax ${sales_tax:.2f}")
            print(f"Total ${total:.2f}")
                
        else:
            additional_amount = 50 - subtotal
            print(f"Additional amount needed to receive discount: ${additional_amount:.2f}")
            

# EOP

    

