n = int(input())
t, s = list(map(int, input().split())), []
for i, v in enumerate(t):
    while s and s[-1][1] <= v:
        s.pop()
    print(s[-1][0] if s else 0, end=' ')
    s.append([i + 1, v])
