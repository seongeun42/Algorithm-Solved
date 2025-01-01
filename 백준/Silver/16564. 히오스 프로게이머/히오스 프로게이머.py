import sys
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    X = sorted([int(input()) for _ in range(N)])
    ans = X[0]
    start, end = X[0], X[-1] + K
    while start <= end:
        mid = (start + end) // 2
        need = 0
        for l in X:
            if l >= mid:
                break
            need += mid - l
        if need <= K:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    print(ans)

solve()