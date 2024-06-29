import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    L, D = input().split('-')
    L = L[::-1]
    v = abs(sum([(ord(L[i]) - 65) * (26 ** i) for i in range(len(L))]) - int(D))
    print("nice" if v <= 100 else "not nice")