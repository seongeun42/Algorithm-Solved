from collections import deque
def bfs(cnt):
    q = deque([1])
    while q:
        cur = q.popleft()
        for i in range(1, 7):
            v = cur + i
            next = la_sn[v] if v in la_sn else v
            if next <= 100 and cnt[next] == 0:
                cnt[next] = cnt[cur] + 1
                q.append(next)
    return cnt[100]

n, m = map(int, input().split())
la_sn = {}
for _ in range(n+m):
    k, v = map(int, input().split())
    la_sn[k] = v
cnt = [0] * 101
print(bfs(cnt))