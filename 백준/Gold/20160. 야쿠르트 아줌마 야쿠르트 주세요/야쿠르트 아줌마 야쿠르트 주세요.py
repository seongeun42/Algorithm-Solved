import sys, heapq
input = sys.stdin.readline

def dijkstra(G, weight, S):
    dp = [1e10] * len(G)
    dp[S] = 0
    hq = [(0, S)]
    while hq:
        cw, cn = heapq.heappop(hq)
        if dp[cn] < cw:
            continue
        for nn in G[cn]:
            w = weight[(min(nn, cn), max(nn, cn))] + cw
            if w < dp[nn]:
                dp[nn] = w
                heapq.heappush(hq, (w, nn))
    return dp

def solve():
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    weight = {}
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
        tmp = (min(u, v), max(u, v))
        if tmp not in weight or w < weight[tmp]:
            weight[tmp] = w
    seller = [*map(int, input().split())]
    start = int(input())
    my_time = dijkstra(G, weight, start)
    seller_time = {}
    for v in set(seller):
        seller_time[v] = dijkstra(G, weight, v)
    ans = []
    if my_time[seller[0]] <= 0:
        ans.append(seller[0])
    time = 0
    pre = 0
    while pre < 10:
        nxt = pre + 1
        dp = seller_time[seller[pre]]
        while nxt < 10 and dp[seller[nxt]] == 1e10:
            nxt += 1
        if nxt == 10:
            break
        time += dp[seller[nxt]]
        pre = nxt
        if my_time[seller[nxt]] <= time:
            ans.append(seller[nxt])
    print(min(ans) if ans else -1)

solve()