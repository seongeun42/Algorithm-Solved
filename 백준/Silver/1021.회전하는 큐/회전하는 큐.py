from collections import deque
n, m = map(int, input().split())
s = list(map(int, input().split()))
q = deque(list(range(1, n + 1)))
cnt = 0
for i in range(m):
    loca = q.index(s[i])
    if loca > len(q) // 2:
        while q[-1] != s[i]:
            q.appendleft(q.pop())
            cnt += 1
        q.pop()
        cnt += 1
    else:
        while q[0] != s[i]:
            q.append(q.popleft())
            cnt += 1
        q.popleft()
print(cnt)