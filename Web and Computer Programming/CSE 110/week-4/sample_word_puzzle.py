# Introduction screen
print("Welcome to the word guessing game!\n")

# Have a secret word stored in the program.
secret_word = "banana"
    
# Display the hint
print("Your hint is: ", end="")
for i in secret_word:
    print("_", end=" ")
print("\n")
num_of_guesses = 0  # To keep track of the number of guesses

# Continue looping as long as that guess is not correct.
while True:
    # Prompt the user for a guess.
    guess = input("What is your guess? ").lower()
    num_of_guesses += 1  # Increment the number of guesses by 1 for each guess
    
    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {num_of_guesses} guesses.")
        break
    else:
        if len(guess) != len(secret_word):
            if len(guess) < len(secret_word):
                print("Your guess is too short.")
            else:
                print("Your guess is too long.")
        else:
            for letter in guess: # for each letter in the guess
                if letter not in secret_word: # if the letter is not in the secret word
                    print("_", end=" ") # print an underscore
                else:
                    i = guess.index(letter) # get the index of the letter in the guess 
                    if secret_word[i] == guess[i]:
                        print(letter.upper(), end=" ") # print the letter in uppercase
                    else:
                        print(letter.lower(), end=" ") # print the letter in lowercase

# End of program