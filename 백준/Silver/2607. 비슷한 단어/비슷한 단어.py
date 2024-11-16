import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    word = list(input().strip())
    ans = 0
    for _ in range(N - 1):
        candi = list(input().strip())
        compare = word[:]
        cnt = 0
        for c in candi:
            if c in compare:
                compare.remove(c)
            else:
                cnt += 1
        if cnt < 2 and len(compare) < 2:
            ans += 1
    print(ans)

solve()