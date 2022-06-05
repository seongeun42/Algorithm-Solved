import sys
input = sys.stdin.readline

S, C = map(int, input().split())
L = [int(input()) for _ in range(S)]
st, ed = 0, 1000000000
leng = 0

while st <= ed:
    mid = (st + ed) // 2
    if mid == 0:
        mid = 1

    cnt = 0
    for v in L:
        cnt += v // mid

    if cnt >= C:
        leng = max(leng, mid)
        st = mid + 1
    else:
        ed = mid - 1

res = sum(L) - leng * C
print(res)