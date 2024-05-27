"""
AUTHOR: MICHAEL KAZEMBE
DATE: 27/05/2024

data.py

A program that finds the youngest person in the list
"""

# List of people
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngest_age = 100
youngest_name = ""

# Iterate through the list of people using indexes
for i in range(len(people)):
    # Split the string into name and age
    person = people[i].split()
    name = person[0]
    age = int(person[1])
    
    # Print the name and age
    print(f"Name: {name}, Age: {age}")

    # Check if the age is less than the youngest age
    if age < youngest_age:
        youngest_age = age
        youngest_name = name

print(f"The youngest person is {youngest_name} with age {youngest_age}")
