import sys
input = sys.stdin.readline

M, N = map(int, input().split())
first = [0] * (2 * M - 1)
for _ in range(N):
    zero, one, two = map(int, input().split())
    idx = zero
    flag = 1
    if one > 0:
        first[idx] += 1
        idx += one
        flag -= 1
    if two > 0:
        first[idx] += 1 + flag
first[0] += 1
for i in range(1, len(first)):
    first[i] += first[i - 1]
s = []
for i in range(M, 2 * M - 1):
    s.append(first[i])
for i in range(M - 1, -1, -1):
    print(first[i], *s)