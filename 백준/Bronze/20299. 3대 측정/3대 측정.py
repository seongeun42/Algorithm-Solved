import sys
input = sys.stdin.readline

N, K, L = map(int, input().split())
arr = []
for _ in range(N):
    s = input().rstrip()
    rating = [*map(int, s.split())]
    if sum(rating) < K or rating[0] < L or rating[1] < L or rating[2] < L:
        continue
    arr.append(s)
print(len(arr))
print(*arr)