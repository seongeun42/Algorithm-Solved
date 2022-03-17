from itertools import combinations as combi
L, C = map(int, input().split())
cha = sorted(list(input().split()))
mu = {'a', 'e', 'i', 'o', 'u'}
for v in combi(cha, L):
    if list(v) == sorted(v):
        if len(set(v) & mu) >= 1 and len(set(v) - mu) >= 2:
            print(''.join(v))