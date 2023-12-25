import sys
input = sys.stdin.readline

sosu = [False, False] + [False, True] * 1000000
sosu[2] = True
for i in range(3, 1001):
    if sosu[i]:
        for j in range(i + i, 1000001, i):
            sosu[j] = False

T = int(input())
for _ in range(T):
    N = int(input())
    ans = 0
    for i in range(1, N // 2 + 1):
        if sosu[i] and sosu[N - i]:
            ans += 1
    print(ans)