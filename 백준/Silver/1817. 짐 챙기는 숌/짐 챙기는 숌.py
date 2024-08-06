import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    if N == 0:
        print(0)
        return
    books = [*map(int, input().split())]
    ans = 1
    weight = 0
    for i in range(N):
        if weight + books[i] <= M:
            weight += books[i]
        else:
            weight = books[i]
            ans += 1
    print(ans)

solve()