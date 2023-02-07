from collections import deque
N, K = map(int, input().split())
A = [*map(int, input().split())]
belt = deque([[0, v] for v in A])
zero = 0
ans = 0
while zero < K:
    ans += 1
    belt.rotate(1)
    belt[N - 1][0] = 0
    for i in range(N - 2, -1, -1):
        if belt[i][0] and belt[i + 1][0] == 0 and belt[i + 1][1] > 0:
            belt[i][0] = 0
            belt[i + 1][0] = 1
            belt[i + 1][1] -= 1
            if belt[i + 1][1] == 0:
                zero += 1
    belt[N - 1][0] = 0
    if belt[0][1] > 0:
        belt[0][0] = 1
        belt[0][1] -= 1
        if belt[0][1] == 0:
            zero += 1
print(ans)