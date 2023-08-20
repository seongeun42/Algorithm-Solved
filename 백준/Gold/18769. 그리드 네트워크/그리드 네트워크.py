import sys, heapq
input = sys.stdin.readline

def find_root(node, R):
    if R[node] != node:
        R[node] = find_root(R[node], R)
    return R[node]

def solve():
    T = int(input())
    for _ in range(T):
        R, C = map(int, input().split())
        E = []
        for i in range(R):
            c = [*map(int, input().split())]
            for j in range(C - 1):
                n = i * C + j
                heapq.heappush(E, (c[j], n, n + 1))
        for i in range(R - 1):
            c = [*map(int, input().split())]
            for j in range(C):
                n = i * C + j
                heapq.heappush(E, (c[j], n, n + C))
        R = [i for i in range(R * C)]
        ans = 0
        while E:
            w, a, b = heapq.heappop(E)
            ar = find_root(a, R)
            br = find_root(b, R)
            if ar != br:
                ans += w
                R[max(ar, br)] = min(ar, br)
        print(ans)

solve()