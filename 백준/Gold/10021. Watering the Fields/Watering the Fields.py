import sys, heapq
input = sys.stdin.readline

def find_root(R, n):
    if R[n] != n:
        R[n] = find_root(R, R[n])
    return R[n]

def solve():
    N, C = map(int, input().split())
    fields = [tuple(map(int, input().split())) for _ in range(N)]
    E = []
    for i in range(N):
        for j in range(i + 1, N):
            cost = (fields[i][0] - fields[j][0]) ** 2 + (fields[i][1] - fields[j][1]) ** 2
            if cost >= C:
                heapq.heappush(E, (cost, i, j))
    R = [i for i in range(N)]
    ans = 0
    cnt = 1
    while E:
        cost, i, j = heapq.heappop(E)
        if cnt == N:
            break
        ir = find_root(R, i)
        jr = find_root(R, j)
        if ir != jr:
            ans += cost
            cnt += 1
            R[max(ir, jr)] = min(ir, jr)
    print(ans if cnt == N else -1)

solve()