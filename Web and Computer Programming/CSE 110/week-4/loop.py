import random

guess = int(input("Guess any number between 1 and 10"))
magic_num = random.randint(1, 10)
if magic_num > guess:
    print('Guess higher')
if magic_num < guess:
    print('guess lower')