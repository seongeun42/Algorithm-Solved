def solve():
    N = int(input())
    if N < 2:
        print(0)
        return

    chk = [0, 0] + [0, 1] * (N // 2)
    chk[2] = 1
    sosu = [2]
    for i in range(3, N + 1, 2):
        if chk[i] == 0:
            continue
        sosu.append(i)
        for j in range(i + i, N + 1, i):
            chk[j] = 0

    ans = 0
    s, e = 0, 0
    total = sosu[0]
    while s <= e:
        if total == N:
            ans += 1
        elif total < N:
            if e == len(sosu) - 1:
                break
            e += 1
            total += sosu[e]
            continue
        total -= sosu[s]
        s += 1
    print(ans)

solve()