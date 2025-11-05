student = int(input("Enter number of students: "))
subject = int(input("Enter number of subjects: "))

class_total = 0

for student in range(1, student + 1):
    print(f"\nStudent {student}")
    sum_scores = 0
    
    for subject in range(1, subject + 1):
        score = float(input(f"Enter score {subject}: "))
        sum_scores += score
    
    student_average = sum_scores / subject
    print(f"Average for Student {student} = {student_average:.1f}")
    
    class_total += student_average

class_average = class_total / student
print(f"\nClass Average = {class_average:.1f}")