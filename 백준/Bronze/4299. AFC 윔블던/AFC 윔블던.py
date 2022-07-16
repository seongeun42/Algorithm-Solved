h, c = map(int, input().split())
flag = 0
for i in range(h, -1, -1):
    if abs(2 * i - h) == c:
        print(i, h - i)
        flag = 1
        break
if flag == 0: print(-1)