import sys
input = sys.stdin.readline

N = int(input())
t = sorted([*map(int, input().split())])
if N % 2 == 0:
    M = t[0] + t[-1]
    for i in range(1, N // 2):
        v = t[i] + t[N - i - 1]
        if M < v:
            M = v
else:
    M = t[-1]
    for i in range(N // 2):
        v = t[i] + t[N - i - 2]
        if M < v:
            M = v
print(M)