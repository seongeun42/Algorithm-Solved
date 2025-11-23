import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    cnt = [int(input()) for _ in range(n)]
    elec, max_v, max_cnt, total_v = -1, 0, 0, 0
    for i, v in enumerate(cnt):
        if max_v < v:
            max_v = v
            elec = i
            max_cnt = 1
        elif max_v == v:
            max_cnt += 1
        total_v += v
    if max_cnt > 1:
        print("no winner")
    elif max_v > total_v // 2:
        print(f"majority winner {elec + 1}")
    else:
        print(f"minority winner {elec + 1}")