import sys
input = sys.stdin.readline

def garo(N, L, H):
    cnt = N
    for i in range(N):
        h = H[i][0]
        exist = [0] * N
        flag = True
        for j in range(N):
            if abs(H[i][j] - h) > 1:
                flag = False
                break
            elif H[i][j] - h == 1:
                if j - L < 0:
                    flag = False
                    break
                for k in range(L, 0, -1):
                    if H[i][j - k] != h or exist[j - k] == 1:
                        flag = False
                        break
                    exist[j - k] = 1
                if not flag:
                    break
                h = H[i][j]
            elif H[i][j] - h == -1:
                if j + L - 1 >= N:
                    flag = False
                    break
                for k in range(L):
                    if H[i][j + k] != h - 1 or exist[j + k] == 1:
                        flag = False
                        break
                    exist[j + k] = 1
                if not flag:
                    break
                h = H[i][j]
        if not flag:
            cnt -= 1
    return cnt

def sero(N, L, H):
    cnt = N
    for i in range(N):
        h = H[0][i]
        exist = [0] * N
        flag = True
        for j in range(N):
            if abs(H[j][i] - h) > 1:
                flag = False
                break
            elif H[j][i] - h == 1:
                if j - L < 0:
                    flag = False
                    break
                for k in range(L, 0, -1):
                    if H[j - k][i] != h or exist[j - k] == 1:
                        flag = False
                        break
                    exist[j - k] = 1
                if not flag:
                    break
                h = H[j][i]
            elif H[j][i] - h == -1:
                if j + L - 1 >= N:
                    flag = False
                    break
                for k in range(L):
                    if H[j + k][i] != h - 1 or exist[j + k] == 1:
                        flag = False
                        break
                    exist[j + k] = 1
                if not flag:
                    break
                h = H[j][i]
        if not flag:
            cnt -= 1
    return cnt

def solve():
    N, L = map(int, input().split())
    H = [[*map(int, input().split())] for _ in range(N)]
    print(garo(N, L, H) + sero(N, L, H))

solve()