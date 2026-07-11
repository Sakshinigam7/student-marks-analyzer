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
        "Jitesh",
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
        [98, 96, 97, 99, 100], # Jitesh
        [78, 81, 76, 83, 80],  # Arjun
        [87, 89, 91, 88, 90],  # Yash
        [73, 69, 75, 71, 72],  # Karan
        [64, 67, 65, 70, 68],  # Neha
        [93, 90, 94, 92, 95]   # Riya
    ])
    

    # Display basic information about the marks dataset.
    display_dataset_info(marks)
    # Display the complete student dataset.
    display_student_dataset(roll_numbers,names,subjects,marks)
    # Display a summary of the dataset.
    explore_dataset(names,marks)
    # Calculate and display total marks for every student.
    calculate_total_marks(marks,names)
    # Search and display marks of a particular student.
    show_student_marks(marks,names,"sakshi".capitalize())
    # Display marks of a particular subject for all the students.
    show_subject_marks(marks,subjects,names,"physics".lower())
    # Display the marks obtained by a specific student in a specific subject.
    show_student_subject_marks(names,subjects,marks,"Jitesh","maths")
    # Display the marks of a range of students.
    show_consecutive_students(names,marks,"Aman","Neha")
    # Display the marks of all students for a selected range of subjects.
    show_subjects_range(subjects,names,marks,"maths","chemistry")
    # Display the marks of a consecutive range of students for a consecutive range of subjects.
    show_consecutive_student_subject_marks(names,subjects,marks,"Priya","Yash","physics","english")
    # Display statistical information for a specific student.
    show_student_statistics(names,marks,"Sakshi")
    # Display statistical information for a specific subject.
    show_subject_statistics(subjects,marks,"english")
    # Display overall statistical information for the entire class.
    show_class_statistics(names,subjects,marks)
    # Display the ranking of all students based on their total marks.
    show_student_ranking(names,marks)
    # Display the topper and the weakest-scoring student based on total marks.
    show_topper_weakest_student(names,marks)
    
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
    print("\n====== MARKS DETAILS ======\n")
    # printing marks shape, dimension, datatype, size(number of items)
    print(f"Shape     : {marks.shape}")
    print(f"Dimension : {marks.ndim}")
    print(f"DataType  : {marks.dtype}")
    print(f"Size      : {marks.size}")


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
    #Display roll_numbers,names,subjects and marks of all students
    print("\n========== STUDENT DATA ==========\n")
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
    ## Display total number of students and subjects.
    print("\n========== DATASET OVERVIEW ==========\n")
    print(f"TOTAL STUDENTS: {names.shape[0]}")
    print(f"TOTAL SUBJECTS: {marks.shape[1]}\n")

    # Display details of the first student.
    print(f"FIRST STUDENT: {names[0]}")
    print(f"MARKS: {marks[0]}\n")

    # Display details of the last student.
    print(f"LAST STUDENT: {names[-1]}")
    print(f"MARKS: {marks[-1]}\n")


def calculate_total_marks(
    marks: np.ndarray,
    names: np.ndarray,
    display: bool = True
) -> np.ndarray:
    """
    Calculate and display the total marks obtained by each student.

    Parameters:
    marks (numpy.ndarray):
        A 2D NumPy array where each row contains
        the marks of one student in all subjects.

    names (numpy.ndarray):
        A 1D NumPy array containing the names
        of all students.

    Returns:
    numpy.ndarray:
        A 1D NumPy array containing the total marks
        obtained by each student.

    Displays:
    - Total marks of every student.
    """
    # Calculate the total marks of each student.      
    total_marks = marks.sum(axis=1)

    # If display is true.
    if display:
        print("\n========== TOTAL MARKS ==========\n")

        # Display the total marks of every student.
        for i in range(len(names)):
            print(f"{names[i]:<10} : {total_marks[i]}")

    return total_marks
    

def show_student_marks(
    marks: np.ndarray,
    names: np.ndarray,
    student_name: str

) -> None:
    """
    Display the marks of a student by searching for their name.

    Parameters:
    names (numpy.ndarray):
        A 1D NumPy array containing the names of all students.

    marks (numpy.ndarray):
        A 2D NumPy array containing the marks of all students.

    student_name (str):
        The name of the student whose marks are to be displayed.

    Displays:
    - Student name
    - Marks obtained in all subjects

    If the student name does not exist in the dataset, an error message is displayed.
    """
    print("\n========== STUDENT MARKS ==========\n")
    
    #Check whether the student exists in the dataset.
    if student_name in names:
        #finding the index of student_name
        index = np.where(student_name == names)[0][0]

        #using index for getting marks_of_student
        print("\n====== STUDENT FOUND ======\n")
        print(f"name of student: {names[index]}\n")
        print(f"marks: {marks[index]}")

    #if student_name not found then:
    else:
        print("\n====INVALID STUDENT====")


def show_subject_marks(
    marks: np.ndarray,
    subjects: np.ndarray,
    names: np.ndarray,
    subject_name: str

) -> None:
    """
    Display the marks obtained by all students in a specified subject.

    Parameters:
    marks (numpy.ndarray):
        A 2D NumPy array containing the marks of all students
        in all subjects.

    subjects (numpy.ndarray):
        A 1D NumPy array containing the names of all subjects.

    names (numpy.ndarray):
        A 1D NumPy array containing the names of all students.

    subject_name (str):
        The name of the subject whose marks are to be displayed.

    Displays:
    - The subject name.
    - The marks obtained by every student in the specified subject.

    If the subject does not exist in the dataset,
    an appropriate error message is displayed.
    """

    print("\n========== SUBJECT MARKS ==========\n")
    
    #Check whether the subject exists in the dataset.
    if subject_name in subjects:
        # Find the column index of the selected subject.
        subject_index = np.where(subject_name == subjects)[0][0]
        print("====SUBJECT FOUND====")
        print(f"subject: {subject_name}\n")
        
        for i in range(marks.shape[0]):
            print(f"{names[i]:<10} : {marks[i,subject_index]}")

    else:
        print("====INVALID SUBJECT====")


def show_student_subject_marks(
    names: np.ndarray,
    subjects: np.ndarray,
    marks: np.ndarray,
    student_name: str,
    subject_name: str

) -> None:
    """
    Display the marks obtained by a specific student in a specific subject.

    Parameters:
    names (numpy.ndarray):
        A 1D NumPy array containing the names of all students.

    subjects (numpy.ndarray):
        A 1D NumPy array containing the subject names.

    marks (numpy.ndarray):
        A 2D NumPy array containing the marks of all students.

    name_of_student (str):
        The name of the student.

    subject_name (str):
        The name of the subject.

    Displays:
    - Student name
    - Subject name
    - Marks obtained in the selected subject

    If the student or subject does not exist in the dataset, an error message is displayed.
    """

    print("\n========== STUDENT SUBJECT MARK ==========\n")
    # Check whether the student exists.
    if student_name not in names:
        print("\n====== INVALID STUDENT ======")
        return

    # Check whether the subject exists
    if subject_name not in subjects:
        print("\n====== INVALID SUBJECT ======") 
        return
   
    # Find the row index of the selected student.
    student_index = np.where(student_name == names)[0][0]

    # Find the column index of the selected subject.
    subject_index = np.where(subject_name == subjects)[0][0]

    print(f"Student: {names[student_index]}")
    print(f"Subject: {subjects[subject_index]}")
    print(f"Marks  : {marks[student_index,subject_index]}")


def show_consecutive_students(
    names: np.ndarray,
    marks: np.ndarray,
    start_student: str,
    end_student: str

) -> None:
    """
    Display the marks of a range of students.

    Parameters:
    names (numpy.ndarray):
        A 1D NumPy array containing the names of all students.

    marks (numpy.ndarray):
        A 2D NumPy array containing the marks of all students.

    start_student_name (str):
        The name of the first student in the range.

    end_student_name (str):
        The name of the last student in the range.

    Displays:
    - Student names within the specified range
    - Marks obtained by each student in all subjects

    If either student does not exist in the dataset or the start student
    comes after the end student, an appropriate error message is displayed.
    """
     
    print("\n====== MARKS OF CONSECUTIVE STUDENTS ======\n")

    # Check whether the start_student exists.
    if start_student not in names:
        print("\n====== INVALID START STUDENT ======\n")
        return

    # Check whether the end_student exists.
    if end_student not in names:
        print("\n====== INVALID END STUDENT ======\n")
        return

    # Find the index of the first student.
    start_student_index = np.where(start_student == names)[0][0]

    # Find the index of the end student.
    end_student_index = np.where(end_student == names)[0][0]

    # Validate the order
    if start_student_index > end_student_index:
        print("The start student must come before the end student.")
        return

    #slicing of arrays
    names_of_students = names[start_student_index : end_student_index +1 ]
    marks_of_students = marks[start_student_index : end_student_index +1 ]

    print("\n======== CONSECUTIVE STUDENTS ========\n")

    for i in range(marks_of_students.shape[0]):
        print(f"Student : {names_of_students[i]}")
        print(f"Marks   : {marks_of_students[i]}\n")


def show_subjects_range(
    subjects: np.ndarray,
    names: np.ndarray,
    marks: np.ndarray,
    start_subject_name: str,
    end_subject_name: str
) -> None:
    """
    Display the marks of all students for a selected range of subjects.

    Parameters:
        subjects (numpy.ndarray):
            A 1D NumPy array containing the subject names.

        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

        start_subject_name (str):
            The name of the first subject in the range.

        end_subject_name (str):
            The name of the last subject in the range.

    Displays:
        - The selected subject range
        - Marks of every student for the selected subjects

    If either subject does not exist in the dataset or the start subject
    comes after the end subject, an appropriate error message is displayed.
    """
    print("\n========== SUBJECT RANGE ==========")

    # Check whether the start_subject exists.
    if start_subject_name not in subjects:
        print("\n====== INVALID START SUBJECT ======\n")
        return

    # Check whether the end_subject exists.
    if end_subject_name not in subjects:
        print("\n====== INVALID END SUBJECT ======\n")
        return

    # Find the index of the first subject.
    start_subject_index = np.where(start_subject_name == subjects)[0][0]

    # Find the index of the end subject.
    end_subject_index = np.where(end_subject_name == subjects)[0][0]

    # Validate the order
    if start_subject_index > end_subject_index:
        print("The start subject must come before the end subject.")
        return

    #slicing of arrays
    names_of_subjects = subjects[start_subject_index : end_subject_index +1 ]
    marks_of_subjects = marks[:,start_subject_index : end_subject_index + 1]

    
    print(f"\nSUBJECTS: {names_of_subjects}\n")

    for i in range(names.shape[0]):
        print(f"{names[i]: <10} : {marks_of_subjects[i]}")


def show_consecutive_student_subject_marks(
    names: np.ndarray,
    subjects: np.ndarray,
    marks: np.ndarray,
    start_student: str,
    end_student: str,
    start_subject: str,
    end_subject: str
) -> None:
    """
    Display the marks of a consecutive range of students
    for a consecutive range of subjects.

    Parameters:
    names (numpy.ndarray):
        A 1D NumPy array containing the names of all students.

    subjects (numpy.ndarray):
        A 1D NumPy array containing the names of all subjects.

    marks (numpy.ndarray):
        A 2D NumPy array where each row represents a student
        and each column represents a subject.

    start_student (str):
        The name of the first student in the selected range.

    end_student (str):
        The name of the last student in the selected range.

    start_subject (str):
        The first subject in the selected range.

    end_subject (str):
        The last subject in the selected range.

    Displays:
    - Student names within the specified range.
    - Subject names within the specified range.
    - Marks obtained by each selected student in each selected subject.

    If any student or subject is not found, or if the start
    value comes after the end value, an appropriate error
    message is displayed.
    """
    print("\n========== STUDENT & SUBJECT RANGE ==========\n")

    # Check whether the start_student exists.
    if start_student not in names:
        print("\n====== INVALID START STUDENT ======\n")
        return

    # Check whether the end_student exists.
    if end_student not in names:
        print("\n====== INVALID END STUDENT ======\n")
        return

    # Check whether the start_subject exists.
    if start_subject not in subjects:
        print("\n====== INVALID START SUBJECT ======\n")
        return

    # Check whether the end_subject exists.
    if end_subject not in subjects:
        print("\n====== INVALID END SUBJECT ======\n")
        return

    # Find the index of the first student.
    start_student_index = np.where(start_student == names)[0][0]

    # Find the index of the end student.
    end_student_index = np.where(end_student == names)[0][0]

    # Find the index of the first subject.
    start_subject_index = np.where(start_subject == subjects)[0][0]

    # Find the index of the end subject.
    end_subject_index = np.where(end_subject == subjects)[0][0]

    # Validate the student order
    if start_student_index > end_student_index:
        print("The start student must come before the end student.")
        return

    # Validate the subject order
    if start_subject_index > end_subject_index:
        print("The start subject must come before the end subject.")
        return

    # Slice the required students,marks and subjects.
    names_of_students = names[start_student_index : end_student_index +1 ]
    selected_marks = marks[start_student_index : end_student_index +1,start_subject_index : end_subject_index +1]
    range_of_subjects = subjects[start_subject_index : end_subject_index +1]

    
    print(f"\nSUBJECTS: {range_of_subjects}")

    for i in range(names_of_students.shape[0]):
        print(f"{names_of_students[i]:<12}: {selected_marks[i]}")


def show_student_statistics(
    names: np.ndarray,
    marks: np.ndarray,
    student_name: str

) -> None:
    """
    Display statistical information for a specific student.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

        student_name (str):
            The name of the student whose statistics are to be displayed.

    Displays:
        - Student name
        - Marks in all subjects
        - Total marks
        - Average marks
        - Highest mark
        - Lowest mark
        - Median
        - Standard deviation
        - Variance

    If the student does not exist in the dataset, an error message is displayed.
    """
     
    print("\n========== STUDENT STATISTICS ==========\n")

    # Check whether the student_name exists.
    if student_name not in names:
        print("\n====INVALID STUDENT====\n")
        return
    
    # Find the index of the student.
    student_index = np.where(student_name == names)[0][0]

    # Extract the marks of the selected student.
    student_marks = marks[student_index]

    # Print the student's name.
    print(f"STUDENT: {names[student_index]}\n")
    # Print the student's marks.
    print(f"MARKS: {student_marks}\n")

    # Calculate and display the total marks.
    print(f"TOTAL: {np.sum(student_marks)}")
    # Calculate and display the average marks.
    print(f"AVERAGE: {np.mean(student_marks):.2f}")
    # Display the highest mark.
    print(f"HIGHEST: {np.max(student_marks)}")
    # Display the lowest mark.
    print(f"LOWEST: {np.min(student_marks)}")
    # Display the median mark.
    print(f"MEDIAN: {np.median(student_marks):.2f}")
    # Display the standard deviation.
    print(f"STD_DEV: {np.std(student_marks):.2f}")
    # Display the variance.
    print(f"VARIANCE: {np.var(student_marks):.2f}")


def show_subject_statistics(
    subjects: np.ndarray,
    marks: np.ndarray,
    subject_name: str
) -> None: 
    """
    Display statistical information for a specific subject.

    Parameters:
        
        subjects (numpy.ndarray):
            A 1D NumPy array containing the names of all subjects.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

        subject_name (str):
            The name of the subject whose statistics are to be displayed.

    Displays:
        - Subject name
        - Marks obtained by all students in the selected subject
        - Total marks
        - Average marks
        - Highest mark
        - Lowest mark
        - Median
        - Standard deviation
        - Variance

    If the subject does not exist in the dataset, an appropriate error
    message is displayed.
    """

    print("\n========== SUBJECT STATISTICS ==========\n")

    # Check whether the subject_name exists.
    if subject_name not in subjects:
        print("\n====INVALID SUBJECT====\n")
        return
    
    # Find the index of the student.
    subject_index = np.where(subject_name == subjects)[0][0]

    # Extract the marks of the selected subject.
    subject_marks = marks[: ,subject_index]

    # Print the subject's name.
    print(f"SUBJECT: {subjects[subject_index]}\n")
    # Print the subject's marks.
    print(f"MARKS: {subject_marks}\n")

    # Calculate and display the total marks.
    print(f"TOTAL: {np.sum(subject_marks)}")
    # Calculate and display the average marks.
    print(f"AVERAGE: {np.mean(subject_marks):.2f}")
    # Display the highest mark.
    print(f"HIGHEST: {np.max(subject_marks)}")
    # Display the lowest mark.
    print(f"LOWEST: {np.min(subject_marks)}")
    # Display the median mark.
    print(f"MEDIAN: {np.median(subject_marks):.2f}")
    # Display the standard deviation.
    print(f"STD_DEV: {np.std(subject_marks):.2f}")
    # Display the variance.
    print(f"VARIANCE: {np.var(subject_marks):.2f}")


def show_class_statistics(
    names: np.ndarray,
    subjects: np.ndarray,
    marks: np.ndarray,
    
) -> None:
    """
    Display overall statistical information for the entire class.

    Parameters:
        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

    Displays:
        - Total number of students
        - Total number of subjects
        - Overall average marks
        - Highest mark
        - Lowest mark
        - Median
        - Standard deviation
        - Variance
    """
    
    print("\n ======= CLASS STATITICS ======= \n")
    # Display total no of students
    print(f"TOTAL STUDENTS: {names.shape[0]}")
    # Display total no of subjects
    print(f"TOTAL SUBJECTS: {subjects.shape[0]}")
    # Calculate and display the overall average marks.
    print(f"OVERALL AVERAGE: {np.mean(marks):.2f}")
    # Display the highest mark.
    print(f"HIGHEST MARKS: {np.max(marks)}")
    # Display the lowest mark.
    print(f"LOWEST MARKS: {np.min(marks)}")
    # Display the median mark.
    print(f"MEDIAN: {np.median(marks)}")
    # Display the standard deviation.
    print(f"STANDARD DEVIATION: {np.std(marks):.2f}")
    # Display the variance.
    print(f"VARIANCE: {np.var(marks):.2f}")


def show_student_ranking(
    names: np.ndarray,
    marks: np.ndarray,

) -> None:
    """
    Display the ranking of all students based on their total marks.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

    Displays:
        - Students ranked from highest to lowest based on total marks
        - Rank number
        - Student name
        - Total marks

    Ranking is determined by calculating the total marks of each student
    and sorting them in descending order.
    """

    print("\n========== STUDENT RANKING ==========\n")
    
    # Reusing the existing function for total marks.
    student_total = calculate_total_marks(marks,names,display = False)

    # Get student indices sorted by total marks in descending order.
    ranked_indices = np.argsort(student_total)[::-1]

    # Display the ranking.
    for rank, index in enumerate(ranked_indices, start=1):
        print(f"{rank:>2}. {names[index]:<10} : {student_total[index]}")


def show_topper_weakest_student(
    names: np.ndarray,
    marks: np.ndarray
) -> None: 
    """
    Display the topper and the weakest-scoring student based on total marks.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

    Displays:
        - Topper's name
        - Topper's total marks
        - Weakest student's name
        - Weakest student's total marks
    """
    print("\n========== TOPPER & WEAKEST STUDENT ==========\n")

    # Reusing the existing function for total marks.
    student_total = calculate_total_marks(marks,names,display = False)

    # Find the index of the topper.
    topper_index = np.argmax(student_total)

    # Find the index of the weakest.
    weakest_index = np.argmin(student_total)

    print("TOPPER\n------")
    print(f"Name        : {names[topper_index]}")
    print(f"Total Marks : {student_total[topper_index]}")

    print("\nWEAKEST\n------")
    print(f"Name        : {names[weakest_index]}")
    print(f"Total Marks : {student_total[weakest_index]}")



    
    



if __name__ == "__main__":
    main()
   