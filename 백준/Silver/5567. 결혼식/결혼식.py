import sys
input = sys.stdin.readline

def solve():
    n, m = int(input()), int(input())
    G = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    
    ans = set(G[1])
    for friend in G[1]:
        ans = ans.union(set(G[friend]))
    ans.discard(1)
    print(len(ans))

solve()