def yaksu(n):
    ys = {1}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ys.add(i)
            ys.add(n // i)
    return ys

while 1:
    n = int(input())
    if n == -1: break
    ys = yaksu(n)
    if sum(ys) == n:
        print(n, "= ", end="")
        print(*sorted(list(ys)), sep=" + ")
    else:
        print(n, "is NOT perfect.")