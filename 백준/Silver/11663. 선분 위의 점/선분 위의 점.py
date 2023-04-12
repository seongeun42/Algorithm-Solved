import sys
input = sys.stdin.readline

def find_min_idx(num):
    s, e = 0, n - 1
    while s <= e:
        mid = (s + e) // 2
        if dot[mid] < num:
            s = mid + 1
        else:
            e = mid - 1
    return e + 1

def find_max_idx(num):
    s, e = 0, n - 1
    while s <= e:
        mid = (s + e) // 2
        if dot[mid] > num:
            e = mid - 1
        else:
            s = mid + 1
    return e

n, m = map(int, input().split())
dot = sorted([*map(int, input().split())])
for _ in range(m):
    a, b = map(int, input().split())
    si = find_min_idx(a)
    ei = find_max_idx(b)
    print(ei - si + 1)