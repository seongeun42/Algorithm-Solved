import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    ht = []
    for _ in range(N):
        ht.append([*map(int, input().split())])
    if ht[0][0] == 0:
        ht[0][0] = 1e9
    if ht[0][1] == 0:
        ht[0][1] = -1
    if ht[-1][0] == 0:
        ht[-1][0] == -1
    if ht[-1][1] == 0:
        ht[-1][1] = 1e9
    min_y_h = [ht[0][0]] * N
    max_y_t = [ht[0][1]] * N
    max_o_h = [ht[-1][0]] * N
    min_o_t = [ht[-1][1]] * N
    for k in range(1, N - 1):
        min_y_h[k] = min(ht[k][0], min_y_h[k - 1]) if ht[k][0] != 0 else min_y_h[k - 1]
        max_y_t[k] = max(ht[k][1], max_y_t[k - 1]) if ht[k][1] != 0 else max_y_t[k - 1]
        max_o_h[N - k - 1] = max(ht[N - k - 1][0], max_o_h[N - k]) if ht[N - k - 1][0] != 0 else max_o_h[N - k]
        min_o_t[N - k - 1] = min(ht[N - k - 1][1], min_o_t[N - k]) if ht[N - k - 1][1] != 0 else min_o_t[N - k]
    for k in range(N - 2, -1, -1):
        if min_y_h[k] > max_o_h[k + 1] and max_y_t[k] < min_o_t[k + 1]:
            print(k + 1)
            return
    print(-1)

solve()