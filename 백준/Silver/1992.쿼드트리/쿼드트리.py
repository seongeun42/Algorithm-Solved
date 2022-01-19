def recursive(m, x, y, d):
    flag = True
    for i in range(y, y + d):
        for j in range(x, x + d):
            if m[i][j] != m[y][x]:
                flag = False
                print("(", end='')
                recursive(m, x, y, d // 2)
                recursive(m, x + d // 2, y, d // 2)
                recursive(m, x, y + d // 2, d // 2)
                recursive(m, x + d // 2, y + d // 2, d // 2)
                print(")", end='')
                break
        if not flag: break
    if flag: print(m[y][x], end='')

n = int(input())
m = [list(input().strip()) for _ in range(n)]
recursive(m, 0, 0, n)