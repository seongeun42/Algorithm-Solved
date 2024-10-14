import sys
input = sys.stdin.readline

def solve():
    check = [False, False] + [True] * 1299710
    for i in range(2, int(1299710**0.5)):
        if not check[i]:
            continue
        for j in range(i + i, 1299710, i):
            check[j] = False
    sosu = [i for i in range(len(check)) if check[i]]
    T = int(input())
    for _ in range(T):
        k = int(input())
        if check[k]:
            print(0)
        else:
            s, e = 0, len(sosu) - 1
            idx = 0
            while s <= e:
                mid = (s + e) // 2
                if k < sosu[mid]:
                    e = mid - 1
                    idx = mid
                else:
                    s = mid + 1
            print(sosu[idx] - sosu[idx - 1])

solve()