import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    begin, time = map(int, input().split())
    print(begin + time // 4 - time // 7)
