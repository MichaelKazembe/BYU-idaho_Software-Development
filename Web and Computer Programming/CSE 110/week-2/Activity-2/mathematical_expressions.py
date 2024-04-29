"""
AUTHOR: MICHAEL KAZEMBE

mathematical_expressions.py

Program that converts from Fahrenheit to Celsius
Display the result to one decimal place precision

"""

# Prompt user to enter temperature in Fahrenheit and cast it into any an integer
fahrenheit = int(input("What is the temperature in Fahrenheit?\n"))
# Convert from Fahrenheit to Celsius 
celsius = (fahrenheit - 32) * (5/9)

print(f"The temperature in Celsius is {celsius:.1f} degrees")

