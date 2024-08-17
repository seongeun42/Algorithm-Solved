import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = input().rstrip()
    v = str(int(N) + int(N[::-1]))
    print("YES" if v == v[::-1] else "NO")