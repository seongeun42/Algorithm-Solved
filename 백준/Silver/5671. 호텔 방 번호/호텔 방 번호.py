while 1:
    try:
        N, M = map(int, input().split())
        cnt = 0
        for v in range(N, M + 1):
            s = set(list(str(v)))
            if len(s) == len(str(v)):
                cnt += 1
        print(cnt)
    except EOFError:
        break