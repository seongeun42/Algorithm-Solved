from itertools import permutations
import sys
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    A = [*map(int, input().split())]
    ans = 0
    for arr in permutations(A, N):
        weight = 500
        for v in arr:
            weight -= K
            weight += v
            if weight < 500:
                break
        else:
            ans += 1
    print(ans)

solve()