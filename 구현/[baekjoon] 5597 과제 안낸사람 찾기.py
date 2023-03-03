import sys

students = [i for i in range(1, 31)]
#print(students)

for i in range(28):
    a = int(input())
    students.remove(a)

print(min(students))
print(max(students))
