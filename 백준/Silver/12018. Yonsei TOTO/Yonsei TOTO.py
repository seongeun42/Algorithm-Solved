import sys
input = sys.stdin.readline

n, m = map(int, input().split())
need = []
for _ in range(n):
    p, l = map(int, input().split())
    use = sorted([*map(int, input().split())], reverse=True)
    need.append(1 if p < l else use[l - 1])
need.sort()
ans = 0
for v in need:
    if v <= m:
        ans += 1
        m -= v
print(ans)