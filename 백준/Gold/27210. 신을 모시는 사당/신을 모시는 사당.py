def solve():
    N = int(input())
    direction = [*map(int, input().split())]
    prefix = 0
    min_v, max_v = 0, 0
    ans = 0
    for i in range(N):
        prefix += 1 if direction[i] == 1 else -1
        if ans < abs(prefix - min_v):
            ans = abs(prefix - min_v)
        if ans < abs(max_v - prefix):
            ans = abs(max_v - prefix)
        if prefix < min_v:
            min_v = prefix
        if max_v < prefix:
            max_v = prefix
    print(ans)

solve()