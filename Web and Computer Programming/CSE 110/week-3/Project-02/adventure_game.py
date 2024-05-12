"""
AUTHOR: MICHAEL KAZEMBE
DATE: 12/05/2024

adventure_game.py

This is a text-based adventure game where you explore a dark cave 
and make choices to progress through the story.

"""

# This is a text-based adventure game where you explore a dark cave 
# and make choices to progress through the story.

# Start of Program
def start_game():
    # Introduce the Game
    print("*" * 40)
    print("*{:^38}*".format("WELCOME TO THE ADVENTURE GAME!"))
    print("*" * 40)
    print("{:^40}".format("You find yourself in a dark cave."))
    print("{:^40}".format("There are two paths ahead of you."))
    print("*" * 40)

    while True:
        choice = input("\nWhich path will you take? LEFT or RIGHT: ")
        # Handle choice regardless of upper/lower/mixed case
        choice = choice.lower()

        # Handle user choices
        if choice == "left":
            # Takes user to level 1 of the game
            level_1()
            break
        elif choice == "right":
            print("\nYou chose the right path. It was a dead end.")
        else:
            # Handle invalid user input
            print("\nInvalid choice. Please choose 'left' or 'right'.")


# LEVEL 1
def level_1():
    print("\nYou enter a room with two doors.")
    print("One door is red, and the other is blue.")

    while True:
        choice = input("\nWhich door will you choose? RED OR BLUE: ")
        # Handle choice regardless of upper/lower/mixed case
        choice = choice.lower()

        # Handle user choices
        if choice == "red":
            # Takes user to level 2 of the game
            level_2()
            break
        elif choice == "blue":
            print("\nYou chose the blue door. It leads to a treasure room!")
            print("You grab all the diamonds you can manage to carry.")
            print("\n*** Congratulations, YOU WIN! ***")
            break
        else:
            # Handle invalid user input
            print("\nInvalid choice. Please choose 'RED' or 'BLUE'.")


# LEVEL 2
def level_2():
    print("\nYou are in a room with a giant spider.")
    print("There is a sword on the ground and a door behind the spider.")

    while True:
        choice = input("\nWhat will you do? FIGHT or SNEAK): ")
        # Handle choice regardless of upper/lower/mixed case
        choice = choice.lower()

        # Handle user choices
        if choice == "fight":
            print("\nYou try to fight the spider, but it's too strong.")
            print("It uses its long jaws and fangs to spear you.")
            print("\n*** GAME OVER!!!. Better luck next time. ***")
            break
        elif choice == "sneak":
            print("\nYou sneak past the spider and through the door.")
            # Takes user to level 3 of the game
            level_3()
            break
        else:
            # Handle invalid user input
            print("\nInvalid choice. Please choose 'FIGHT' or 'SNEAK'.")


# LEVEL 3
def level_3():
    print("\nYou find yourself in a treasure room.")
    print("There are piles of gold and precious jewels everywhere.")
    print("You hear a noise behind you. You're startled!")

    while True:
        choice = input("\nWhat will you do? LOOK or LEAVE: ")
        # Handle choice regardless of upper/lower/mixed case
        choice = choice.lower()

        # Handle user choices
        if choice == "look":
            print("\nYou turn around and see a scary beast with a huge hammer")
            print("It charges towards you and squashes you with its hammer!")
            print("GAME OVER!!!. Better luck next time.")
            break
        elif choice == "leave":
            print("\nYou grab some treasure and escape the room.")
            print("\n*** Congratulations, YOU WIN!!! ***")
            break
        else:
            # Handle invalid user input
            print("\nInvalid choice. Please choose 'LOOK' or 'LEAVE'.")


# Start the game
start_game()

# End of Program
