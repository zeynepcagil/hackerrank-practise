def gradingStudents(grades):
    newGrades = []
    for grade in grades:
        if grade<38:
            newGrades.append(grade)
        else:
            remainder = grade%5
            points_to_next_multiple = 5 - remainder
            if points_to_next_multiple<3:
                grade=grade+points_to_next_multiple
                newGrades.append(grade)
            else:
                newGrades.append(grade)      
    return newGrades 