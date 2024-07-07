from collections import defaultdict
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    ex = defaultdict(int)
    for _ in range(N):
        e, x = map(int, input().split())
        ex[e] += 1
        ex[x] -= 1
    ex = sorted(ex.items(), key=lambda x: x[0])
    cnt = 0
    term = [0, 0]
    prefix_sum = 0
    chk = False
    for i in range(len(ex)):
        prefix_sum += ex[i][1]
        if prefix_sum > cnt:
            cnt = prefix_sum
            term[0] = ex[i][0]
            chk = True
        elif prefix_sum < cnt and chk:
            term[1] = ex[i][0]
            chk = False
    print(cnt)
    print(*term)

solve()