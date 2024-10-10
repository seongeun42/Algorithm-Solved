import sys
input = sys.stdin.readline

T = int(input())
for i in range(1, T + 1):
    g = [1, 2, 3, 3, 4, 10]
    s = [1, 2, 2, 2, 3, 5, 10]
    gnum = [*map(int, input().split())]
    snum = [*map(int, input().split())]
    gs = sum([gnum[i] * g[i] for i in range(6)])
    ss = sum([snum[i] * s[i] for i in range(7)])
    if gs == ss:
        print(f"Battle {i}: No victor on this battle field")
    elif gs > ss:
        print(f"Battle {i}: Good triumphs over Evil")
    else:
        print(f"Battle {i}: Evil eradicates all trace of Good")