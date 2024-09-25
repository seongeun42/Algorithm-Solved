def solve():
    D = int(input())
    test = [*map(int, input().split())]
    cnt = 1
    total = 1
    act_num = 1
    print(1)
    for i in range(1, D):
        act_num = (act_num - 1) * (i + 1) + test[i]
        print((total + act_num) % 1_000_000_007)
        cnt *= (i + 1)
        total += cnt

solve()