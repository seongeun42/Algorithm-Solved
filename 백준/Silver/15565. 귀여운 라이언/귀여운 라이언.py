def solve():
    N, K = map(int, input().split())
    doll = [*map(int, input().split())]
    cnt = doll[0] % 2
    ans = 1e7
    s, e = 0, 0
    while s <= e:
        if cnt >= K and ans > e - s + 1:
            ans = e - s + 1
        if cnt < K:
            if e < N - 1:
                e += 1
                if doll[e] == 1:
                    cnt += 1
            else: break
        elif cnt >= K:
            if doll[s] == 1:
                cnt -= 1
            s += 1
    print(ans if ans != 1e7 else -1)

solve()