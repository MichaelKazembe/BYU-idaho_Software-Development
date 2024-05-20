"""
AUTHOR: MICHAEL KAZEMBE
DATE: 20/05/2024

word_puzzle.py

This is a word puzzle game where the player has to guess the secret word.

"""

# Display the welcome message
print("*" * 40)
print("*{:^38}*".format("WELCOME TO THE WORD PUZZLE GAME!"))
print("*" * 40)

secret_word = "happy" 
num_of_guesses = 0 # to keep track of the number of guesses

while True:   
    guess = input("What is your guess? ").lower()
    num_of_guesses += 1 # increment the number of guesses by 1 for each guess

    if guess == secret_word:
        print("Congratulations! You guessed the secret word!")
        print(f"The secret word is {secret_word}.")
        print(f"It took you {num_of_guesses} guesses.")
        break
    else:
        print("Incorrect guess!")
        print("Try again!")
        print(f"You have guessed {num_of_guesses} times.")
        continue