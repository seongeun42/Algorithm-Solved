n = int(input())
cnt = 0
for num in range(1, n + 1):
    for c in str(num):
        if c in "369":
            cnt += 1
print(cnt)