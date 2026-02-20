import sys
input = sys.stdin.readline

N = int(input())
P = [int(input()) for _ in range(N)]
P_sorted = sorted([(v, i) for i, v in enumerate(P)], reverse=True)
left = P[:]
ans = []
for v, i in P_sorted:
    if left[i] == -1:
        continue
    ans.append(i + 1)
    left[i] = -1
    r = i + 1
    while r < N and left[r - 1] < 0 and P[r - 1] > P[r]:
        left[r] = -1
        r += 1
    l = i - 1
    while l >= 0 and left[l + 1] < 0 and P[l + 1] > P[l]:
        left[l] = -1
        l -= 1
print(*sorted(ans))