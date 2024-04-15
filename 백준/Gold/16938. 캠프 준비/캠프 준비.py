from itertools import combinations as cb
import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
A = sorted([*map(int, input().split())])
ans = 0
for i in range(2, N + 1):
    for list in cb(A, i):
        if L <= sum(list) <= R and max(list) - min(list) >= X:
            ans += 1
print(ans)