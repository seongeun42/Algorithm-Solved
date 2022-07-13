import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    r = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            r[j] = not r[j]
    print(sum(r))