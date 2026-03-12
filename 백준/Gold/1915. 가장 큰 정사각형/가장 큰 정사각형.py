import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        line = input().rstrip()
        arr.append([int(c) for c in line])
    ans = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                continue
            if i != 0 and j != 0:
                arr[i][j] += min(arr[i - 1][j - 1], arr[i - 1][j], arr[i][j - 1])
            if ans < arr[i][j]:
                ans = arr[i][j]
    print(ans ** 2)

solve()