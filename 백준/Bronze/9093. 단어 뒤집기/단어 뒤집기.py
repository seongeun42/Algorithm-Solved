import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    words = map(reversed, input().split())
    for w in words:
        print(''.join(w), end=' ')