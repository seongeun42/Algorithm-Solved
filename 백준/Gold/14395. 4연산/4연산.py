from collections import deque

def solve():
    s, t = map(int, input().split())
    if s == t:
        return 0
    q = deque([(s, "")])
    visited = {s}
    while q:
        cur, path = q.popleft()
        if cur == t:
            return path
        # *
        nxt = cur * cur
        if 0 <= nxt <= t and nxt not in visited:
            visited.add(nxt)
            q.append((nxt, path + "*"))
        # +
        nxt = cur + cur
        if 0 <= nxt <= t and nxt not in visited:
            visited.add(nxt)
            q.append((nxt, path + "+"))
        # -는 0이라 필요X, /는 무조건 1
        if 1 not in visited:
            visited.add(1)
            q.append((1, path + "/"))
    return -1

print(solve())