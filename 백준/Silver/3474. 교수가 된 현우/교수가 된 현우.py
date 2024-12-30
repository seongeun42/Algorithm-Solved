import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        cnt = 0
        while N > 0:
            cnt += N // 5
            N //= 5
        print(cnt)

solve()