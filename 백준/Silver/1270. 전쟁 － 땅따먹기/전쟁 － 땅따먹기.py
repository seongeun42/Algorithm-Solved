import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    T = [*map(int, input().split())]
    cnt = {}
    for c in T[1:]:
        cnt[c] = cnt.get(c, 0) + 1
        if cnt[c] > T[0] // 2:
            print(c)
            break
    else:
        print("SYJKGW")