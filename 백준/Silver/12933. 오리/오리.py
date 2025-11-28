def solve():
    S = input()
    if S[0] != 'q' or len(S) % 5 > 0:
        print(-1)
        exit()
    quack = "quack"
    visited = [False] * len(S)
    cnt = 0
    for i, c in enumerate(S):
        if c == 'q' and not visited[i]:
            si = 0
            start = True
            for j in range(i, len(S)):
                if S[j] == quack[si] and not visited[j]:
                    visited[j] = True
                    if start and quack[si] == 'k':
                        cnt += 1
                        start = False
                    si = (si + 1) % 5
    print(-1 if not all(visited) or cnt == 0 else cnt)

solve()