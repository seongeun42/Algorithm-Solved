N, m, M, T, R = map(int, input().split())
time, cnt, cur = 0, 0, m
while cnt < N:
    if m + T > M:
        break
    if cur + T <= M:
        cur += T
        cnt += 1
    else:
        cur = max(m, cur - R)
    time += 1
print(time if cnt == N else -1)