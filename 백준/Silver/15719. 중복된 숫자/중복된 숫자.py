N = int(input())
arr = input()
ans = -(N * (N - 1) // 2)
num = 0
for c in arr:
    if c == ' ':
        ans += num
        num = 0
    else:
        num *= 10
        num += int(c)
ans += num
print(ans)