import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])
ans = 4
for i in range(N):
    need = 4
    for j in range(i + 1, N):
        if arr[j] > arr[i] + 4:
            break
        need -= 1
    ans = min(ans, need)
print(ans)