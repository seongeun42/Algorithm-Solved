import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    U = sorted([int(input()) for _ in range(N)])
    hap = set()
    for i in range(N):
        for j in range(i, N):
            hap.add(U[i] + U[j])
    for i in range(N - 1, -1, -1):
        for j in range(i, -1, -1):
            if U[i] - U[j] in hap:
                return U[i]
            
print(solve())