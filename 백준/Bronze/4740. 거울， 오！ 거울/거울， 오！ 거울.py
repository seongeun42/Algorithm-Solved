import sys
input = sys.stdin.readline

while 1:
    s = input().rstrip('\n')
    if s == "***":
        break
    print(s[::-1])