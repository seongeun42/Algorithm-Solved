import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    div, mod = divmod(n, 5)
    ans = ["++++"] * div + ['|' * mod]
    print(' '.join(ans))