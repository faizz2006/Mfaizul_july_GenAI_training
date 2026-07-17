# q1_result_analyzer.py

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"

student_name = input("Enter Student Name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter marks for Subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
grade = calculate_grade(average)

print("\n------ RESULT ------")
print("Student Name :", student_name)
print("Marks :", marks)
print("Total :", total)
print("Average :", round(average, 2))
print("Grade :", grade)
