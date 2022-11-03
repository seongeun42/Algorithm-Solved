n = int(input())
students = []
for _ in range(n):
    name, d, m, y = input().split()
    students.append([name, int(d), int(m), int(y)])
students.sort(key=lambda x : (x[3], x[2], x[1]))
print(students[-1][0])
print(students[0][0])