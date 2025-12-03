import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    S = input().rstrip()
    print(min(S.count('a'), S.count('b')))