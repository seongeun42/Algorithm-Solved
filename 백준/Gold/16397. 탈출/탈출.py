from collections import deque

def solve():
    N, T, G = map(int, input().split())
    visited = {N}
    q = deque([(N, 0)])
    while q:
        num, cnt = q.popleft()
        if num == G:
            print(cnt)
            return
        if cnt < T:
            A = num + 1
            if A <= 99999 and A not in visited:
                visited.add(A)
                q.append((A, cnt + 1))
            if num != 0:
                B = num * 2
                if B <= 99999:
                    B = list(str(B))
                    B[0] = str(int(B[0]) - 1)
                    B = int(''.join(B))
                    if B not in visited:
                        visited.add(B)
                        q.append((B, cnt + 1))
    print("ANG")
    return

solve()