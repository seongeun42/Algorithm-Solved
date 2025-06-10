def solve():
    N = int(input())
    arr = [*map(int, input().split())]
    if N == 1:
        return 'A'
    if N == 2:
        return 'A' if arr[0] != arr[1] else arr[-1]
    a = (arr[2] - arr[1]) / (arr[1] - arr[0]) if arr[0] != arr[1] else 0
    if a != int(a):
        return 'B'
    a = int(a)
    b = arr[1] - arr[0] * a
    for i in range(N - 1):
        if arr[i] * a + b != arr[i + 1]:
            return 'B'
    return arr[-1] * a + b

print(solve())