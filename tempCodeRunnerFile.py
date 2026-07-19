def show_students_with_full_marks(
    names    : np.ndarray,
    marks    : np.ndarray,
    subjects : np.ndarray
) -> None : 
    """
    Displays students who scored full marks in one or more subjects.

    The function checks each student's marks using NumPy Boolean indexing.
    If a student has scored full marks (100) in any subject, their name
    and the corresponding subject(s) are displayed.

    Parameters:
        names (np.ndarray): A one-dimensional NumPy array containing the
            names of all students.
        marks (np.ndarray): A two-dimensional NumPy array where each row
            represents a student's marks across all subjects.
        subjects (np.ndarray): A one-dimensional NumPy array containing
            the names of all subjects.

    Returns:
        None

    Displays:
        - The names of students who scored full marks.
        - The subject(s) in which they scored full marks.
        - The total number of students with at least one full mark.
    """
    FULL_MARKS = 100

    total_students = 0

    print("\n========== STUDENTS WITH FULL MARKS ==========\n")

    for i in range(names.shape[0]):
        student_marks = marks[i]

        # Create a Boolean mask for subjects with full marks.
        perfect_score_mask = student_marks == FULL_MARKS

        if np.any(perfect_score_mask):
            total_students += 1

            print(f"{names[i]}")
            print("-" * len(names[i]))
            
            # Find the indices of subjects with perfect scores.
            subject_indices = np.where(perfect_score_mask)[0]

            for index in subject_indices:
                print(f"{subjects[index]:<10} : {FULL_MARKS}")
            
            print()

    print(f"Total Students with Full Marks : {total_students}")
            

        
            
