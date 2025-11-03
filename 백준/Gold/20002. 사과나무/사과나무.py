import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = [[*map(int, input().split())] for _ in range(N)]
    prefix = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i - 1][j - 1]
    ans = -1e9
    for w in range(N):
        for i in range(1, N + 1):
            if i + w > N:
                break
            for j in range(1, N + 1):
                if j + w > N:
                    break
                v = prefix[i + w][j + w] - prefix[i - 1][j + w] - prefix[i + w][j - 1] + prefix[i - 1][j - 1]
                if ans < v:
                    ans = v
    print(ans)

solve()