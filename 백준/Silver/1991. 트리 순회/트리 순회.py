def dfs(visit, node, i):
    if node >= N:
        return
    visit[node] = 1
    if i == 0:
        print(chr(node + A), end='')
    if G[node][0] != nul and not visit[G[node][0]]:
        dfs(visit, G[node][0], i)
    if i == 1:
        print(chr(node + A), end='')
    if G[node][1] != nul and not visit[G[node][1]]:
        dfs(visit, G[node][1], i)
    if i == 2:
        print(chr(node + A), end='')

N = int(input())
G = [[] for _ in range(N)]
A = ord('A')
nul = ord('.') - A
for _ in range(N):
    P, CL, CR = input().split()
    G[ord(P) - A].append(ord(CL) - A)
    G[ord(P) - A].append(ord(CR) - A)
for i in range(3):
    visited = [0] * N
    dfs(visited, 0, i)
    print()