import sys
input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())
s = 1
ans = 0
for i in range(J):
    lo = int(input())
    if s <= lo <= s + M - 1:
        continue
    if lo < s:
        ans += abs(s - lo)
        s = lo
    else:
        ans += abs(s + M - 1 - lo)
        s = lo - (M - 1)
print(ans)