import sys
input = sys.stdin.readline

N = int(input())
sn = [int(input()) for _ in range(N)]
leng = len(str(sn[0]))
for i in range(1, leng + 1):
    chk = set()
    for c in sn:
        chk.add(c % (10 ** i))
    if len(chk) == N:
        print(i)
        break