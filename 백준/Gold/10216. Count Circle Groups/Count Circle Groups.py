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
        circle = []
        for i in range(N):
            a1, b1, r1 = map(int, input().split())
            for j, v in enumerate(circle):
                a2, b2, r2 = v
                if (a1 - a2) ** 2 + (b1 - b2) ** 2 <= (r1 + r2) ** 2:
                    ir = find_root(i, R)
                    jr = find_root(j, R)
                    if ir != jr:
                        R[min(ir, jr)] = max(ir, jr)
            circle.append((a1, b1, r1))
        cnt = 0
        for i in range(N):
            if find_root(i, R) == i:
                cnt += 1
        print(cnt)

solve()