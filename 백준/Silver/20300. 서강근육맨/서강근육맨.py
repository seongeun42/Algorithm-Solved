import sys
input = sys.stdin.readline

N = int(input())
t = sorted([*map(int, input().split())])
odd = N % 2 == 1
M = t[-1] if odd else 0
for i in range(N // 2):
    v = t[i] + (t[N - i - 2] if odd else t[N - i - 1])
    if M < v:
        M = v
print(M)