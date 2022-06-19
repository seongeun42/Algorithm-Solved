for _ in range(3):
    sh, sm, ss, eh, em, es = map(int, input().split())
    start = (sh * 3600) + (sm * 60) + ss
    end = (eh * 3600) + (em * 60) + es
    work = end - start
    wh = work // 3600
    wm = (work % 3600) // 60
    ws = (work % 3600) % 60
    print(wh, wm, ws)