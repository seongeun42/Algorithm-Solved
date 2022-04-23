import sys
input = sys.stdin.readline

N = int(input())
S = [*map(int, input().split())]
for _ in range(int(input())):
    g, v = map(int, input().split())
    if g == 1:
        for i in range(v - 1, N, v):
            S[i] = 0 if S[i] else 1
    else:
        if v == 1 or v == N:
            S[v - 1] = 0 if S[v - 1] else 1
        else:
            l, r = v - 2, v
            S[v - 1] = 0 if S[v - 1] else 1
            while l >= 0 and r < N:
                if S[l] == S[r]:
                    S[l] = 0 if S[l] else 1
                    S[r] = S[l]
                    l -= 1
                    r += 1
                else:
                    break
for i in range(N):
    print(S[i], end=' ')
    if i % 20 == 19:
        print()