"""
AUTHOR: MICHAEL KAZEMBE
DATE: 10/05/2024

adventure_game.py

Text-based game that takes you to various destinations based on
your choices

"""

# Level 1: Main Storyline

# scenario
print("#" * 50)
print(" MYSTERIOUS DESTINATION!")
print("You have 3 choices to pick from. For each choice")
print("you will be taken through 3 Levels")
print("#" * 50)

# Prompt user to choose an option
choice = input("Choose option (A), option (B) or option (C):" )
print(f"You chose option {choice}!")


# Choice A
if choice == "A":
    print("You are now presented with 3 Scenarios")
    print("Think Carefully before you make a choice")

    # Level 2: Story Branching
    scenario = input("Choose Scenario(1), Scenario(2), Scenario(3)")
    # Scenario 1 for choice A
    if scenario == '1':
        print("You are now into scenario 1")
        # Level 3: Destination
        deep_1 = input(" Go Deeper into next level: Choose A, B , C ")
        if deep_1 == 'A':
            print("You have reached destination 1")
        elif deep_1 == 'B':
            print("You have reached destination 2")
        else:
            print("You have reached destination 3")

    # Scenario 2 for choice B
    elif scenario == '2':
        print("You are now into scenario 1")
        # Level 3: Destination
        deep_1 = input(" Go Deeper into next level: Choose A, B , C ")
        if deep_1 == 'A':
            print("You have reached destination 4")
        elif deep_1 == 'B':
            print("You have reached destination 5")
        else:
            print("You have reached destination 6") 

    # Scenario 3 for choice B
    else:
        print("You are now into scenario 1")
        # Level 3: Destination
        deep_1 = input(" Go Deeper into next level: Choose A, B , C ")
        if deep_1 == 'A':
            print("You have reached destination 7")
        elif deep_1 == 'B':
            print("You have reached destination 8")
        else:
            print("You have reached destination 9") 

# Choice B
elif choice == "B":
    print("You are now presented with 3 Scenarios")
    print("Think Carefully before you make a choice")

    # Level 2: Story Branching
    scenario = input("Choose Scenario(1), Scenario(2), Scenario(3)")
    # Scenario 1 for choice A
    if scenario == '1':
        print("You are now into scenario 1")
        # Level 3: Destination
        deep_1 = input(" Go Deeper into next level: Choose A, B , C ")
        if deep_1 == 'A':
            print("You have reached destination 10")
        elif deep_1 == 'B':
            print("You have reached destination 11")
        else:
            print("You have reached destination 12")

    # Scenario 2 for choice B
    elif scenario == '2':
        print("You are now into scenario 1")
        # Level 3: Destination
        deep_1 = input(" Go Deeper into next level: Choose A, B , C ")
        if deep_1 == 'A':
            print("You have reached destination 13")
        elif deep_1 == 'B':
            print("You have reached destination 14")
        else:
            print("You have reached destination 15") 

    # Scenario 3 for choice B
    else:
        print("You are now into scenario 1")
        # Level 3: Destination
        deep_1 = input(" Go Deeper into next level: Choose A, B , C ")
        if deep_1 == 'A':
            print("You have reached destination 16")
        elif deep_1 == 'B':
            print("You have reached destination 17")
        else:
            print("You have reached destination 18")

# Choice C
elif choice == 'C':
    print("You are now presented with 3 Scenarios")
    print("Think Carefully before you make a choice")

    # Level 2: Story Branching
    scenario = input("Choose Scenario(1), Scenario(2), Scenario(3)")
    # Scenario 1 for choice A
    if scenario == '1':
        print("You are now into scenario 1")
        # Level 3: Destination
        deep_1 = input(" Go Deeper into next level: Choose A, B , C ")
        if deep_1 == 'A':
            print("You have reached destination 19")
        elif deep_1 == 'B':
            print("You have reached destination 20")
        else:
            print("You have reached destination 21")

    # Scenario 2 for choice B
    elif scenario == '2':
        print("You are now into scenario 1")
        # Level 3: Destination
        deep_1 = input(" Go Deeper into next level: Choose A, B , C ")
        if deep_1 == 'A':
            print("You have reached destination 22")
        elif deep_1 == 'B':
            print("You have reached destination 23")
        else:
            print("You have reached destination 24") 

    # Scenario 3 for choice B
    else:
        print("You are now into scenario 1")
        # Level 3: Destination
        deep_1 = input(" Go Deeper into next level: Choose A, B , C ")
        if deep_1 == 'A':
            print("You have reached destination 25")
        elif deep_1 == 'B':
            print("You have reached destination 26")
        else:
            print("You have reached destination 27")

else:
    print("You entered a wrong choice!")
    print("Please Restart Game")