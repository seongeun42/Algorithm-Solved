import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    G = int(input())
    nums = [int(input()) for _ in range(G)]
    m = G
    while 1:
        mod = set()
        for num in nums:
            v = num % m
            if v in mod:
                break
            mod.add(v)
        if len(mod) == G:
            print(m)
            break
        m += 1