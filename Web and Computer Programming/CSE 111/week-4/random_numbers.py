"""
AUTHOR: MICHAEL KAZEMBE
DATE: 26/11/2024

test_random_numbers.py

Program that creates a list of numbers and words and 
appends random numbers and words to the list respectively.

"""
# Import the random module
import random

def main():
    print("Random Numbers Program\n")
    # Create list named numbers
    numbers = [16.2, 75.1, 52.3]
    # Print the list
    print(numbers)
    
    
    # call append_random_numbers function with 
    # only one argument to add one number to numbers
    append_random_numbers(numbers)
    
    # Print the numbers list
    print(f"Initial Number list: {numbers}")
    
    # Prompt the user to enter the number of random words
    # to add to the list.
    quantity = int(input("Enter the number of random numbers to add: "))
    
    # Calls the append_random_numbers function again 
    # with two arguments to add three numbers to numbers
    append_random_numbers(numbers, quantity)
    
    # Print the numbers list
    print(f"List of random {quantity} words:{numbers}")
    
    print("\n...End of Random Numbers Program\n")
    
    print("Random Words Program\n")
    # Create a list named words
    words = []
    
    # call append_random_words function with
    # only one argument to add one word to words
    append_random_words(words)
    # Print the words list
    print(f"Initial List of Words: {words}")
    
    # Prompt the user to enter the number of random words
    # to add to the list.
    quantity = int(input("Enter the number of random words to add: "))
    
    # Call the append_random_words function again
    # with two arguments to add three words to words
    append_random_words(words, quantity)
    # Print the words list
    print(f"List of random {quantity} words:{words}")
    
    print("\n...End of Random Words Program\n")
    

def append_random_numbers(numbers_list, quantity=1):
    """
    Appends random numbers to the numbers_list list.
    parameters:
        numbers_list: list of numbers
        quantity: number of random numbers to append
    returns:
        none
    """
    
    # Computes quantity pseudo random numbers by calling 
    # the random.uniform function.
    for i in range(quantity):
        # Generate a random number between 0 and 100
        # using the random.uniform function
        random_number = random.uniform(0, 100)
        # Round the random number to one decimal place
        random_number = round(random_number, 1)
        # Append the random number to the numbers_list list
        numbers_list.append(random_number)     
        

def append_random_words(words_list, quantity=1):
    """ 
    Randomly selects quantity words from a list of words 
    and appends the selected words at the end of words_list.
    parameters:
        words_list: list of words
        quantity: number of random words to append
    returns:
        none
    """
    
    # Create a list of words named words
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"
        "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "pear",
        "quince", "raspberry", "strawberry", "tangerine", "watermelon",
        "apricot", "blackberry", "cantaloupe", "dragonfruit", "eggplant"
    ]
    
    # Select a random word from the words list
    random_word = random.choice(words)
    
    for i in range(quantity):
        # Append the random word to the words_list list
        words_list.append(random_word)
    

# Call the main function
if __name__ == "__main__":
    main()