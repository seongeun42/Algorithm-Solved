import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    start, end = [], []
    for _ in range(N):
        s, e = map(int, input().split())
        start.append(s)
        end.append(e)
    start.sort()
    end.sort()
    ans, cnt = 0, 0
    e = 0
    for s in start:
        cnt += 1
        if e < len(end) and end[e] <= s:
            cnt -= 1
            e += 1
        if ans < cnt:
            ans = cnt
    print(ans)

solve()