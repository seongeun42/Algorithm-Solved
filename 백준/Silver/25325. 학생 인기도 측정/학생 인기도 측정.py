import sys
input = sys.stdin.readline

n = int(input())
rank = dict(zip([*input().rstrip().split()], [0] * n))
for _ in range(n):
    names = [*input().rstrip().split()]
    for name in names:
        rank[name] += 1
rank = sorted(list(rank.items()), key=lambda x: (-x[1], x[0]))
for r in rank:
    print(*r)