from collections import deque

def solve():
    S = int(input())
    q = deque([(1, 0)])
    time = [[-1] * (S + 1) for _ in range(S + 1)]
    time[1][0] = 0
    while q:
        cnt, copy_cnt = q.popleft()
        if time[cnt][cnt] == -1:
            time[cnt][cnt] = time[cnt][copy_cnt] + 1
            q.append((cnt, cnt))
        if cnt + copy_cnt <= S and time[cnt + copy_cnt][copy_cnt] == -1:
            time[cnt + copy_cnt][copy_cnt] = time[cnt][copy_cnt] + 1
            q.append((cnt + copy_cnt, copy_cnt))
        if cnt - 1 >= 0 and time[cnt - 1][copy_cnt] == -1:
            time[cnt - 1][copy_cnt] = time[cnt][copy_cnt] + 1
            q.append((cnt - 1, copy_cnt))

    ans = 10000
    for i in range(S + 1):
        if time[S][i] != -1 and ans > time[S][i]:
            ans = time[S][i]
    return ans

print(solve())