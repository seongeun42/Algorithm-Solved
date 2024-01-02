import sys
input = sys.stdin.readline

N = int(input())
patr = input().rstrip().split('*')
length = len(patr[0]) + len(patr[1])
for _ in range(N):
    S = input().rstrip()
    print("DA" if len(S) >= length and S.startswith(patr[0]) and S.endswith(patr[1]) else "NE")