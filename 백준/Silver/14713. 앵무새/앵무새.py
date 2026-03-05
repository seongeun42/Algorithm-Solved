import sys
input = sys.stdin.readline

N = int(input())
words = {}
for i in range(N):
    S = input().rstrip().split()
    for j, w in enumerate(S):
        if w not in words:
            words[w] = (i, j)
chk = [-1] * N
L = list(input().rstrip().split())
if len(L) != len(words):
    print("Impossible")
else:
    ans = "Impossible"
    for w in L:
        if w not in words:
            break
        num, idx = words[w]
        if chk[num] < idx:
            chk[num] = idx
        else:
            break
    else:
        ans = "Possible"
    print(ans)