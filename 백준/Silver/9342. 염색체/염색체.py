import sys, re
input = sys.stdin.readline

T = int(input())
chk = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(T):
    S = input().rstrip()
    print('Infected!' if chk.match(S) else 'Good')