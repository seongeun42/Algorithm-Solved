from collections import deque

A, K = map(int, input().split())
q = deque([A])
arr = [-1] * (K + 1)
arr[A] = 0
while q:
    cur = q.popleft()
    if cur == K:
        print(arr[K])
    if cur + 1 <= K and arr[cur + 1] == -1:
        arr[cur + 1] = arr[cur] + 1
        q.append(cur + 1)
    if cur * 2 <= K and arr[cur * 2] == -1:
        arr[cur * 2] = arr[cur] + 1
        q.append(cur * 2)