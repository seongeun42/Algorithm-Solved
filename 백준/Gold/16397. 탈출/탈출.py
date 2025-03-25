from collections import deque

def solve():
    N, T, G = map(int, input().split())
    visited = [-1] * 100_000
    visited[N] = 0
    q = deque([N])
    while q:
        num = q.popleft()
        if num == G:
            print(visited[G])
            return
        if visited[num] < T:
            A = num + 1
            if A <= 99999 and visited[A] == -1:
                visited[A] = visited[num] + 1
                q.append(A)
            if num != 0:
                B = num * 2
                if B <= 99999:
                    B = list(str(B))
                    B[0] = str(int(B[0]) - 1)
                    B = int(''.join(B))
                    if visited[B] == -1:
                        visited[B] = visited[num] + 1
                        q.append(B)
    print("ANG")
    return

solve()