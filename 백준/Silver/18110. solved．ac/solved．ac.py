import sys
input = sys.stdin.readline

def r(n):
    return int(n) if n - int(n) < 0.5 else int(n) + 1

n = int(input())
s = sorted([int(input()) for _ in range(n)])
ex = r(n * 0.15)
print(r(sum(s[ex:n - ex]) / (n - (ex * 2))) if n else 0)