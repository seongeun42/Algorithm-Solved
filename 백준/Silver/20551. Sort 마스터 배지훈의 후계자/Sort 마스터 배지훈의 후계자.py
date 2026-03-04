import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = sorted([int(input()) for _ in range(N)])
B = {}
for i, v in enumerate(A):
    if v not in B:
        B[v] = i
for _ in range(M):
    D = int(input())
    print(B[D] if D in B else -1)