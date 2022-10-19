import sys
input = sys.stdin.readline

while 1:
    m, fm = map(int, input().split())
    if m == fm == 0: break
    print(m + fm)