n = int(input())
cl = [-1] * 11
ans = 0
for _ in range(n):
    c, l = map(int, input().split())
    if cl[c] == -1:
        cl[c] = l
    elif cl[c] != l:
        cl[c] = l
        ans += 1
print(ans)