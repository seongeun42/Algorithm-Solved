import sys
input = sys.stdin.readline

N = int(input())
ans = ""
for _ in range(N):
    name = input()
    if 'S' in name:
        ans = name
print(ans)