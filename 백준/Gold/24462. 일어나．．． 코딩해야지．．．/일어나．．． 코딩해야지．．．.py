import sys, math
input = sys.stdin.readline
N, D = map(int, input().split())
TKC = [[*map(int, input().split())] + [0] for _ in range(N)]
for i in range(N):
    TKC[i][2] = (D - TKC[i][0]) // TKC[i][1] + 1
arm1, arm2, ans = 0, 0, 0
for i in range(N):
    for j in range(i + 1, N):
        gcd = math.gcd(TKC[i][1], TKC[j][1])
        lcm = TKC[i][1] * TKC[j][1] // gcd
        arm3 = 0
        if max(TKC[i][0], TKC[j][0]) % lcm == 0:
            arm3 = max(TKC[i][0], TKC[j][0])
        else:
            arm3 = (max(TKC[i][0], TKC[j][0]) // lcm + 1) * lcm
        arm3 = (D - arm3) // lcm + 1 if arm3 <= D else 0
        cnt = TKC[i][2] + TKC[j][2] - arm3
        if ans < cnt:
            arm1, arm2, ans = i, j, cnt
print(arm1 + 1, arm2 + 1)
print(ans)