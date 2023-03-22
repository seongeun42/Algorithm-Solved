import sys
input = sys.stdin.readline

L = int(input())
N = int(input())
cake = [0] * L
want = [0] * N
actu = [0] * N
for i in range(N):
    p, k = map(int, input().split())
    want[i] = k - p + 1
    for j in range(p - 1, k):
        if cake[j] == 0:
            cake[j] = 1
            actu[i] += 1
print(want.index(max(want)) + 1)
print(actu.index(max(actu)) + 1)