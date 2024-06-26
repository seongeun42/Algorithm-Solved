A, B = map(int, input().split())
num, cnt, ans = 1, 1, 0
for i in range(1, B + 1):
    if A <= i <= B:
        ans += num
    cnt -= 1
    if cnt == 0:
        num += 1
        cnt = num
print(ans)