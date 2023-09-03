from collections import deque

def solve():
    N, L = map(int, input().split())
    A = [*map(int, input().split())]
    ans = []
    q = deque()
    for i in range(N):
        v = A[i]
        while q and q[-1] > v:
            q.pop()
        q.append(v)
        if i >= L and q[0] == A[i - L]:
            q.popleft()
        ans.append(q[0])
    print(*ans)

solve()