import sys
input = sys.stdin.readline

moum = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
while 1:
    s = input().strip()
    cnt = 0
    if s == "#":
        break
    for c in s:
        if c in moum:
            cnt += 1
    print(cnt)