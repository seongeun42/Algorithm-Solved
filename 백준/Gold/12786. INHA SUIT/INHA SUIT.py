import sys, heapq
input = sys.stdin.readline

def solve():
    N = int(input())
    K = int(input())
    tree = [[]]
    dp = {(0, 1): 0}
    for i in range(N):
        hole = [*map(int, input().split())]
        for v in hole[1:]:
            dp[(i + 1, v)] = 1e9
        tree.append(set(hole[1:]))
    hq = [(0, 1, 0)]
    while hq:
        c_w, c_h, c_t = heapq.heappop(hq)
        if dp[(c_t, c_h)] < c_w:
            continue
        for n_h in tree[c_t + 1]:
            w = c_w
            if n_h not in {c_h, c_h + 1, c_h - 1, min(c_h * 2, 20)}:
                if c_w < K:
                    w += 1
                else:
                    continue
            if w < dp[(c_t + 1, n_h)]:
                dp[(c_t + 1, n_h)] = w
                if c_t + 1 < N:
                    heapq.heappush(hq, (w, n_h, c_t + 1))
    ans = 1e9
    for h in tree[-1]:
        if dp[(N, h)] < ans:
            ans = dp[(N, h)]
    print(ans if ans != 1e9 else -1)

solve()