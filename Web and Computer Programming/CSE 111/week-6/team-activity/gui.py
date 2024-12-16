"""
AUTHOR: MICHAEL KAZEMBE
DATE: 11/12/2024

gui.py

A program that gets user input from a GUI, performs a simple calculation, 
and displays the result in a GUI.

"""

import tkinter as tk  # Import the tkinter module for GUI
from tkinter import messagebox  # Import messagebox for showing messages
import csv  # Import csv module for reading and writing CSV files

# Dictionary to store students
students = {}

# Function to add a student
def add_student(data):
    student_id = data.get("id")
    name = data.get("name")
    if student_id and name:
        students[student_id] = name
        messagebox.showinfo("Success", f"Student {name} added.")
    else:
        messagebox.showwarning("Input Error", "Please enter both ID and name.")

# Function to delete a student
def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        messagebox.showinfo("Success", f"Student {student_id} deleted.")
    else:
        messagebox.showwarning("Input Error", "Student not found.")

# Function to view all students
def view_students():
    return students

# Function to search for a student
def search_student(search_term):
    results = {student_id: name for student_id, name in students.items() if search_term in student_id or search_term in name}
    return results

# Function to save students to a CSV file
def save_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name"])
        for student_id, name in data.items():
            writer.writerow([student_id, name])
    messagebox.showinfo("Success", f"Data saved to {filename}")

# Function to load students from a CSV file
def load_from_csv(filename):
    global students
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        students = {rows[0]: rows[1] for rows in reader}
    messagebox.showinfo("Success", f"Data loaded from {filename}")

# Function to clear the output text widget
def clear_output():
    output_text.delete(1.0, tk.END)

def main():
    global name_entry, id_entry, output_text  # Declare global variables

    # Initialize the main window
    root = tk.Tk()
    root.title("Student Registration App")

    # Create and place the ID label
    id_label = tk.Label(root, text="ID:")
    id_label.grid(row=0, column=0)

    # Create and place the ID entry widget
    id_entry = tk.Entry(root)
    id_entry.grid(row=0, column=1)

    # Create and place the name label
    name_label = tk.Label(root, text="Name:")
    name_label.grid(row=1, column=0)

    # Create and place the name entry widget
    name_entry = tk.Entry(root)
    name_entry.grid(row=1, column=1)

    # Create and place the add button
    add_button = tk.Button(root, text="Add Student", command=lambda: add_student({"id": id_entry.get(), "name": name_entry.get()}))
    add_button.grid(row=2, column=0, columnspan=2)

    # Create and place the delete button
    delete_button = tk.Button(root, text="Delete Student", command=lambda: delete_student(id_entry.get()))
    delete_button.grid(row=3, column=0, columnspan=2)

    # Create and place the view button
    view_button = tk.Button(root, text="View Students", command=lambda: output_text.insert(tk.END, f"{view_students()}\n"))
    view_button.grid(row=4, column=0, columnspan=2)

    # Create and place the search button
    search_button = tk.Button(root, text="Search Student", command=lambda: output_text.insert(tk.END, f"{search_student(name_entry.get())}\n"))
    search_button.grid(row=5, column=0, columnspan=2)

    # Create and place the save button
    save_button = tk.Button(root, text="Save to CSV", command=lambda: save_to_csv("students.csv", students))
    save_button.grid(row=6, column=0, columnspan=2)

    # Create and place the load button
    load_button = tk.Button(root, text="Load from CSV", command=lambda: load_from_csv("students.csv"))
    load_button.grid(row=7, column=0, columnspan=2)

    # Create and place the clear button
    clear_button = tk.Button(root, text="Clear Output", command=clear_output)
    clear_button.grid(row=8, column=0, columnspan=2)

    # Create and place the text widget for output
    output_text = tk.Text(root, height=10, width=30)
    output_text.grid(row=9, column=0, columnspan=2)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()