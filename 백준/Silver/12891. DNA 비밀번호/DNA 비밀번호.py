def check():
    for i in range(4):
        if acgt[i] > cnt[i]:
            return 0
    return 1

sLen, pLen = map(int, input().split())
S = input()
idx = { 'A': 0, 'C': 1, 'G': 2, 'T': 3 }
acgt = [*map(int, input().split())]
cnt = [0, 0, 0, 0]
for i in range(pLen):
    cnt[idx[S[i]]] += 1
ans = check()
for i in range(pLen, sLen):
    cnt[idx[S[i]]] += 1
    cnt[idx[S[i - pLen]]] -= 1
    ans += check()
print(ans)