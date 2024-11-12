def solve():
    N = int(input())
    S = input()
    num = {'A': 0, 'G': 1, 'C': 2, 'T': 3}
    change = [[0, 2, 0, 1],
            [2, 1, 3, 0],
            [0, 3, 2, 1],
            [1, 0, 1, 3]]
    last = num[S[-1]]
    for c in range(N - 2, -1, -1):
        last = change[num[S[c]]][last]
    print("AGCT"[last])

solve()