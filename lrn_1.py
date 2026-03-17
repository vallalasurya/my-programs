students = []
n = int(input("Enter number of students: "))
for _ in range(n):
    name = input("Enter student name: ")
    score = float(input("Enter student score: "))
    students.append([name, score])  # nested list: [name, score]
unique_scores = sorted({score for name, score in students})
second_lowest = unique_scores[1]
second_lowest_students = [name for name, score in students if score == second_lowest]
for name in sorted(second_lowest_students):
    print(name)
