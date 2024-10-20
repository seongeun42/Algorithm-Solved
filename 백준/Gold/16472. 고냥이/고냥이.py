import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    S = input().rstrip()
    alpa = {S[0]: 1}
    cnt = 1
    l, r = 0, 0
    ans = 1
    while l <= r and r < len(S) - 1:
        r += 1
        if alpa.get(S[r], 0) == 0:
            cnt += 1
        alpa[S[r]] = alpa.get(S[r], 0) + 1
        while cnt > N:
            alpa[S[l]] -= 1
            if alpa[S[l]] == 0:
                cnt -= 1
            l += 1
        if ans < r - l + 1:
            ans = r - l + 1
    print(ans)

solve()