import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s, p = input().rstrip().split()
    s = s.replace(p, "a")
    print(len(s))