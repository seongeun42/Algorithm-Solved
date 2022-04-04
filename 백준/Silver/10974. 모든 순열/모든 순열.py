from itertools import permutations as permu
N = int(input())
for v in permu(range(1, N + 1), N):
    print(*v)