import sys
input = sys.stdin.readline
while 1:
    s = input().strip()
    if s == "END": break
    print(s[::-1])