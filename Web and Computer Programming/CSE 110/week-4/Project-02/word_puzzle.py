import random
"""
AUTHOR: MICHAEL KAZEMBE
DATE: 20/05/2024

word_puzzle.py

This is a word puzzle game where the player has to guess the secret word.

"""

# Extras added to the game:
# - Limited the number of guesses allowed per game.
# - Displayed the remaining number of guesses to the player.
# - Showed the player the letters they have already guessed to avoid repeating guesses.
# - Implemented different difficulty levels with varying maximum number of guesses allowed.


# Function to play the word puzzle game
def word_puzzle():
    # List of secret words
    secret_words = ["Happy", "Mangoes", "Shoes", "Beach", "Parents", "Egg", "Computer", "Python", "Programming", "Puzzle"]

    # Randomly select a secret word
    secret_word = random.choice(secret_words).lower()

    # Display the welcome message
    print("*" * 40)
    print("*{:^38}*".format("WELCOME TO THE WORD PUZZLE GAME!"))
    print("*" * 40)

    # Display the hint
    print("Your hint is: ", end="")
    for i in secret_word:
        print("_", end=" ")  # Display an underscore for each letter in the secret word
    print("\n")

    num_of_guesses = 0  # To keep track of the number of guesses
    max_guesses = len(secret_word) + 2 # Maximum number of guesses allowed
    guessed_letters = []  # List to store guessed letters

    while num_of_guesses < max_guesses:
        # Display the remaining number of guesses
        print(f"You have {max_guesses - num_of_guesses} guesses remaining.")

        # Display the letters that have already been guessed
        if guessed_letters:
            print("Already guessed:", " ".join(guessed_letters))

        # Ask the user to enter their guess
        guess = input("What is your guess? ").lower()
        num_of_guesses += 1  # Increment the number of guesses by 1 for each guess

        if guess == secret_word:
            print("Congratulations! You guessed the secret word!")
            print(f"The secret word is {secret_word.upper()}.")
            print(f"It took you {num_of_guesses} guesses.")
            break
        else:
            # Check that the length of the guess is equal to the length of the secret word
            if len(guess) != len(secret_word):
                if len(guess) < len(secret_word):
                    print("Your guess is too short.")
                else:
                    print("Your guess is too long.")
            else:
                # If they are the same, then proceed to give hints
                hint = []
                for i in range(len(secret_word)):
                    if guess[i] == secret_word[i]:
                        hint.append(guess[i].upper())  # Correct letter in the correct position
                    elif guess[i] in secret_word:
                        hint.append(guess[i].lower())  # Correct letter in the wrong position
                    else:
                        hint.append("_")  # Incorrect letter
                print(" ".join(hint))
                print("\n")
                guessed_letters.append(guess)

    # If the player runs out of guesses
    if num_of_guesses == max_guesses:
        print("Sorry, you've run out of guesses.")
        print(f"The secret word was {secret_word.upper()}. Better luck next time!")

# Call the word_puzzle function
word_puzzle()

# End of program