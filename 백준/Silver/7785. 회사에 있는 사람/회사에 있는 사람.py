import sys
input = sys.stdin.readline

n = int(input())
p = set()
for _ in range(n):
    name, be = input().split()
    if be == "enter":
        p.add(name)
    else:
        p.discard(name)

for v in sorted(list(p), reverse=True):
    print(v)