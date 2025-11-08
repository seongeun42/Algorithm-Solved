import sys
input = sys.stdin.readline

while 1:
    s = input().rstrip()
    if s == '#':
        break
    cnt = s.count('1')
    if s[-1] == 'e':
        print(s[:-1] + ("1" if cnt % 2 else "0"))
    else:
        print(s[:-1] + ("0" if cnt % 2 else "1"))