from itertools import product
N, K = map(int, input().split())
elem = list(input().split())
length = len(str(N))
for i in range(length, 0, -1):
    arr = sorted([*map(list, product(elem, repeat=i))], reverse=True)
    for v in arr:
        v = int(''.join(v))
        if v <= N:
            print(v)
            exit()