t = int(input())
for _ in range(t):
    lt, wt, le, we = map(int, input().split())
    t, e = lt * wt, le * we
    if t > e: print("TelecomParisTech")
    elif t < e: print("Eurecom")
    else: print("Tie")