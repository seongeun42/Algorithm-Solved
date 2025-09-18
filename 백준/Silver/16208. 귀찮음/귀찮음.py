n = int(input())
l = [*map(int, input().split())]
left = sum(l)
ans = 0
while l:
    v = l.pop()
    ans += (left - v) * v
print(ans // 2)