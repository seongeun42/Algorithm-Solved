import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    sorted_arr = sorted(arr, reverse=True)
    i = arr.index(sorted_arr[0])
    cnt = 1
    for j in range(i - 1, -1, -1):
        if arr[j] == sorted_arr[cnt]:
            cnt += 1
    print(N - cnt)

solve()