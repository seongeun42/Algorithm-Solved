import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
cut = [0] + [int(input()) for _ in range(M)] + [L]
for _ in range(N):
    cnt = int(input())
    s, e = 0, L
    ans = 0
    while s <= e:
        mid = (s + e) // 2
        cur_cnt = 0
        prev_cut = 0
        for i, v in enumerate(cut):
            if v - prev_cut >= mid:
                cur_cnt += 1
                prev_cut = v
        if cur_cnt <= cnt:
            e = mid - 1
        else:
            s = mid + 1
    print(e)