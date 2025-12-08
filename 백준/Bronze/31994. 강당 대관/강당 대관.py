ans = [0, 0]
for _ in range(7):
    name, cnt = input().split()
    cnt = int(cnt)
    if ans[1] < cnt:
        ans = [name, cnt]
print(ans[0])