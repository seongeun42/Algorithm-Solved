n, m = map(int, input().split())
T = [*map(int, input().split())]
pay = sum(T[:m])
ans = pay
for i in range(n - m):
    pay -= T[i]
    pay += T[i + m]
    if ans < pay:
        ans = pay
print(ans)