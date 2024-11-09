import sys
input = sys.stdin.readline

def backtack(word, cnt, cur, ans):
    if len(cur) == len(word):
        ans.append(cur)
        return
    for c in cnt:
        if cnt[c]:
            cnt[c] -= 1
            backtack(word, cnt, cur + c, ans)
            cnt[c] += 1

def solve():
    N = int(input())
    for _ in range(N):
        word = sorted(list(input().rstrip()))
        cnt = {}
        for c in word:
            cnt[c] = cnt.get(c, 0) + 1
        ans = []
        backtack(word, cnt, "", ans)
        print("\n".join(ans))

solve()