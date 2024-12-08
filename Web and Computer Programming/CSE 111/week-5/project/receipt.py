"""
Michael Kazembe / BYU-Idaho / Software Development 
CSE 111 - week 5: Project
8/12/2024

receipt.py 

A program that reads the contents of a CSV file 
into a compound dictionary, reads the request.csv file, 
and prints a receipt for the requested products.

"""

import csv
from datetime import datetime, timedelta


def main():
    try:
        # Calls the read_dictionary function and stores the compound dictionary in a variable named products_dict.
        products_dict = read_dictionary("products.csv", 0)
        print()

        # Reads requested products
        order = read_request(products_dict)
        
        # Prints receipt
        print_receipt(order)
        
    except FileNotFoundError as file_err:
        print(f"File not found: {file_err.filename}")
        
    except PermissionError as perm_err:
        print(f"Permission denied: {perm_err.filename}")
        
    except KeyError as key_err:
        print(f"Error: unknown product ID in the request.csv file")
        print(f"{key_err}")  


def read_request(products_dict):
    """
    Read the request.csv file and return requested products 
    as a list of tuples.
    Parameters:
        products_dict: a dictionary that contains the product 
            details read from the products.csv file.
    Return:
        a list that contain the name, quantity, and
            price of each requested product.
    """
    requested_products = []

    # Opens the request.csv file for reading
    with open("request.csv", "r") as file:
        # Creates a CSV reader object
        reader = csv.reader(file)

        # Skips the first line of the request.csv file because it contains column headings
        next(reader)

        # Reads and processes each row from the request.csv file
        for row_list in reader:
            # Get product details
            product_number = row_list[0]  # Product number
            quantity = int(row_list[1])  # Requested quantity

            # Attempt to get product details, which may raise KeyError
            product = products_dict[product_number]

            # Append to the requested_products list
            requested_products.append((product[1], quantity, float(product[2])))

    return requested_products


def read_dictionary(filename, key_column_index):
    """
    Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: 
        a compound dictionary that contains the 
            contents of the CSV file.
    """
    # Create an empty dictionary
    compound_dict = {}

    # Open the file for reading
    with open(filename, "r") as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        # Skip the first line of the file
        next(reader)

        # Iterate over the rows in the file
        for row_list in reader:
            # Check if the row is not empty
            if len(row_list) > 0:
                # Get the key from the row
                key = row_list[key_column_index]
                # Add the row to the dictionary
                compound_dict[key] = row_list

    # Return the dictionary
    return compound_dict


def get_current_date():
    """
    Get the current date and time.
    parameters: 
        None
    Return: 
        a string that contains the current date and time
    """
    now = datetime.now()

    # Format the date to be more readable
    formatted_date = now.strftime("%a %b %d %H:%M:%S %Y")

    # Return the formatted date
    return formatted_date


def remind_new_years_sale():
    """
    Reminds the user how many days are left until the New Year's Sale on January 1st, 2025.
    """
    current_date = datetime.now()
    new_years_date = datetime(2025, 1, 1)
    
    days_left = (new_years_date - current_date).days
    
    print(f"🎉 NEW YEAR'S SALE 🎉 in 🎇 {days_left} DAYS! 🎇")


def return_product_by_date():
    """
    print a "return by" date that is 9:00 PM 
    30 days in the future at the bottom of the receipt.
    parameters: 
        None
    return:
        None
    """
    future_days = 30
    current_date = datetime.now()
    # Set the time to 9:00 PM
    current_date = current_date.replace(hour=21, minute=0, second=0)
    
    # Calculate the return date
    return_date =  current_date + timedelta(days=future_days)
    
    print(f"Return by: {return_date.strftime('%a %b %d %H:%M:%S %Y')}")


def print_receipt(order):
    """
    Print a receipt for the requested products.
    Parameters:
        order: a list of tuples that contain the
            name, quantity, and price of each product.
    return: None
    """
    print("-" * 40)
    print("Inkom Emporium")
    print("Receipt")
    print("-" * 40)

    total_items = 0
    sub_total = 0.0
    sales_tax = 0.06
    for name, quantity, price in order: 
        line_total = quantity * price
        sub_total += line_total
        total_items += quantity 
        print(f"{name}: {quantity} @ ${price:.2f} = ${line_total:.2f}")
       
    total_tax = sub_total * sales_tax
    total_cost = sub_total + total_tax
    
    print("-" * 40)
    print(f"Total Items: {total_items}")
    print(f"Subtotal: ${sub_total:.2f}")
    print(f"Sales Tax: ${total_tax:.2f}")
    print(f"Total: ${total_cost:.2f}")
    print("-" * 40)
    print()
    print("*** Thank you for shopping at Inkom Emporium! ***")
    print(get_current_date())
    print()
    remind_new_years_sale()
    print()
    print("+" * 40)
    return_product_by_date()
    print("+" * 40)
    print()


if __name__ == "__main__":
    main()
