import sys
input = sys.stdin.readline

def find_root(node, R):
    if R[node] < 0:
        return node
    else:
        R[node] = find_root(R[node], R)
    return R[node]

if __name__ == "__main__":
    N, M = map(int, input().split())
    E = sorted([[*map(int, input().split())] for _ in range(M)], key=lambda x: -x[2])
    fac1, fac2 = map(int, input().split())
    R = [-1] * (N + 1)
    ans = 0
    for a, b, c in E:
        ar = find_root(a, R)
        br = find_root(b, R)
        if ar != br:
            if R[ar] <= R[br]:
                R[ar] += R[br]
                R[br] = ar
            else:
                R[br] += R[ar]
                R[ar] = br
        if find_root(fac1, R) == find_root(fac2, R):
            print(c)
            break