def dfs(node, i):
    if node >= N:
        return
    if i == 0:
        print(chr(node + A), end='')
    if G[node][0] != nul:
        dfs(G[node][0], i)
    if i == 1:
        print(chr(node + A), end='')
    if G[node][1] != nul:
        dfs(G[node][1], i)
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
    dfs(0, i)
    print()