S = list(input())
s, e = 0, 0
while e < len(S):
    if S[e] == '<':
        while S[e] != '>':
            e += 1
        e += 1
    elif S[e].isalnum():
        s = e
        while e < len(S) and S[e].isalnum():
            e += 1
        rvs = reversed(S[s:e])
        S[s:e] = rvs
    else: e += 1
print(''.join(S))