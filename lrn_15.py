'''x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = [
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if i + j + k != n
]

print(coordinates)'''
#students = []

'''n = int(input())
for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])
grades = sorted({student[1] for student in students})
second_lowest = grades[1]
names = sorted(
    student[0]
    for student in students
    if student[1] == second_lowest
)
for name in names:
    print(name)'''
t = int(input())

for _ in range(t):
    n = int(input())
    cubes = list(map(int, input().split()))
    
    last = float('inf')  # top cube size
    
    while cubes:
        if cubes[0] >= cubes[-1]:
            chosen = cubes.pop(0)
        else:
            chosen = cubes.pop()
        
        if chosen <= last:
            last = chosen
        else:
            print("No")
            break
    else:
        print("Yes")


