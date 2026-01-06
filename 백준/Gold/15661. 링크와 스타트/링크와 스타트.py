from itertools import combinations
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    S = [[*map(int, input().split())] for _ in range(N)]
    ans = 100000
    for i in range(1, N // 2 + 1):
        for start in combinations(range(N), i):
            link = set(range(N)) - set(start)
            s_score, l_score = 0, 0
            for si in start:
                for sj in start:
                    s_score += S[si][sj]
            for li in link:
                for lj in link:
                    l_score += S[li][lj]
            cha = abs(s_score - l_score)
            if cha < ans:
                ans = cha
    print(ans)
solve()