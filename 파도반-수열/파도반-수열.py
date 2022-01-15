t = int(input())
p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for _ in range(t):
    n = int(input())
    for i in range(len(p), n + 1):
        p.append(p[i - 1] + p[i - 5])
    print(p[n])