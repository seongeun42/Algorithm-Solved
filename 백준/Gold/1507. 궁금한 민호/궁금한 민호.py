import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    time = [[*map(int, input().split())] for _ in range(N)]
    for m in range(N):
        for i in range(N):
            for j in range(N):
                if time[i][j] == 0 or time[i][m] == 0 or time[m][j] == 0:
                    continue
                if time[i][j] == time[i][m] + time[m][j]:
                    time[i][j] = 0
                    time[j][i] = 0
                elif time[i][j] > time[i][m] + time[m][j]:
                    print(-1)
                    return
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += time[i][j]
    print(ans)

solve()