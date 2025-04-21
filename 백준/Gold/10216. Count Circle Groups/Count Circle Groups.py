import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        R = list(range(N))
        circle = [tuple(map(int, input().split())) for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                ir = find_root(i, R)
                jr = find_root(j, R)
                if ir != jr:
                    a1, b1, r1 = circle[i]
                    a2, b2, r2 = circle[j]
                    if (a1 - a2) ** 2 + (b1 - b2) ** 2 <= (r1 + r2) ** 2:
                        R[min(ir, jr)] = max(ir, jr)
        cnt = 0
        for i in range(N):
            if find_root(i, R) == i:
                cnt += 1
        print(cnt)

solve()