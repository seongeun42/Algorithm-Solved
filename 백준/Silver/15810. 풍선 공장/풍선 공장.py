if __name__ == "__main__":
    N, M = map(int, input().split())
    A = [*map(int, input().split())]
    s, e = 0, max(A) * M
    ans = 0
    while s <= e:
        m = (s + e) // 2
        if sum([m // t for t in A]) >= M:
            ans = m
            e = m - 1
        else:
            s = m + 1
    print(ans)