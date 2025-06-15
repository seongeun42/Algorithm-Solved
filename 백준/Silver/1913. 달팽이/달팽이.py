def solve():
    N = int(input())
    M = int(input())
    arr = [[0] * N for _ in range(N)]
    start = (N // 2, N // 2)
    direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dist, turn, d = 1, 2, 0
    cr, cc = start
    arr[cr][cc] = 1
    num = 2
    ans = (cr + 1, cc + 1)
    while num <= N ** 2:
        for _ in range(dist):
            if num > N ** 2:
                break
            cr += direct[d][0]
            cc += direct[d][1]
            arr[cr][cc] = num
            if num == M:
                ans = (cr + 1, cc + 1)
            num += 1
        turn -= 1
        d = (d + 1) % 4
        if turn == 0:
            dist += 1
            turn = 2
    for i in range(N):
        print(*arr[i])
    print(*ans)

solve()