#1
def student_with_lowest_grade(d):
    lowest_grade = 100
    student_name = ""
    for k, v in d.items():
        if v < lowest_grade:
            lowest_grade = v
            student_name = k
    return student_name

#2
def numbers_of_As(d):
    total = 0
    for k,v in d.items():
        if v >= 93:
            total += 1
    return total