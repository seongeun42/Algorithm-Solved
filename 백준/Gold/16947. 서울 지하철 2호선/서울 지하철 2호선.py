from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find_circle(G, visited, cur):
    v = 0
    for n in G[cur]:
        # 이전 노드면 패스
        if n == visited[cur]:
            continue
        # 방문한 적 없으면
        if not visited[n]:
            visited[n] = cur
            v = find_circle(G, visited, n)
            # 사이클을 찾았으면 탐색 중단
            if v < 0:
                break
        # 방문한 적 있으면 사이클 시작
        else:
            v = -n
            break
    visited[cur] = v
    # 현재 노드가 사이클 시작점이면 이제 0 반환
    return v if v != -cur else 0

def find_dist(G, visited, s):
    q = deque([s])
    visited[s] = 1
    while q:
        c = q.popleft()
        for n in G[c]:
            if visited[n] < 0:
                return visited[c]
            if not visited[n]:
                visited[n] = visited[c] + 1
                q.append(n)

def solve():
    N = int(input())
    G = [[] for _ in range(N + 1)]
    for _ in range(N):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    visited = [0] * (N + 1)
    # 순환선 찾기
    visited[1] = 1
    find_circle(G, visited, 1)
    # 거리 출력
    for i in range(1, N + 1):
        if visited[i] == 0:
            print(find_dist(G, visited[:], i), end=" ")
        else:
            print(0, end=" ")

solve()