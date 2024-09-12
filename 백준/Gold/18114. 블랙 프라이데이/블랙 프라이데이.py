import sys
input = sys.stdin.readline

def binary_search(s, e, diff, w):
    while s <= e:
        mid = (s + e) // 2
        if w[mid] == diff:
            return True
        elif w[mid] < diff:
            s = mid + 1
        else:
            e = mid - 1
    return False

def solve():
    N, C = map(int, input().split())
    w = sorted([*map(int, input().split())])
    if binary_search(0, N - 1, C, w):
        print(1)
        return
    l, r = 0, N - 1
    while l < r:
        if w[l] + w[r] == C:
            print(1)
            return
        if w[l] + w[r] > C:
            r -= 1
        else:
            diff = C - w[r] - w[l]
            if diff != w[r] and diff != w[l] and binary_search(l, r, diff, w):
                print(1)
                return
            l += 1
    print(0)
    return

solve()