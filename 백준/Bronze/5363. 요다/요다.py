import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    sent = list(input().rstrip().split())
    ans = sent[2:] + sent[:2]
    print(*ans)