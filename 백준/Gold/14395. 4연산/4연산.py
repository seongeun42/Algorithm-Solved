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
        if -s <= nxt <= t * 2 and nxt not in visited:
            visited.add(nxt)
            q.append((nxt, path + "*"))
        # +
        nxt = cur + cur
        if -s <= nxt <= t * 2 and nxt not in visited:
            visited.add(nxt)
            q.append((nxt, path + "+"))
        # -
        nxt = cur - cur
        if -s <= nxt <= t * 2 and nxt not in visited:
            visited.add(nxt)
            q.append((nxt, path + "-"))
        # /
        if cur != 0:
            nxt = cur // cur
            if -s <= nxt <= t * 2 and nxt not in visited:
                visited.add(nxt)
                q.append((nxt, path + "/"))
    return -1

print(solve())