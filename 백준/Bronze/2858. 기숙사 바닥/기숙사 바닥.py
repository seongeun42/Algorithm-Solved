R, B = map(int, input().split())
rcnt = (R - 4) // 2
for i in range(1, rcnt):
    if i * (rcnt - i) == B:
        print(rcnt - i + 2, i + 2)
        break