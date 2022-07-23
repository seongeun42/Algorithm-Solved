import sys
input = sys.stdin.readline

N = int(input())
remain = 0
for _ in range(N):
    s, a = map(int, input().split())
    remain += a % s
print(remain)