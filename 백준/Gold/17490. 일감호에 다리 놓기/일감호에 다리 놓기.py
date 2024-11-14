import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, M, K = map(int, input().split())
    need = sorted(list(zip([*map(int, input().split())], range(1, N + 1))))
    R = [0] + list(range(N))
    R[1] = 1
    connect = 1
    last_connected = True
    for _ in range(M):
        a, b = map(int, input().split())
        a, b = min(a, b), max(a, b)
        if (a, b) == (1, N):
            last_connected = False
        R[b] = b
        connect += 1
    if last_connected:
        nr = find_root(N, R)
        R[nr] = 1
        connect -= 1
    if M <= 1:
        print("YES")
        return
    total = 0
    for cnt, num in need:
        root = find_root(num, R)
        if root != 0:
            R[root] = 0
            total += cnt
            connect -= 1
        if connect == 0:
            break
    print("YES" if total <= K else "NO")

solve()