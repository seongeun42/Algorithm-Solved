import sys
input = sys.stdin.readline

while 1:
    S = input().rstrip()
    if S == '#':
        break
    S = S.lower()
    alpa = set()
    for c in S:
        if c.isalpha():
            alpa.add(c)
    print(len(alpa))
            