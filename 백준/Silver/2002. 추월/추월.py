import sys
input = sys.stdin.readline

N = int(input())
I = {input().strip(): i for i in range(N)}
O = [input().strip() for _ in range(N)]
cnt = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if I[O[i]] > I[O[j]]:
            cnt += 1
            break
print(cnt)