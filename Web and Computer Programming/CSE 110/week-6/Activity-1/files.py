"""
AUTHOR: MICHAEL KAZEMBE
DATE: 27/05/2024

files.py

A program that opens and reads files then parsing strings in python

"""

import os
if os.path.exists("books.txt"):
    with open("books.txt") as file:
        for line in file:
            books = line.strip()
            print(books)
else:
    print("File not found!")
