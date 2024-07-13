import sys
input = sys.stdin.readline

def count(arr, presum, size):
    cnt = {}
    for l in range(len(arr)):
        for r in range(len(arr) - 1):
            hap = presum[l + r] - presum[l] + arr[l]
            if hap > size:
                break
            cnt[hap] = cnt.get(hap, 0) + 1
    all = presum[len(arr) - 1]
    if all <= size:
        cnt[all] = cnt.get(all, 0) + 1
    return cnt

def solve():
    want = int(input())
    m, n = map(int, input().split())
    A = [int(input()) for _ in range(m)]
    B = [int(input()) for _ in range(n)]
    pre_a = A[:] + A[:m - 1]
    pre_b = B[:] + B[:n - 1]
    for i in range(1, 2*m - 1):
        pre_a[i] += pre_a[i - 1]
    for i in range(1, 2*n - 1):
        pre_b[i] += pre_b[i - 1]
    ans = 0
    a_cnt = count(A, pre_a, want)
    b_cnt = count(B, pre_b, want)
    for a_size in range(want + 1):
        b_size = want - a_size
        if a_size == 0:
            ans += b_cnt.get(want, 0)
        elif b_size == 0:
            ans += a_cnt.get(want, 0)
        else:
            ans += a_cnt.get(a_size, 0) * b_cnt.get(b_size, 0)
    print(ans)

solve()