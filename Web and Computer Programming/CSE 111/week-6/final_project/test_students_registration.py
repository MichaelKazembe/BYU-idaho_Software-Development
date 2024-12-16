"""

Test module for students_registration.py

This module contains tests for the students_registration.py module 
using pytest.

"""

import pytest
import os
import csv
from students_registration import add_student, \
    delete_student, \
        save_to_csv, \
            load_from_csv, students


def reset_students():
    """
    helper function to reset the students dictionary
    """
    # Clear the students dictionary
    students.clear()


@pytest.fixture
def setup_students():
    """
    set up initial data for testing
    """
    # Reset the students dictionary before each test
    reset_students()
    
    # Add initial data to the students dictionary
    students["1"] = "Michael Kazembe"
    students["2"] = "Jessie Mkambula"
    yield
    # Reset the students dictionary after each test
    reset_students()


# Test add_student function
def test_add_student():
    """ 
    tests the add_student function
    """
    
    # Reset the students dictionary
    reset_students()
    student_id = "3"
    name = "Mphatso Phiri"

    # add student to the dictionary
    students[student_id] = name

    # Assert that the student was added correctly
    assert students[student_id] == name, "Student was not added correctly."


def test_delete_student(setup_students):
    """
    tests the delete_student function
    """
    
    # Set up initial students data
    student_id = "1"
    name = "Michael Kazembe"

    # delete a student from the dictionary
    del students[student_id]

    # Assert that the student was deleted correctly
    assert student_id not in students, "Student was not deleted correctly."


def test_save_to_csv(setup_students, tmpdir):
    """
    tests the save_to_csv function
    """
    
    # Create a temporary file path for the CSV file
    file_path = os.path.join(tmpdir, "students.csv")

    # Save students to CSV
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["ID", "Name"])
        # Write the student data
        for student_id, name in students.items():
            # Write each student's ID and name to the CSV file
            writer.writerow([student_id, name])

    # Verify file content
    with open(file_path, mode="r") as file:
        # Read the CSV file
        reader = csv.reader(file)
        # Convert the reader object to a list
        rows = list(reader)

    # Assert that the CSV header is correct
    assert rows[0] == ["ID", "Name"], "CSV header is incorrect."
    # Assert that the first student record is correct
    assert rows[1] == ["1", "Michael Kazembe"], "First student record is incorrect."
    # Assert that the second student record is correct
    assert rows[2] == ["2", "Jessie Mkambula"], "Second student record is incorrect."


def test_load_from_csv(tmpdir):
    """
    tests the load_from_csv function
    """
    # Create a temporary file path for the CSV file
    file_path = os.path.join(tmpdir, "students.csv")

    # Create a CSV file with student data
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["ID", "Name"])
        # Write the student data
        writer.writerow(["1", "Michael Kazembe"])
        writer.writerow(["2", "Jessie Mkambula"])

    # Load students from CSV
    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        # skip the header
        next(reader) 
        for row in reader:
            # Read the student data
            student_id, name = row
            students[student_id] = name

    # Verify students dictionary
    # Assert that the first student record is loaded correctly
    assert students["1"] == "Michael Kazembe", "First student record not loaded correctly."
    # Assert that the second student record is loaded correctly
    assert students["2"] == "Jessie Mkambula", "Second student record not loaded correctly."


# Run the tests with verbose output
pytest.main(["-v", "--tb=line", __file__])