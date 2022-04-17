import sys
input = sys.stdin.readline

N, C, W = map(int, input().split())
tree = [int(input()) for _ in range(N)]
res = 0
for l in range(1, max(tree) + 1):
    hap = 0
    for leng in tree:
        cnt, remain = divmod(leng, l)
        cost = (cnt * W * l) - (cnt * C) if remain else (cnt * W * l) - ((cnt - 1) * C)
        if cost < 0:
            continue
        hap += cost
    res = max(hap, res)
print(res)