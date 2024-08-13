import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, M = map(int, input().split())
    R = [i for i in range(N + 1)]
    index = {input().rstrip(): i+1 for i in range(N)}
    for _ in range(M):
        a, b, war = input().rstrip().split(",")
        ai, bi = index[a], index[b]
        ar = find_root(ai, R)
        br = find_root(bi, R)
        if ar != br:
            if war == '1':
                R[br] = ar
            else:
                R[ar] = br
        else:
            if war == '1' and ar != ai:
                R[ai], R[br] = ai, ai
            elif war == '2' and br != bi:
                R[bi], R[ar] = bi, bi
    name = list(index.keys())
    ans = []
    for i in range(1, N + 1):
        if find_root(i, R) == i:
            ans.append(name[i - 1])
    print(len(ans))
    ans.sort()
    for v in ans:
        print(v)

solve()