#1
def lowest_gpa(csv_file):
  lowest_gpa = 4.0
  for student in csv_file:
    if float(student["gpa"]) < lowest_gpa:
      lowest_gpa = float(student["gpa"])
  return lowest_gpa

#2
def average_gpa(csv_file):
  average_gpa = 0.0
  num_of_students = 0
  for student in csv_file:
    num_of_students += 1
    average_gpa += float(student["gpa"])
  return average_gpa / num_of_students

#3
def gpa_range(csv_file):
  highest_gpa = 0.0
  lowest_gpa = 4.0
  for student in csv_file:
    if float(student["gpa"]) < lowest_gpa:
      lowest_gpa = float(student["gpa"])
    if float(student["gpa"]) > highest_gpa:
      highest_gpa = float(student["gpa"])
  return highest_gpa - lowest_gpa