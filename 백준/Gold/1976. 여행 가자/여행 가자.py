from _collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    q = deque([s])
    visit[s] = 1
    while q:
        node = q.popleft()
        for i, v in enumerate(arr[node - 1]):
            if v == 1 and not visit[i + 1]:
                visit[i + 1] = 1
                q.append(i + 1)

N = int(input())
M = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
plan = [*map(int, input().split())]
visit = [0] * (N + 1)
bfs(plan[0])
res = "YES"
for v in plan:
    if not visit[v]:
        res = "NO"
        break
print(res)