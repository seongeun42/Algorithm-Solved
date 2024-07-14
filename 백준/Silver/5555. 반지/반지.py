import sys
input = sys.stdin.readline

find = input().rstrip()
N = int(input())
ans = 0
for _ in range(N):
    s = input().rstrip()
    s += s[:len(s) - 1]
    if find in s:
        ans += 1
print(ans)