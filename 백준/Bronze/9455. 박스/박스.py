import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    grid = [[*map(int, input().split())] for _ in range(m)]
    st = [m] * n
    ans = 0
    for i in range(m - 1, -1, -1):
        for j in range(n):
            if grid[i][j] == 1:
                st[j] -= 1
                ans += st[j] - i
    print(ans)