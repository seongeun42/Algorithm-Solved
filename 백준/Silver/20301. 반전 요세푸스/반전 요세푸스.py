from collections import deque
N, K, M = map(int, input().split())
dq = deque([i for i in range(1, N + 1)])
cnt = 0
while dq:
    if cnt == 2 * M:
        cnt = 0
    if cnt < M:
        for i in range(K - 1):
            dq.append(dq.popleft())
        print(dq.popleft())
    elif cnt < 2 * M:
        for i in range(K - 1):
            dq.appendleft(dq.pop())
        print(dq.pop())
    cnt += 1