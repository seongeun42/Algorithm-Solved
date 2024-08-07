import sys
input = sys.stdin.readline

def backtrack(W, visited, energy, dep):
    global ans
    if len(W) - dep == 2:
        if ans < energy:
            ans = energy
        return
    for i in range(1, len(W) - 1):
        if visited[i]:
            continue
        visited[i] = 1
        getE = 1
        for l in range(i - 1, -1, -1):
            if not visited[l]:
                getE *= W[l]
                break
        for r in range(i + 1, len(W)):
            if not visited[r]:
                getE *= W[r]
                break
        backtrack(W, visited, energy + getE, dep + 1)
        visited[i] = 0

N = int(input())
W = [*map(int, input().split())]
visited = [0] * N
ans = 0
backtrack(W, visited, 0, 0)
print(ans)