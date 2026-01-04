import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M = input().rstrip()
    alpha = {}
    i = 0
    while i < len(M):
        if M[i] in alpha and alpha[M[i]] % 3 == 2:
            alpha[M[i]] = alpha.get(M[i], 0) + 1
            if i + 1 == len(M) or M[i] != M[i + 1]:
                print("FAKE")
                break
            i += 2
        else:
            alpha[M[i]] = alpha.get(M[i], 0) + 1
            i += 1
    else:
        print("OK")