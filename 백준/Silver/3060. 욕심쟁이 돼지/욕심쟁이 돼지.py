import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    need = sum([*map(int, input().split())])
    ans = 1
    while N - need >= 0:
        need *= 4
        ans += 1
    print(ans)