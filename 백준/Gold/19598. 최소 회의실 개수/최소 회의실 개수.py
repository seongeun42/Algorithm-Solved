from collections import defaultdict
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    time = defaultdict(int)
    for _ in range(N):
        s, e = map(int, input().split())
        time[s] += 1
        time[e] -= 1
    time = sorted(time.items())
    ans, cnt = 0, 0
    for t, v in time:
        cnt += v
        if ans < cnt:
            ans = cnt
    print(ans)

solve()