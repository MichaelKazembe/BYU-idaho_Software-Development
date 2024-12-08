"""
Michael Kazembe / BYU-Idaho / Software Development 
CSE 111 - week 5
5/12/2024

students.py

a Python program that uses a student’s I-Number to look up the student’s name.

"""

import csv

def main():
    # The column headings and indexes.
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1
    
    try:
        # Get a filename
        filename = "students.csv"
        
        # Get Student ID from the user
        i_number = input("Enter Student's ID Number: ")
        
        # Read the contents of the file into a dictionary
        students_dict = read_dictionary(filename, I_NUMBER_INDEX)
            
        # Get the student's name from the dictionary
        student_name = students_dict[i_number][NAME_INDEX]
        
        # Display the student's name
        print(f"The student with I-Number {i_number} is {student_name}")
          
   
    except PermissionError as perm_err:
        # This code will be executed if the user enters the name
        # of a file and doesn't have permission to read that file.
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"You don't have permission to read {filename}.")
        print("Run the program again and enter the name" \
                " of a file that you are allowed to read.")
        
    except ValueError as val_err:
        # This code will be executed if the user enters the wrong value
        print()
        print(type(val_err).__name__, val_err, sep=": ")
        print(f"The student I-Number:{i_number} is invalid")
        print("Please enter a numeric I-number")
    
    except KeyError as key_err:
        # This code will be executed if the user enters the key value
        # of a dictionary that doesn't exist
        
        print()
        print(type(key_err).__name__, key_err, sep=": ")
        print(f"The student I-Number:{i_number} does not exist in the file")
        print("Run the program again and enter a valid student I-Number")

        
    except Exception as excep:
        # This code will be executed if some other type of exception occurs.
        print()
        print(type(excep).__name__, excep, sep=": ")
        


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    
    # create a dictionary to store
    students_dictionary = {}
    
    # Read from file 
    with open(filename, "rt") as students_file:
        # Create a CSV reader object
        reader = csv.reader(students_file)
        
        # Read the header row then skip it
        next(reader)
        
        # Read the remaining rows
        for row_list in reader:
            # check if the row is not empty
            if len(row_list) > key_column_index:
                # Get the value to use as the key
                key = row_list[key_column_index]
                # Store the row in the dictionary using the key
                students_dictionary[key] = row_list 
    return students_dictionary


if __name__ == '__main__':
    main()