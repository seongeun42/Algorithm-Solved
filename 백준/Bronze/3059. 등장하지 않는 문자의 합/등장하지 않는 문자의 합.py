import sys
input = sys.stdin.readline

T = int(input())
alpa = set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
for _ in range(T):
    ans = 0
    S = set(list(input().rstrip()))
    for c in alpa - S:
        ans += ord(c)
    print(ans)