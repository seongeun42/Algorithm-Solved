import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    n = int(input())
    A = [*map(int, input().split())]
    m = int(input())
    B = [*map(int, input().split())]

    a_prefix = [A[0]]
    a_sum = {A[0]: 1}
    for i in range(1, n):
        a_prefix.append(a_prefix[i - 1] + A[i])
        a_sum[a_prefix[i]] = a_sum.get(a_prefix[i], 0) + 1
        for j in range(i):
            v = a_prefix[i] - a_prefix[j]
            a_sum[v] = a_sum.get(v, 0) + 1

    b_prefix = [B[0]]
    b_sum = {B[0]: 1}
    for i in range(1, m):
        b_prefix.append(b_prefix[i - 1] + B[i])
        b_sum[b_prefix[i]] = b_sum.get(b_prefix[i], 0) + 1
        for j in range(i):
            v = b_prefix[i] - b_prefix[j]
            b_sum[v] = b_sum.get(v, 0) + 1

    ans = 0
    for key in a_sum.keys():
        ans += b_sum.get(T - key, 0) * a_sum[key]

    print(ans)

solve()