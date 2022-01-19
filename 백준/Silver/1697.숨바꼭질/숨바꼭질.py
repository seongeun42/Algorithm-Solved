from collections import deque
def bfs(check, start, target):
    check[start] = 0
    q = deque([start])
    while q:
        v = q.popleft()
        if v * 2 <= target + 1 and check[v * 2] == -1:
            check[v * 2] = check[v] + 1
            q.append(v * 2)
        if v > 0 and check[v - 1] == -1:
            check[v - 1] = check[v] + 1
            q.append(v - 1)
        if v <= target and check[v + 1] == -1:
            check[v + 1] = check[v] + 1
            q.append(v + 1)

n, k = map(int, input().split())
if n >= k: print(n - k)
else:
    check = [-1] * (k + 2)
    bfs(check, n, k)
    print(check[k])