import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N = int(input())
    arr = sorted([[*map(int, input().split())] for _ in range(N)], key=lambda x: (-x[1], -x[0]))
    day = [i for i in range(N + 1)]
    ans = 0
    for deadline, cup in arr:
        solve_day = find_root(deadline, day)
        if solve_day == 0:
            continue
        ans += cup
        day[solve_day] = find_root(solve_day - 1, day)
    print(ans)

solve()