import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N, M, K = map(int, input().split())
        money = [*map(int, input().split())]
        hap = sum(money[:M])
        if N == M:
            print(1 if hap < K else 0)
            continue
        ans = 0
        for l in range(N):
            r = (l + M) % N
            hap -= money[l]
            hap += money[r]
            if hap < K:
                ans += 1
        print(ans)

solve()