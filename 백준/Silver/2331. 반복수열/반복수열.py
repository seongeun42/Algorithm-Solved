def next(n, P):
    nxt = 0
    while n:
        n, v = divmod(n, 10)
        nxt += v ** P
    return nxt

A, P = map(int, input().split())
arr = [A]
exist = {A}
while 1:
    nxt = next(arr[-1], P)
    if nxt in exist:
        while arr.pop() != nxt:
            continue
        print(len(arr))
        break
    arr.append(nxt)
    exist.add(nxt)