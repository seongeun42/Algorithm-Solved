p = [*map(int, input().split())]
x, y, r = map(int, input().split())
flag = 0
for i in range(4):
    if x == p[i]:
        print(i + 1)
        flag = 1
        break
if flag == 0:
    print(0)