import sys
input = sys.stdin.readline

while 1:
    N = int(input())
    if N == 0:
        break
    st = [list(input().rstrip().split()) for _ in range(N)]
    st = sorted([[float(st[i][1]), st[i][0], i] for i in range(N)], key=lambda x: (-x[0], x[2]))
    ans = [st[0][1]]
    i = 1
    while i < N and st[i - 1][0] == st[i][0]:
        ans.append(st[i][1])
        i += 1
    print(*ans)