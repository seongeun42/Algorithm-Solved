import sys
input = sys.stdin.readline

N = int(input())
p = set()
ans = 0
for _ in range(N):
    s = input().rstrip()
    if s == "ENTER":
        p = set()
    elif s not in p:
        p.add(s)
        ans += 1
print(ans)