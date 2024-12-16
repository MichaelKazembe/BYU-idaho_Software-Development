"""
AUTHOR: MICHAEL KAZEMBE
DATE: 11/12/2024

students_registration.py
A program that gets user input from a GUI, stores the data in a dictionary,
and displays the data in a GUI.
"""

import tkinter as tk
from tkinter import messagebox
import csv
import os


# Dictionary to store students
students = {}

def add_student():
    """
    Adds a student to the students dictionary.
    Retrieves the ID and name from the entry widgets and adds them to the dictionary.
    Displays a success message if the student is added, otherwise shows a warning.
    """
    # Get the ID and name from the entry widgets
    student_id = ent_id.get()
    name = ent_name.get()
    
    # Check if the ID and name are not empty
    if student_id and name:
        # Add the student to the dictionary
        students[student_id] = name
        
        # Clear the entry widgets
        ent_id.delete(0, tk.END)
        ent_name.delete(0, tk.END)
        
        # Show success message
        messagebox.showinfo("Success", f"Student {name} added.")
    else:
        # Show warning message
        messagebox.showwarning("Input Error", "Please enter both ID and name.")


def delete_student():
    """
    Deletes a student from the students dictionary.
    Retrieves the ID and name from the entry widgets and deletes the student from the dictionary.
    Displays a success message if the student is deleted, otherwise shows a warning.
    """
    # Get the ID and name from the entry widgets
    student_id = ent_id.get()
    name = ent_name.get()
    
    # Check if both ID and name are provided
    if student_id and name:
        # Check if the student exists in the dictionary
        if student_id in students and students[student_id] == name:
            # Delete the student from the dictionary
            del students[student_id]
            
            # Clear the entry widgets
            ent_id.delete(0, tk.END)
            ent_name.delete(0, tk.END)
            
            # Show success message
            messagebox.showinfo("Success", f"Student {name} with ID {student_id} deleted.")
        else:
            # Show warning message if the student is not found
            messagebox.showwarning("Input Error", "Student not found or details do not match.")
    else:
        # Show warning message if either ID or name is missing
        messagebox.showwarning("Input Error", "Please enter both ID and name.")


def view_students():
    """
    Displays all students in the students dictionary.
    Clears the text widget and inserts each student's ID and name.
    If no students are found, displays a message indicating so.
    """
    # Clear the text widget
    txt_output.delete(1.0, tk.END)
    
    # Check if there are any students
    if students:
        # Insert header
        txt_output.insert(tk.END, f"{'ID':<10}{'Name':<20}\n")
        txt_output.insert(tk.END, f"{'-'*30}\n")
        
        # Iterate over the students
        for student_id, name in students.items():
            # Insert each student's ID and name into the text widget
            txt_output.insert(tk.END, f"{student_id:<10}{name:<20}\n")
    else:
        # Show message if no students
        txt_output.insert(tk.END, "No students found.")


def clear_output():
    """
    Clears the output text widget.
    """
    txt_output.delete(1.0, tk.END)


def save_to_csv():
    """
    Saves the students dictionary to a CSV file.
    """
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the CSV file
    file_path = os.path.join(script_dir, "students.csv")
    
    # Open a file for writing
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["ID", "Name"])
        # Write the student data
        for student_id, name in students.items():
            writer.writerow([student_id, name])
            
    # Show success message
    messagebox.showinfo("Success", "Data saved to students.csv")


def load_from_csv():
    """
    Loads the students data from a CSV file into the students dictionary.
    """
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the CSV file
    file_path = os.path.join(script_dir, "students.csv")
    
    try:
        # Open the file for reading
        with open(file_path, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            
            # Clear the current students dictionary
            students.clear()
            
            # Read the student data
            for row in reader:
                student_id, name = row
                students[student_id] = name
                
        # Show success message
        messagebox.showinfo("Success", "Data loaded from students.csv")
    except FileNotFoundError:
        # Show error message if the file is not found
        messagebox.showerror("Error", "students.csv file not found")


def main():
    """
    Main function to initialize the GUI and run the application.
    """
    global ent_id, ent_name, txt_output 

    # Initialize the main window
    root = tk.Tk()
    root.title("Student Registration App")

    # Create and place the ID label
    lbl_id = tk.Label(root, text="ID:")
    lbl_id.grid(row=0, column=0, padx=10, pady=10)

    # Create and place the ID entry widget
    ent_id = tk.Entry(root)
    ent_id.grid(row=0, column=1, padx=10, pady=10)

    # Create and place the name label
    lbl_name = tk.Label(root, text="Name:")
    lbl_name.grid(row=1, column=0, padx=10, pady=10)

    # Create and place the name entry widget
    ent_name = tk.Entry(root)
    ent_name.grid(row=1, column=1, padx=10, pady=10)

    # Create and place the add button
    btn_add = tk.Button(root, text="Add Student", command=add_student)
    btn_add.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # Create and place the delete button
    btn_delete = tk.Button(root, text="Delete Student", command=delete_student)
    btn_delete.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # Create and place the view button
    btn_view = tk.Button(root, text="View Students", command=view_students)
    btn_view.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # Create and place the clear button
    btn_clear = tk.Button(root, text="Clear Output", command=clear_output)
    btn_clear.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # Create and place the save button
    btn_save = tk.Button(root, text="Save to CSV", command=save_to_csv)
    btn_save.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # Create and place the load button
    btn_load = tk.Button(root, text="Load from CSV", command=load_from_csv)
    btn_load.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    # Create and place the text widget for output
    txt_output = tk.Text(root, height=10, width=30)
    txt_output.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    # Run the main loop
    root.mainloop()
    

if __name__ == "__main__":
    main()