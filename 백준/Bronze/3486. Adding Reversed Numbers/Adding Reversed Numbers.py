import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    a, b = input().rstrip().split()
    print(int(str(int(a[::-1]) + int(b[::-1]))[::-1]))