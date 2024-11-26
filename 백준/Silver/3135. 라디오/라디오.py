import sys
input = sys.stdin.readline

def solve():
    A, B = map(int, input().split())
    ans = abs(A - B)
    N = int(input())
    for _ in range(N):
        fixed = int(input())
        if abs(fixed - B) < ans:
            ans = abs(fixed - B) + 1
    print(ans)

solve()