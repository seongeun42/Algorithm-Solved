import sys
input = sys.stdin.readline

N, M  = map(int, input().split())
cnt = dict(zip(range(1, N + 1), [0] * N))
for _ in range(M):
    A, B = map(int,  input().split())
    cnt[A] += 1
    cnt[B] += 1
for k, v in sorted(cnt.items(), key=lambda x: x[0]):
    print(v)