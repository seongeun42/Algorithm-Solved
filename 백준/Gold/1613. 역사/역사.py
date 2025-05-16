import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    arr = [[0] * n for _ in range(n)]
    for _ in range(k):
        bf, af = map(int, input().split())
        arr[bf - 1][af - 1] = -1
        arr[af - 1][bf - 1] = 1
    for m in range(n):
        for s in range(n):
            for e in range(n):
                if s == e or arr[s][e] != 0:
                    continue
                if arr[s][m] != 0 and arr[m][e] != 0:
                    if arr[s][m] == -1 and arr[m][e] == -1:
                        arr[s][e] = -1
                        arr[e][s] = 1
                    elif arr[s][m] == 1 and arr[m][e] == 1:
                        arr[s][e] = 1
                        arr[e][s] = -1
    s = int(input())
    for _ in range(s):
        c1, c2 = map(int, input().split())
        print(arr[c1 - 1][c2 - 1])

solve()