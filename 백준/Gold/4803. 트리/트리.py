import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    t = 1
    while t:
        n, m = map(int, input().split())
        if n == m == 0:
            break
        R = list(range(n + 1))
        no_tree = set()
        for _ in range(m):
            u, v = map(int, input().split())
            ur = find_root(u, R)
            vr = find_root(v, R)
            if ur != vr:
                if ur in no_tree or vr in no_tree:
                    no_tree.add(ur)
                    no_tree.add(vr)
                R[max(ur, vr)] = min(ur, vr)
            else:
                no_tree.add(ur)
        tree_cnt = 0
        for i in range(1, n + 1):
            if find_root(i, R) == i and i not in no_tree:
                tree_cnt += 1
        if tree_cnt == 0:
            print(f"Case {t}: No trees.")
        elif tree_cnt == 1:
            print(f"Case {t}: There is one tree.")
        else:
            print(f"Case {t}: A forest of {tree_cnt} trees.")
        t += 1

solve()