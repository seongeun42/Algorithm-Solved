import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = [int(input()) for _ in range(m)]
s, e = 1, max(j)
ans = e
while s <= e:
    mid = (s + e) // 2
    receiver = 0
    for cnt in j:
        q, r = divmod(cnt, mid)
        receiver += q
        if r > 0:
            receiver += 1
    if receiver > n:
        s = mid + 1
    else:
        ans = mid
        e = mid - 1
print(ans)