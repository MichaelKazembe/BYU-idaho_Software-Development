"""
AUTHOR: MICHAEL KAZEMBE
DATE: 4/11/2024

tire_volume.py

This program calculates the volume of a tire based on tire width, aspect ratio, and diameter. 
It the calculates the price of a tire based on specified size ranges 
If the user chooses to buy, their phone number is saved, along with the tire specifications and volume 

"""
# START OF PROGRAM

# Import the math and datetime modules
from math import pi as PI
from datetime import datetime

# Get the width, aspect ratio, and diameter of the tire from the user
width = float(input("Enter the width of the tire in mm: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the tire in inches: "))

# Determine tire price based on input
if 175 <= width <= 195 and 45 <= aspect_ratio <= 55 and 13 <= diameter <= 15:
    price = 120  
elif 195 < width <= 215 and 55 <= aspect_ratio <= 65 and 15 <= diameter <= 17:
    price = 150  
elif 215 < width <= 245 and 45 <= aspect_ratio <= 55 and 17 <= diameter <= 18:
    price = 175  
elif 245 < width <= 275 and 65 <= aspect_ratio <= 75 and 18 <= diameter <= 20:
    price = 190 
else:
    price = "unavailable for this size"

# Calculate the volume of the tire
volume = PI * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000

# Print the volume of the tire
print(f"The approximate volume of the tire is: {volume:.2f} liters")

# Check if the price is available before prompting for purchase
if price != "unavailable for this size":
    # Print the price of the tire
    print(f"Price for the tire with given specifications is: ${price}")

    # Ask the user if they want to buy the tires with the entered dimensions
    buy = input("Would you like to buy tires with these dimensions? (yes/no): ").strip().lower()

    # Initialize phone_number as "N/A" in case the user doesn't want to buy
    phone_number = "N/A"

    # If the user wants to buy the tires, ask for their phone number
    if buy == "yes":
        phone_number = input("Please enter your phone number to complete the purchase: ")
    else:
        print("Thank you for visiting our tire store. Have a great day!")
else:
    # Set phone_number to "N/A" if user won't buy tires
    phone_number = "N/A"
    print("Sorry, we do not have tires available for the specified dimensions.")

# Get the current date
current_date = datetime.now()

# Open a text file named volumes.txt for appending
with open("volumes.txt", "a") as file: 
    # Append the current date, width, aspect ratio, diameter, volume, and phone number
    file.write(f"{current_date.strftime('%Y-%m-%d')}, {width:.0f}, {aspect_ratio:.0f}, {diameter:.0f}, {volume:.2f}, {phone_number}\n")

# Open the file in read mode to verify the contents
with open("volumes.txt", "r") as file:
    # Read the contents of the file
    contents = file.readlines()
    
    # Print the contents of the file
    print("\nContents of volumes.txt:")
    for line in contents:
        print(line.strip())

# END OF PROGRAM