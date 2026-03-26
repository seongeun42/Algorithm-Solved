import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    C = [*map(int, input().split())]
    for i, v in enumerate(C):
        if v % 2 == 1:
            C[i] += 1
    ans = 0
    while len(set(C)) > 1:
        ans += 1
        half = [0] * N
        for i, v in enumerate(C):
            C[i] = v // 2
            half[(i + 1) % N] = v // 2
        for i in range(N):
            C[i] += half[i]
            if C[i] % 2 == 1:
                C[i] += 1
    print(ans)