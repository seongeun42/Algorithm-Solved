def solve():
    N, K = map(int, input().split(  ))
    a = [*map(int, input().split(  ))]
    ans, tmp = 0, 0
    num = [0] * 100001
    s = 0
    for i in range(N):
        if num[a[i]] + 1 <= K:
            num[a[i]] += 1
            tmp += 1
        else:
            if ans < tmp:
                ans = tmp
            while num[a[i]] + 1 > K:
                num[a[s]] -= 1
                tmp -= 1
                s += 1
            num[a[i]] += 1
            tmp += 1
    print(max(ans, tmp))

if __name__ == "__main__":
    solve()