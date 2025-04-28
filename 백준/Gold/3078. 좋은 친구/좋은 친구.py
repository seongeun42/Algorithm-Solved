import sys
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split()) 
    names = [len(input().rstrip()) for _ in range(N)]
    ans = 0
    cnt = [0] * 21
    for i in range(K + 1):
        ans += cnt[names[i]]
        cnt[names[i]] += 1
    for i in range(N - K - 1):
        cnt[names[i]] -= 1
        name = names[i + K + 1]
        ans += cnt[name]
        cnt[name] += 1
    print(ans)

solve()