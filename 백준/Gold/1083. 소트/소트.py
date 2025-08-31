import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = [*map(int, input().split())]
    S = int(input())
    for i in range(N - 1):
        if S == 0:
            break
        max_v, idx = arr[i], i
        for j in range(i + 1, min(N, i + S + 1)):
            if arr[j] > max_v:
                max_v, idx = arr[j], j
        S -= idx - i
        for j in range(idx, i, - 1):
            arr[j] = arr[j - 1]
        arr[i] = max_v
    print(*arr)

solve()