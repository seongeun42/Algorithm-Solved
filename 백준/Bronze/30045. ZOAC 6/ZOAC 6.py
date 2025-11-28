import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
for _ in range(N):
    S = input().rstrip()
    if "01" in S or "OI" in S:
        cnt += 1
print(cnt)