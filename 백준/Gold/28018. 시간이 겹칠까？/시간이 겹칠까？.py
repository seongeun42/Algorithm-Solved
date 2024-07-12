import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    time = [0] * 1000002
    for _ in range(N):
        S, E = map(int, input().split())
        time[S] += 1
        time[E + 1] -= 1
    cnt = [0] * 1000002
    for i in range(1, 1000002):
        cnt[i] += cnt[i - 1] + time[i]
    Q = int(input())
    arr = [*map(int, input().split())]
    for c in arr:
        print(cnt[c])

solve()