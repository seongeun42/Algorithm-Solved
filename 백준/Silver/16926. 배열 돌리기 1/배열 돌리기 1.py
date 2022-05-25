import sys
input = sys.stdin.readline

def rotate(sr, er, sc, ec, rot):
    ccnt, rcnt = ec - sc + 1, er - sr + 1
    if ccnt == 1:
        cnt = rcnt
    elif rcnt == 1:
        cnt = ccnt
    else:
        cnt = ccnt * 2 + rcnt * 2 - 4
    rot %= cnt

    tmp = arr[sr][sc:ec + 1]
    for i in range(sr + 1, er + 1):
        tmp.append(arr[i][ec])
    tmp += arr[er][sc:ec][::-1]
    for i in range(er - 1, sr, -1):
        tmp.append(arr[i][sc])
    tmp = tmp[rot:] + tmp[:rot]

    idx = 0
    for i in range(sc, ec + 1):
        ans[sr][i] = tmp[idx]
        idx += 1
    for i in range(sr + 1, er + 1):
        ans[i][ec] = tmp[idx]
        idx += 1
    for i in range(ec - 1, sc - 1, -1):
        ans[er][i] = tmp[idx]
        idx += 1
    for i in range(er - 1, sr, -1):
        ans[i][sc] = tmp[idx]
        idx += 1

N, M, R = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
ans = [[0] * M for _ in range(N)]
for i in range(min(N, M) // 2):
    rotate(i, N - 1 - i, i, M - 1 - i, R)
for a in ans:
    print(*a)