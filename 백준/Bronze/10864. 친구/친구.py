import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = [0] * N
for _ in range(M):
    A, B = map(int, input().split())
    cnt[A - 1] += 1
    cnt[B - 1] += 1
print(*cnt, sep='\n')