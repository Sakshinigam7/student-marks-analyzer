"""
Student Marks Analyzer 

Author: Sakshi Nigam
Version: 1.0.0

Description:
A beginner-friendly NumPy project for analyzing
student performance using statistical operations.
"""
import numpy as np


def main():
    """
    Main entry point of the Student Marks Analyzer project.

    Creates sample student data including roll numbers,
    student names, and student marks, then displays the dataset
    and basic information about the marks array.
    """

    # create an array of student roll_numbers
    roll_numbers = np.arange(101, 111)
    

    # Creating an array of student names.
    names = np.array([
        "Sakshi",
        "Aman",
        "Priya",
        "Rahul",
        "Anjali",
        "Arjun",
        "Yash",
        "Karan",
        "Neha",
        "Riya"
    ])
    
    

    subjects = np.array([
        "maths",
        "physics",
        "chemistry",
        "english",
        "computer"
    ])
    

    # Subject order:
    # Maths, Physics, Chemistry, English, Computer
    marks = np.array([
        [95, 91, 88, 93, 97],  # Sakshi
        [82, 76, 85, 80, 79],  # Aman
        [91, 94, 89, 95, 92],  # Priya
        [68, 72, 70, 66, 74],  # Rahul
        [98, 96, 97, 99, 100], # Anjali
        [78, 81, 76, 83, 80],  # Arjun
        [87, 89, 91, 88, 90],  # Yash
        [73, 69, 75, 71, 72],  # Karan
        [64, 67, 65, 70, 68],  # Neha
        [93, 90, 94, 92, 95]   # Riya
    ])
    

    display_dataset_info(marks)
    display_student_dataset(roll_numbers,names,marks,subjects)
    explore_dataset(names,marks)
    calculate_total_marks(marks)

    

def display_dataset_info(marks: np.ndarray) -> None:
    """
    Display basic information about the marks array.

    Parameters:
        marks (numpy.ndarray): A 2D NumPy array containing
        student marks for all subjects.

    Displays:
        - Shape
        - Number of dimensions
        - Data type
        - Total number of elements
    """
    # printing marks shape, dimension, datatype, size(number of items)
    print(f"Shape of marks: {marks.shape}")
    print(f"Dimension of marks: {marks.ndim}D")
    print(f"DataType of marks: {marks.dtype}")
    print(f"Size of marks: {marks.size}")

def display_student_dataset(
    roll_numbers: np.ndarray,
    names: np.ndarray,
    subjects: np.ndarray,
    marks: np.ndarray
) -> None:
    """
    Display the complete student dataset.

    Parameters:
    roll_numbers (numpy.ndarray):
        A 1D array containing the roll numbers of all students.

    names (numpy.ndarray):
        A 1D array containing the names of all students.

    marks (numpy.ndarray):
        A 2D array containing the marks of all students.

    subjects (numpy.ndarray):
        A 1D array containing the all the subjects.    

    Displays:
    - Roll numbers
    - Student names
    - Marks matrix
    - Subject names
    """
    print("========== STUDENT DATA ==========")
    print(f"Roll Numbers: {roll_numbers}")
    print(f"Student Names: {names}")
    print(f"subjects: \n{subjects}")
    print(f"Student Marks:\n{marks}")
    

def explore_dataset(
    names: np.ndarray,
    marks: np.ndarray
    
) -> None:
    """
    Explore the student dataset by displaying basic information.

    Parameters:
    names (numpy.ndarray):
        A 1D array containing the names of all students.

    marks (numpy.ndarray):
        A 2D array containing the marks of all students.

    Displays:
    - Total number of students
    - Total number of subjects
    - First student's name and marks
    - Last student's name and marks
    """
    print("\n========== DATASET OVERVIEW ==========\n")
    print(f"TOTAL STUDENTS: {names.size}")
    print(f"TOTAL SUBJECTS: {marks.shape[1]}\n")

    print("FIRST STUDENT: {names[0]}")
    print("MARKS: {marks[0]}\n")

    print("LAST STUDENT: {names[-1]}")
    print("MARKS: {marks[-1]}\n")



def calculate_total_marks(
    marks: np.ndarray
): 
    """
    Calculate the total marks obtained by each student.

    Parameters: 
        marks: A 2D NumPy array where each row represents
               a student's marks in all subjects.

    Returns:
        A 1D NumPy array containing the total marks of each student.
    """

    marks.sum(axis=1)




if __name__ == "__main__":
    main()
   