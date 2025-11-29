import sys
input = sys.stdin.readline

G = 0
while 1:
    n = int(input())
    if n == 0:
        break
    G += 1
    name = []
    bad = []
    for _ in range(n):
        S = input().rstrip().split()
        name.append(S[0])
        for i in range(1, len(S)):
            if S[i] == 'N':
                cur = len(name) - 1
                bad.append((cur, (cur - i) % n))
    print(f"Group {G}")
    if len(bad) == 0:
        print("Nobody was nasty")
    else:
        for i, j in bad:
            print(f"{name[j]} was nasty about {name[i]}")
    print()