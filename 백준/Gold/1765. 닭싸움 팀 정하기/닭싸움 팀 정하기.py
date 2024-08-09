import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    n = int(input())
    R = [i for i in range(n + 1)]
    enermy = [0] * (n + 1)
    m = int(input())
    for _ in range(m):
        r, a, b = input().split()
        a, b = int(a), int(b)
        if r == 'F':
            ar = find_root(a, R)
            br = find_root(b, R)
            if ar != br:
                R[max(ar, br)] = min(ar, br)
        else:
            if enermy[a] != 0:
                aer = find_root(enermy[a], R)
                br = find_root(b, R)
                if aer != br:
                    R[max(aer, br)] = min(aer, br)
            enermy[a] = b
            if enermy[b] != 0:
                ar = find_root(a, R)
                ber = find_root(enermy[b], R)
                if ar != ber:
                    R[max(ar, ber)] = min(ar, ber)
            enermy[b] = a
    ans = 0
    for i in range(1, n + 1):
        if find_root(i, R) == i:
            ans += 1
    print(ans)

solve()