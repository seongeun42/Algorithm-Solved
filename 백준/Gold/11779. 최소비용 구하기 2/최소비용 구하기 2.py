import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    dp[start] = 0
    while hq:
        s_w, s_n = heapq.heappop(hq)
        if dp[s_n] < s_w:
            continue
        for w, e_n in G[s_n]:
            e_w = s_w + w
            if e_w < dp[e_n]:
                dp[e_n] = e_w
                preCity[e_n] = s_n
                heapq.heappush(hq, (e_w, e_n))

n = int(input())
m = int(input())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    G[s].append((c, e))
dp = [1e9] * (n + 1)
preCity = [0] * (n + 1)
sc, ec = map(int, input().split())
dijkstra(sc)

city = []
cur = ec
while preCity[cur] != 0:
    city.append(cur)
    cur = preCity[cur]
city = [sc] + city[::-1]
print(dp[ec])
print(len(city))
print(*city)