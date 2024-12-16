"""
AUTHOR: MICHAEL KAZEMBE
DATE: 16/12/2024

test_students_registration.py
Unit tests for the students registration application.
"""

import pytest
import csv
import os
from students_registration import add_student, delete_student, save_to_csv, load_from_csv, students, view_students, clear_output

@pytest.fixture(autouse=True)
def run_around_tests():
    """
    Fixture to run before and after each test.
    Clears the students dictionary before each test and removes the test CSV file after each test.
    """
    # Clear the students dictionary before each test
    students.clear()
    yield
    # Remove the test CSV file after each test
    if os.path.exists("test_students.csv"):
        os.remove("test_students.csv")

def test_add_student():
    """
    Tests whether the add_student function correctly adds a student.
    """
    # Add a student to the dictionary
    assert add_student("1", "Michael Kazembe")
    # Check if the student ID is in the dictionary
    assert "1" in students
    # Check if the student name is correct
    assert students["1"] == "Michael Kazembe"

def test_delete_student():
    """
    Tests whether the delete_student function correctly removes a student.
    """
    # Add a student to the dictionary
    students["1"] = "Michael Kazembe"
    # Delete the student from the dictionary
    assert delete_student("1", "Michael Kazembe")
    # Check if the student ID is not in the dictionary
    assert "1" not in students

def test_save_to_csv():
    """
    Tests whether the save_to_csv function writes the data correctly to a file.
    """
    # Add a student to the dictionary
    students["1"] = "Michael Kazembe"
    # Save the students dictionary to a CSV file
    file_path = save_to_csv()
    # Check if the CSV file exists
    assert os.path.exists(file_path)
    # Open the CSV file for reading
    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        # Read the header row
        header = next(reader)
        # Read the data row
        data = next(reader)
        # Check if the header is correct
        assert header == ["ID", "Name"]
        # Check if the data is correct
        assert data == ["1", "Michael Kazembe"]

def test_load_from_csv():
    """
    Tests whether the load_from_csv function reads and loads the data correctly.
    """
    # Create a CSV file with test data
    with open("test_students.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name"])
        writer.writerow(["1", "Michael Kazembe"])
    # Load the data from the CSV file into the students dictionary
    assert load_from_csv()
    # Check if the student ID is in the dictionary
    assert "1" in students
    # Check if the student name is correct
    assert students["1"] == "Michael Kazembe"

def test_view_students():
    """
    Tests whether the view_students function displays the students correctly.
    """
    # Add a student to the dictionary
    students["1"] = "Michael Kazembe"
    # Get the string representation of the students dictionary
    output = view_students()
    # Check if the student ID is in the output
    assert "1" in output
    # Check if the student name is in the output
    assert "Michael Kazembe" in output

def test_clear_output():
    """
    Tests whether the clear_output function clears the students dictionary correctly.
    """
    # Add a student to the dictionary
    students["1"] = "Michael Kazembe"
    # Clear the students dictionary
    clear_output()
    # Check if the students dictionary is empty
    assert not students

# Run the tests with verbose output and a line-by-line traceback
pytest.main(["-v", "--tb=line", __file__])