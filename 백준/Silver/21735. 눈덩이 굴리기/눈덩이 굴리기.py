import sys
input = sys.stdin.readline

def backtrack(cur, time, size):
    global ans
    if cur == N or time == M:
        if ans < size:
            ans = size
        return
    for nxt in range(cur + 1, cur + 3):
        if nxt <= N and not visited[nxt]:
            visited[nxt] = True
            if nxt == cur + 1:
                backtrack(nxt, time + 1, size + a[nxt])
            else:
                backtrack(nxt, time + 1, size // 2 + a[nxt])
            visited[nxt] = False

N, M = map(int, input().split())
a = [0] + [*map(int, input().split())]
visited = [True] + [False] * N
ans = 0
backtrack(0, 0, 1)
print(ans)