import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    J, N = map(int, input().split())
    area = []
    for _ in range(N):
        R, C = map(int, input().split())
        area.append(R * C)
    area.sort(reverse=True)
    ans = 0
    total = 0
    for v in area:
        if total >= J:
            break
        total += v
        ans += 1
    print(ans)