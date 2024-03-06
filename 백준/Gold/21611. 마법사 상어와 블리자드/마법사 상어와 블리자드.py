import sys
input = sys.stdin.readline

# 1차 배열로 변환
def change_arr(N, arr):
    marbles = []
    # 좌하우상
    cdx = [-1, 0, 1, 0]
    cdy = [0, 1, 0, -1]
    d = 0
    length = 1
    cnt = 0
    ny = nx = (N + 1) // 2 - 1
    while 0 <= nx < N and 0 <= ny < N:
        # 두 번 돌았으면 cnt, length 갱신
        if cnt == 2:
            length += 1
            cnt = 0
        leng = 0
        while leng < length:
            ny += cdy[d]
            nx += cdx[d]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[ny][nx] == 0:
                    return marbles
                marbles.append(arr[ny][nx])
            else:
                break
            leng += 1
        d = (d + 1) % 4
        cnt += 1
    return marbles

def explosion(marbles, cnt):
    done = False
    while not done:
        tmp = []
        equal_cnt = 0
        flag = True
        while marbles:
            v = marbles.pop()
            if not tmp or tmp[-1] == v:
                equal_cnt += 1
            else:
                if equal_cnt >= 4:
                    flag = False
                    k = tmp[-1]
                    while tmp and tmp[-1] == k:
                        tmp.pop()
                        cnt[k - 1] += 1
                equal_cnt = 1
            tmp.append(v)
        if equal_cnt >= 4:
            flag = False
            k = tmp[-1]
            while tmp and tmp[-1] == k:
                tmp.pop()
                cnt[k - 1] += 1
            equal_cnt = 1
        marbles = tmp[::-1]
        done = flag
    return marbles


def marble_change(marbles, N):
    new_marbles = []
    marbles = marbles[::-1]
    max_n = N * N - 1
    while marbles and len(new_marbles) < max_n:
        tmp = []
        k = marbles[-1]
        while marbles and marbles[-1] == k:
            tmp.append(marbles.pop())
        new_marbles.append(len(tmp))
        if len(new_marbles) < max_n:
            new_marbles.append(k)
    return new_marbles


def solve():
    N, M = map(int, input().split())
    arr = [[*map(int, input().split())] for _ in range(N)]
    marbles = change_arr(N, arr)

    # 상하좌우
    b_index = [[6, 21], [2, 13], [0, 9], [4, 17]]
    for i in range(7, 50, 2):
        k = i // 2 - 1
        for j in range(4):
            b_index[j].append(b_index[j][k - 1] * 2 - b_index[j][k - 2] + 8)

    cnt = [0] * 3

    for _ in range(M):
        # 블리자드
        d, s = map(int, input().split())
        d -= 1
        del_list = b_index[d][:s][::-1]
        for idx in del_list:
            if idx < len(marbles):
                del marbles[idx]
        # 구슬 폭발
        marbles = explosion(marbles, cnt)
        # 구슬 변환
        marbles = marble_change(marbles, N)
        
    print(cnt[0] + 2 * cnt[1] + 3 * cnt[2])
    
solve()