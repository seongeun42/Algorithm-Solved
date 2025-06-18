import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(N)], key=lambda x: (-x[0], x[1]))
ans = 0
for i in range(5, N):
    if arr[i][0] == arr[4][0]:
        ans += 1
print(ans)