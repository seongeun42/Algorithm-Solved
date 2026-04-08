import sys
input = sys.stdin.readline

n, k = map(int, input().split())
tall = [*map(int, input().split())]
if n == 1:
    print(0)
else:
    H = []
    for i in range(n):
        if i == 0:
            H.append(abs(tall[i] - tall[i + 1]))
        elif i == n - 1:
            H.append(abs(tall[i] - tall[i - 1]))
        else:
            H.append(max(abs(tall[i] - tall[i - 1]), abs(tall[i] - tall[i + 1])))
    H.sort(reverse=True)
    if n == k:
        print(0)
    else:
        print(H[k])