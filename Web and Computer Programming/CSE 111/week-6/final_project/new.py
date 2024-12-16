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
    student_id = ent_id.get()
    name = ent_name.get()
    if student_id and name:
        students[student_id] = name
        ent_id.delete(0, tk.END)
        ent_name.delete(0, tk.END)
        messagebox.showinfo("Success", f"Student {name} added.")
    else:
        messagebox.showwarning("Input Error", "Please enter both ID and name.")

def delete_student():
    student_id = ent_id.get()
    name = ent_name.get()
    if student_id and name:
        if student_id in students and students[student_id] == name:
            del students[student_id]
            ent_id.delete(0, tk.END)
            ent_name.delete(0, tk.END)
            messagebox.showinfo("Success", f"Student {name} with ID {student_id} deleted.")
        else:
            messagebox.showwarning("Input Error", "Student not found or details do not match.")
    else:
        messagebox.showwarning("Input Error", "Please enter both ID and name.")

def view_students():
    txt_output.delete(1.0, tk.END)
    if students:
        txt_output.insert(tk.END, f"{'ID':<10}{'Name':<20}\n")
        txt_output.insert(tk.END, f"{'-'*30}\n")
        for student_id, name in students.items():
            txt_output.insert(tk.END, f"{student_id:<10}{name:<20}\n")
    else:
        txt_output.insert(tk.END, "No students found.")

def clear_output():
    txt_output.delete(1.0, tk.END)

def save_to_csv():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "students.csv")
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name"])
        for student_id, name in students.items():
            writer.writerow([student_id, name])
    messagebox.showinfo("Success", "Data saved to students.csv")

def load_from_csv():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "students.csv")
    try:
        with open(file_path, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            students.clear()
            for row in reader:
                student_id, name = row
                students[student_id] = name
        messagebox.showinfo("Success", "Data loaded from students.csv")
    except FileNotFoundError:
        messagebox.showerror("Error", "students.csv file not found")

def search_student():
    search_query = ent_search.get()
    txt_output.delete(1.0, tk.END)
    found = False
    for student_id, name in students.items():
        if search_query == student_id or search_query.lower() in name.lower():
            txt_output.insert(tk.END, f"{'ID':<10}{'Name':<20}\n")
            txt_output.insert(tk.END, f"{'-'*30}\n")
            txt_output.insert(tk.END, f"{student_id:<10}{name:<20}\n")
            found = True
            break
    if not found:
        txt_output.insert(tk.END, "No matching student found.")

def main():
    global ent_id, ent_name, txt_output, ent_search
    root = tk.Tk()
    root.title("Student Registration App")
    root.configure(bg="#f0f0f5")

    lbl_title = tk.Label(root, text="Student Registration App", font=("Arial", 16), bg="#f0f0f5")
    lbl_title.grid(row=0, column=0, columnspan=2, pady=10)

    lbl_id = tk.Label(root, text="ID:", bg="#f0f0f5")
    lbl_id.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    ent_id = tk.Entry(root)
    ent_id.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    lbl_name = tk.Label(root, text="Name:", bg="#f0f0f5")
    lbl_name.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    ent_name = tk.Entry(root)
    ent_name.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    btn_add = tk.Button(root, text="Add Student", command=add_student, bg="#4CAF50", fg="white")
    btn_add.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    btn_delete = tk.Button(root, text="Delete Student", command=delete_student, bg="#f44336", fg="white")
    btn_delete.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    btn_view = tk.Button(root, text="View Students", command=view_students, bg="#2196F3", fg="white")
    btn_view.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    btn_clear = tk.Button(root, text="Clear Output", command=clear_output, bg="#FFC107")
    btn_clear.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    btn_save = tk.Button(root, text="Save to CSV", command=save_to_csv, bg="#9C27B0", fg="white")
    btn_save.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    btn_load = tk.Button(root, text="Load from CSV", command=load_from_csv, bg="#673AB7", fg="white")
    btn_load.grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    lbl_search = tk.Label(root, text="Search by ID/Name:", bg="#f0f0f5")
    lbl_search.grid(row=9, column=0, padx=10, pady=5, sticky="w")
    ent_search = tk.Entry(root)
    ent_search.grid(row=9, column=1, padx=10, pady=5, sticky="w")

    btn_search = tk.Button(root, text="Search", command=search_student, bg="#3F51B5", fg="white")
    btn_search.grid(row=10, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    txt_output = tk.Text(root, height=10, width=50)
    txt_output.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
