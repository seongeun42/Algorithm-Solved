import sys
input = sys.stdin.readline

def check(S):
    # D: 0 ~ len(S) - 2
    for d in range(len(S) - 1):
        pair = set()
        for i in range(len(S) - d - 1):
            if (S[i], S[i + d + 1]) in pair:
                print(f"{S} is NOT surprising.")
                return
            pair.add((S[i], S[i + d + 1]))
    print(f"{S} is surprising.")

while 1:
    S = input().rstrip()
    if S == "*":
        break
    check(S)