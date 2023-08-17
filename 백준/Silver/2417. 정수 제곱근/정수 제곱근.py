def solve():
    n = int(input())
    s, e = 0, 9223372036854775807
    ans = 0
    while s <= e:
        mid = (s + e) // 2
        v = mid * mid
        if n <= v:
            ans = mid
            e = mid - 1
        else:
            s = mid + 1
    print(ans)

solve()