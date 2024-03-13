N, K = map(int, input().split())
problem = [*map(int, input().split())]
s, e = 0, 20 * N
ans = 0
while s <= e:
    mid = (s + e) // 2
    cnt = tmp = 0
    for i in range(N):
        tmp += problem[i]
        if tmp >= mid:
            cnt += 1
            tmp = 0
    if cnt >= K:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1
print(ans)