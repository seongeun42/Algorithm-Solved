import sys
input = sys.stdin.readline

s = set()
res = 0
for _ in range(5):
    v = int(input())
    if v in s:
        res -= v
        s.discard(v)
    else:
        s.add(v)
        res += v
print(res)