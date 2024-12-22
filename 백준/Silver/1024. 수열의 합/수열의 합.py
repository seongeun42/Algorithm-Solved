def solve():
    N, L = map(int, input().split())
    for size in range(L, 101):
        x = N / size - (size + 1) / 2
        if int(x) == x and x + 1 >= 0:
            x = int(x)
            print(*list(range(x + 1, x + size + 1)))
            return
    print(-1)
    return

solve()