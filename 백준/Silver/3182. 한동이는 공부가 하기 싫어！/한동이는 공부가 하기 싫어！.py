import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = [0] + [int(input()) for _ in range(N)]
    ans = [0, 0]
    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        visited[i] = True
        nxt = arr[i]
        cnt = 1
        while not visited[nxt]:
            visited[nxt] = True
            nxt = arr[nxt]
            cnt += 1
        if ans[1] < cnt:
            ans = [i, cnt]
    print(ans[0])

solve()