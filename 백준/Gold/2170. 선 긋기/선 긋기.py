import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    line = sorted([[*map(int, input().split())] for _ in range(n)])
    s, e = line[0]
    ans = 0
    for i in range(1, n):
        ns, ne = line[i]
        if s <= ns <= e and e < ne:
            e = ne
        elif e < ns:
            ans += e - s
            s, e = ns, ne
    ans += e - s
    print(ans)

solve()