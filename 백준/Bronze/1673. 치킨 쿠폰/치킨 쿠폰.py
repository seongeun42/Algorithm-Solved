import sys
input = sys.stdin.readline

while 1:
    try:
        n, k = map(int, input().split())
        ans, coupon = n, n
        while coupon >= k:
            v, m = divmod(coupon, k)
            ans += v
            coupon = m + v
        print(ans)
    except:
        break