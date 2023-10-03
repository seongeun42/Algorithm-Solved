def solve():
    N = int(input())
    A = sorted([*map(int, input().split())])
    ans = 0
    for i in range(N):
        list = A[:i] + A[i + 1:]
        s, e = 0, len(list) - 1
        while s < e:
            v = list[s] + list[e]
            if v == A[i]:
                ans += 1
                break
            if v < A[i]:
                s += 1
            else:
                e -= 1
    print(ans)

solve()