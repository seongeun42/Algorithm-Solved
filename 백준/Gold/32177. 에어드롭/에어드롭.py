from collections import deque
import sys
input = sys.stdin.readline

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def solve():
    N, K, T = map(int, input().split())
    people = [[*map(int, input().split())]]
    G = [[] for _ in range(N + 1)]
    havePicture = set()
    for i in range(1, N + 1):
        x, y, v, p = map(int, input().split())
        if p == 1:
            havePicture.add(i)
        for j, person in enumerate(people):
            if abs(v - person[2]) <= T and distance(x, y, person[0], person[1]) <= K:
                G[j].append(i)
                G[i].append(j)
        people.append([x, y, v])
    q = deque([0])
    visited = [False] * (N + 1)
    visited[0] = True
    ans = []
    while q:
        cur = q.popleft()
        if cur in havePicture:
            ans.append(cur)
        for nxt in G[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    ans.sort()
    if len(ans) == 0:
        print(0)
    else:
        print(*ans)

solve()