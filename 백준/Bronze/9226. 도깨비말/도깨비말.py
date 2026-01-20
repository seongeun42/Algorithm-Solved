import sys
input = sys.stdin.readline

while 1:
    S = input().rstrip()
    if S == "#":
        break
    for i, c in enumerate(S):
        if c in {'a', 'e', 'i', 'o', 'u'}:
            print(S[i:] + S[:i] + "ay")
            break
    else:
        print(S + "ay")