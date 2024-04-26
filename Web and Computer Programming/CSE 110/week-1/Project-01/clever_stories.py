"""
AUTHOR: MICHAEL KAZEMBE
DATE: 26/04/2024
clever_stories.py
This program will generate a story based on user input.
The user will be prompted to enter an adjective, animal, verb, exclamation, and two more verbs.
The program will then generate a story using the user's input.

"""
# Stretch Challenge: Added three more prompts for a fruit and two adjectives
# Also added a conditional statement to check if the second adjective starts with a vowel
# Welcome Message and Instructions to the User
print("Welcome to Clever Stories! This program generates a fun story based on your input.\n")

# Get user input

print("Please enter the following information: \n")
# Prompt User For An Adjective and convert it to lowercase
adjective = input("Enter an adjective: ").lower()
# Prompt User For An Animal and convert it to lowercase
animal = input("Enter an animal: ").lower()
# Prompt User For A Verb and convert it to lowercase
verb_1 = input("Enter a verb: ").lower()
# Prompt User For An Exclamation and capitalize it
exclamation = input("Enter an exclamation: ").capitalize()
# Prompt User For Another Verb and convert it to lowercase
verb_2 = input("Enter another verb: ").lower()
# Prompt User For Another Verb and convert it to lowercase
verb_3 = input("Enter another verb: ").lower()

# Stretch Challenge
# Prompt User For A Noun and convert it to lowercase
fruit = input("Enter a fruit: ").lower()
# Prompt User For An Adjective and convert it to lowercase
adjective_2 = input("Enter an adjective: ").lower()
# Check if the adjective starts with a vowel
if adjective_2[0] in "aeiou":
    article = "An"
else:
    article = "A"


# Generate and display the story

print(f"\nThe other day, I was really in trouble. It all started when I saw a very")
print(f"{adjective} {animal} {verb_1} down the hallway. \"{exclamation}!\" I yelled. But all")
print(f"I could think to do was to {verb_2} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb_3} right in front of my family. ")
# Stretch Challenge: Add 2 new lines to the story
print(f"Let me tell you, it was a day etched in memory, when a hefty {fruit} like me")
print(f"became the star of an embarrassing show. Yes, it was {article} {adjective_2} moment!")

# End Of Program